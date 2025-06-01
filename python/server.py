# _*- coding : utf-8_*_
# @Time : 2025/6/1 下午9:54
# @Author : NINE
# @File : server
# @Project : bilibili-downloader
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import os
import re
import requests
import json
from bs4 import BeautifulSoup
from moviepy.editor import VideoFileClip, AudioFileClip

app = Flask(__name__)

headers = {
    "referer": "https://www.bilibili.com ",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

# 获取桌面路径
def get_desktop_path():
    if os.name == 'nt':  # Windows
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        desktop = winreg.QueryValueEx(key, "Desktop")[0]
        winreg.CloseKey(key)
        return desktop
    else:  # Mac and Linux
        return os.path.join(os.path.expanduser('~'), 'Desktop')

def sanitize_filename(filename):
    return re.sub(r'[\\/:*?"<>|]', '', filename).strip()

def get_play_info(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('h1', {'class': 'video-title'}) or soup.find('h1')
        filename = sanitize_filename(title_tag.get_text().strip()) if title_tag else "untitled"

        play_info = re.search(r'window\.__playinfo__=(.*?)</script>', response.text)
        if not play_info:
            raise ValueError("无法提取视频播放信息")

        play_data = json.loads(play_info.group(1))
        video_url = play_data["data"]["dash"]["video"][0]["baseUrl"]
        audio_url = play_data["data"]["dash"]["audio"][0]["baseUrl"]

        return video_url, audio_url, filename

    except Exception as e:
        print(f"获取视频信息失败: {e}")
        raise

def download_file(url, filepath):
    try:
        with requests.get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))

            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print(f"文件已保存到: {filepath}")
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return False

def combine_with_moviepy(video_path, audio_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)

        if audio_clip.duration > video_clip.duration:
            audio_clip = audio_clip.subclip(0, video_clip.duration)
        elif audio_clip.duration < video_clip.duration:
            audio_clip = audio_clip.audio_loop(duration=video_clip.duration)

        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            threads=4,
            fps=video_clip.fps,
            bitrate="5000k"
        )

        video_clip.close()
        audio_clip.close()
        final_clip.close()

        print("音视频合并成功")
        os.remove(video_path)
        os.remove(audio_path)
        print("已删除临时文件")
        return True

    except Exception as e:
        print(f"合并过程中出错: {e}")
        return False

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get('url')
        custom_name = data.get('customName', '')

        if not url:
            return jsonify({'error': 'URL不能为空'}), 400

        # 获取桌面路径并创建bilibili_downloads文件夹
        desktop = get_desktop_path()
        base_dir = os.path.join(desktop, "bilibili_downloads")
        os.makedirs(base_dir, exist_ok=True)

        video_url, audio_url, filename = get_play_info(url)
        if custom_name:
            filename = sanitize_filename(custom_name)

        video_temp = os.path.join(base_dir, f"{filename}_temp.mp4")
        audio_temp = os.path.join(base_dir, f"{filename}_temp.mp3")
        output_file = os.path.join(base_dir, f"{filename}.mp4")

        print("正在下载视频部分...")
        if not download_file(video_url, video_temp):
            return jsonify({'error': '视频下载失败'}), 500

        print("正在下载音频部分...")
        if not download_file(audio_url, audio_temp):
            return jsonify({'error': '音频下载失败'}), 500

        print("正在合并音视频...")
        if combine_with_moviepy(video_temp, audio_temp, output_file):
            return jsonify({
                'success': True,
                'message': f'视频下载完成: {output_file}',
                'filepath': output_file
            })

        return jsonify({'error': '视频处理失败'}), 500

    except Exception as e:
        print(f"程序运行出错: {e}")
        return jsonify({'error': f'发生错误: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
