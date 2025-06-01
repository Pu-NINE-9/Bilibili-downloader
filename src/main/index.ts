import { app, BrowserWindow, ipcMain } from 'electron'
import path from 'path'
import { spawn } from 'child_process'

let mainWindow: BrowserWindow | null = null
let pythonProcess: any = null

function startPythonServer() {
  const isDev = !app.isPackaged
  const pythonPath = isDev ? 'python' : path.join(process.resourcesPath, 'python', 'server.py')

  const scriptPath = isDev
    ? path.join(__dirname, '../../python/server.py')
    : path.join(process.resourcesPath, 'python/server.py')

  pythonProcess = spawn(pythonPath, [scriptPath])

  pythonProcess.stdout.on('data', (data: Buffer) => {
    console.log(`Python: ${data.toString()}`)
  })

  pythonProcess.stderr.on('data', (data: Buffer) => {
    console.error(`Python Error: ${data.toString()}`)
  })

  pythonProcess.on('close', (code: number) => {
    console.log(`Python process exited with code ${code}`)
  })
}

async function createWindow() {
  mainWindow = new BrowserWindow({
    webPreferences: {
      preload: path.join(__dirname, '../preload/index.js'),
      contextIsolation: true,
      sandbox: true
    },
    width: 900,
    height: 700
  })

  startPythonServer()

  if (process.env.VITE_DEV_SERVER_URL) {
    await mainWindow.loadURL(process.env.VITE_DEV_SERVER_URL)
    mainWindow.webContents.openDevTools()
  } else {
    await mainWindow.loadFile(path.join(__dirname, '../renderer/index.html'))
  }

  return mainWindow
}

app.whenReady().then(async () => {
  await createWindow()

  app.on('activate', async () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      await createWindow()
    }
  })
})

app.on('window-all-closed', () => {
  if (pythonProcess) {
    pythonProcess.kill()
  }
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

ipcMain.handle('download-video', async (_, { url, customName, savePath }) => {
  try {
    const response = await fetch('http://localhost:5000/download', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url, customName, savePath: savePath || 'bilibili_downloads' })
    })
    return await response.json()
  } catch (error: any) {
    return { error: true, message: error.message }
  }
})
