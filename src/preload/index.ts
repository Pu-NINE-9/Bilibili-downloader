import { contextBridge, ipcRenderer } from 'electron'

contextBridge.exposeInMainWorld('electronAPI', {
  downloadVideo: (data: any) => ipcRenderer.invoke('download-video', data)
})
