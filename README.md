# Bilibili Downloader - 项目说明文档(Project Description Document)
#### 免责声明
本项目仅为个人兴趣开发，仅供个人学习和研究使用！严禁将本项目用于任何商业用途或其他未经授权的活动！使用本项目时，请确保遵守相关法律法规以及 Bilibili 的使用条款！项目开发者不对任何未经授权的使用行为及其后果负责！


### 中文版(Chinese version)
## 📌 项目概述
大家好~我是NINE。这是我开发的第二个全栈项目 --- Bilibili Downloader。该项目是一个基于 Electron + Vue + TypeScript + Flask 的跨平台桌面应用，用于下载 Bilibili 视频内容。本项目采用现代前端技术栈开发，支持 Windows、macOS 和 Linux 三大平台。
## 🛠️ 技术栈
### 核心框架
- **Electron (v28+)**: 跨平台桌面应用框架
- **Vue3**: 前端框架
- **TypeScript**: 类型安全的 JavaScript 超集
- **Flask**: 后端框架，用于处理视频下载逻辑

### 前端技术
- **Pinia**: 状态管理
- **Vite**: 构建工具
- **Sass/Scss**: CSS 预处理器

### 后端技术
- **Node.js (v22+)**: 运行时环境
- **Axios**: HTTP 客户端
- **FFmpeg**: 视频处理（如需）
- **Requests**: 用于发送 HTTP 请求，获取网页内容
- **BeautifulSoup**: 用于解析 HTML 内容，提取视频信息
- **moviepy**: 用于合并下载的视频和音频文件

### 开发工具
- **ESLint**: 代码质量检查
- **Prettier**: 代码格式化
- **Volar**: Vue 开发工具

## 🚀 快速开始
### 环境要求
- Node.js v22.x
- pnpm v8.x
- Git

### 安装依赖
```bash
pnpm install
```

### 开发模式
```bash
pnpm dev
```

### 构建应用
```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

## ✨ 功能特性

### 当前版本 (v1.0.0)
- ✅ B站视频下载功能
- ✅ 多清晰度选择支持
- ✅ 下载队列管理
- ✅ 跨平台支持 (Windows/macOS/Linux)
- ✅ 响应式用户界面

### 计划功能
- 🔲 下载历史记录
- 🔲 自定义下载路径
- 🔲 主题切换功能

## 🏗️ 项目结构
```
bilibili-downloader/
├── electron/          # Electron 主进程代码
├── src/               # 前端源代码
│   ├── assets/        # 静态资源
│   ├── components/    # Vue 组件
│   ├── stores/        # Pinia 状态管理
│   ├── utils/         # 工具函数
│   └── views/         # 页面组件
├── build/             # 构建相关配置
├── public/            # 公共资源
├── server/            # 后端服务代码
│   ├── __init__.py    # Flask 应用初始化
│   ├── routes.py      # 路由定义
│   ├── utils.py       # 工具函数
│   └── download.py    # 视频下载逻辑
└── package.json       # 项目配置
```

## 📬 联系开发者
如有任何问题或建议，欢迎通过以下方式联系我哟
- CSDN: [Pu_Nine_9-CSDN博客]https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343
- 
Happy Coding! 🎉


### English version
## 📌 Project Overview
Hello everyone! I'm NINE. This is my second full-stack project --- Bilibili Downloader. It is a cross-platform desktop application for downloading Bilibili video content, developed using the modern front-end technology stack and supports Windows, macOS, and Linux platforms.

## 🛠️ Technology Stack
### Core Frameworks
- **Electron (v28+)**: Cross-platform desktop application framework
- **Vue3**: Front-end framework
- **TypeScript**: A type-safe superset of JavaScript
- **Flask**: Back-end framework for handling video download logic

### Front-end Technologies
- **Pinia**: State management
- **Element Plus**: UI component library
- **Vite**: Build tool
- **Sass/Scss**: CSS preprocessor

### Back-end Technologies
- **Node.js (v22+)**: Runtime environment
- **Axios**: HTTP client
- **FFmpeg**: Video processing (if needed)
- **Requests**: For sending HTTP requests and obtaining web content
- **BeautifulSoup**: For parsing HTML content and extracting video information
- **moviepy**: For merging downloaded video and audio files

### Development Tools
- **ESLint**: Code quality check
- **Prettier**: Code formatting
- **Volar**: Vue development tool

## 🚀 Quick Start
### Environment Requirements
- Node.js v22.x
- pnpm v8.x
- Git

### Install Dependencies
```bash
pnpm install
```

### Development Mode
```bash
pnpm dev
```

### Build the Application
```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

## ✨ Features

### Current Version (v1.0.0)
- ✅ Bilibili video download function
- ✅ Support for multiple clarity options
- ✅ Download queue management
- ✅ Cross-platform support (Windows/macOS/Linux)
- ✅ Responsive user interface

### Planned Features
- 🔲 Download history
- 🔲 Customizable download path
- 🔲 Theme switching function

## 🏗️ Project Structure
```
bilibili-downloader/
├── electron/          # Electron main process code
├── src/               # Front-end source code
│   ├── assets/        # Static resources
│   ├── components/    # Vue components
│   ├── stores/        # Pinia state management
│   ├── utils/         # Utility functions
│   └── views/         # Page components
├── build/             # Build-related configuration
├── public/            # Public resources
├── server/            # Back-end service code
│   ├── __init__.py    # Flask application initialization
│   ├── routes.py      # Route definition
│   ├── utils.py       # Utility functions
│   └── download.py    # Video download logic
└── package.json       # Project configuration
```

## 📬 Contact the Developer
If you have any questions or suggestions, feel free to contact me through the following ways:
- CSDN: [Pu_Nine_9-CSDN博客](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉


### 日本語版(Japanese version)
## 📌 プロジェクト概要
こんにちは、NINEです。これは私の2番目のフルスタックプロジェクトです。Bilibili Downloaderは、Bilibiliのビデオコンテンツをダウンロードするためのクロスプラットフォームデスクトップアプリケーションで、モダンなフロントエンド技術スタックを使用して開発され、Windows、macOS、Linuxの3つのプラットフォームをサポートしています。

## 🛠️ 技術スタック
### コアフレームワーク
- **Electron (v28+)**: クロスプラットフォームデスクトップアプリケーションフレームワーク
- **Vue3**: フロントエンドフレームワーク
- **TypeScript**: タイプセーフなJavaScriptのスーパーセット
- **Flask**: ビデオダウンロードロジックを処理するためのバックエンドフレームワーク

### フロントエンド技術
- **Pinia**: ステート管理
- **Vite**: ビルドツール
- **Sass/Scss**: CSSプリプロセッサ

### バックエンド技術
- **Node.js (v22+)**: ランタイム環境
- **Axios**: HTTPクライアント
- **FFmpeg**: ビデオ処理（必要に応じて）
- **Requests**: HTTPリクエストを送信してウェブコンテンツを取得するためのもの
- **BeautifulSoup**: HTMLコンテンツを解析してビデオ情報を抽出するためのもの
- **moviepy**: ダウンロードされたビデオとオーディオファイルを結合するためのもの

### 開発ツール
- **ESLint**: コード品質チェック
- **Prettier**: コードフォーマッティング
- **Volar**: Vue開発ツール

## 🚀 クイックスタート
### 環境要件
- Node.js v22.x
- pnpm v8.x
- Git

### 依存関係のインストール
```bash
pnpm install
```

### 開発モード
```bash
pnpm dev
```

### アプリケーションのビルド
```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

## ✨ 機能
### 現在のバージョン (v1.0.0)
- ✅ Bilibiliビデオのダウンロード機能
- ✅ 複数の画質オプションのサポート
- ✅ ダウンロードキューの管理
- ✅ クロスプラットフォームのサポート (Windows/macOS/Linux)
- ✅ レスポンシブユーザーインターフェース

### 計画機能
- 🔲 ダウンロード履歴
- 🔲 カスタマイズ可能なダウンロードパス
- 🔲 テーマ切り替え機能

## 🏗️ プロジェクト構造
```
bilibili-downloader/
├── electron/          # Electronメインプロセスコード
├── src/               # フロントエンドソースコード
│   ├── assets/        # 静的リソース
│   ├── components/    # Vueコンポーネント
│   ├── stores/        # Piniaステート管理
│   ├── utils/         # ユーティリティ関数
│   └── views/         # ページコンポーネント
├── build/             # ビルド関連の設定
├── public/            # 公開リソース
├── server/            # バックエンドサービスコード
│   ├── __init__.py    # Flaskアプリケーションの初期化
│   ├── routes.py      # ルート定義
│   ├── utils.py       # ユーティリティ関数
│   └── download.py    # ビデオダウンロードロジック
└── package.json       # プロジェクト設定
```

## 📬 開発者に連絡する
質問や提案があれば、以下の方法で連絡してください。
- CSDN: [Pu_Nine_9-CSDNブログ](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉


### 한국어 버전(Korean version)
## 📌 프로젝트 개요
안녕하세요, NINE입니다. 이 프로젝트는 Bilibili Downloader로, Bilibili의 동영상 콘텐츠를 다운로드하는 크로스 플랫폼 데스크톱 애플리케이션입니다. 현대적인 프론트엔드 기술 스택을 사용하여 개발되었으며, Windows, macOS, Linux 세 플랫폼을 지원합니다.

## 🛠️ 기술 스택
### 코어 프레임워크
- **Electron (v28+)**: 크로스 플랫폼 데스크톱 애플리케이션 프레임워크
- **Vue3**: 프론트엔드 프레임워크
- **TypeScript**: 타입 안전한 JavaScript의 슈퍼셋
- **Flask**: 비디오 다운로드 로직을 처리하는 백엔드 프레임워크

### 프론트엔드 기술
- **Pinia**: 상태 관리
- **Vite**: 빌드 도구
- **Sass/Scss**: CSS 프리프로세서

### 백엔드 기술
- **Node.js (v22+)**: 런타임 환경
- **Axios**: HTTP 클라이언트
- **FFmpeg**: 비디오 처리 (필요 시)
- **Requests**: HTTP 요청을 보내고 웹 콘텐츠를 가져옴
- **BeautifulSoup**: HTML 콘텐츠를 파싱하여 비디오 정보를 추출함
- **moviepy**: 다운로드된 비디오와 오디오 파일을 합침

### 개발 도구
- **ESLint**: 코드 품질 검사
- **Prettier**: 코드 포맷팅
- **Volar**: Vue 개발 도구

## 🚀 빠른 시작
### 환경 요구 사항
- Node.js v22.x
- pnpm v8.x
- Git

### 종속성 설치
```bash
pnpm install
```

### 개발 모드
```bash
pnpm dev
```

### 애플리케이션 빌드
```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

## ✨ 기능
### 현재 버전 (v1.0.0)
- ✅ Bilibili 비디오 다운로드 기능
- ✅ 다중 해상도 선택 지원
- ✅ 다운로드 대기열 관리
- ✅ 크로스 플랫폼 지원 (Windows/macOS/Linux)
- ✅ 반응형 사용자 인터페이스

### 계획 기능
- 🔲 다운로드 기록
- 🔲 사용자 정의 다운로드 경로
- 🔲 테마 전환 기능

## 🏗️ 프로젝트 구조
```
bilibili-downloader/
├── electron/          # Electron 메인 프로세스 코드
├── src/               # 프론트엔드 소스 코드
│   ├── assets/        # 정적 리소스
│   ├── components/    # Vue 컴포넌트
│   ├── stores/        # Pinia 상태 관리
│   ├── utils/         # 유틸리티 함수
│   └── views/         # 페이지 컴포넌트
├── build/             # 빌드 관련 설정
├── public/            # 공용 리소스
├── server/            # 백엔드 서비스 코드
│   ├── __init__.py    # Flask 애플리케이션 초기화
│   ├── routes.py      # 라우트 정의
│   ├── utils.py       # 유틸리티 함수
│   └── download.py    # 비디오 다운로드 로직
└── package.json       # 프로젝트 설정
```

## 📬 개발자에게 연락하기
문제나 제안이 있다면, 다음 방법으로 연락해 주세요.
- CSDN: [Pu_Nine_9-CSDN 블로그](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉
# Bilibili Downloader - 项目说明文档(Project Description Document)
### 免责声明
本项目仅为个人兴趣开发，仅供个人学习和研究使用！严禁将本项目用于任何商业用途或其他未经授权的活动！使用本项目时，请确保遵守相关法律法规以及 Bilibili 的使用条款！项目开发者不对任何未经授权的使用行为及其后果负责！


## 中文版 (Chinese Version)
# 📌 项目概述
大家好，我是 NINE。这是我开发的第二个全栈项目——Bilibili Downloader。该项目是一个基于 Electron + Vue + TypeScript + Flask 的跨平台桌面应用，用于下载 Bilibili 视频内容。本项目采用现代前端技术栈开发，支持 Windows、macOS 和 Linux 三大平台。

# 🛠️ 技术栈

## 核心框架

- **Electron (v28+)**：跨平台桌面应用框架
- **Vue3**：前端框架
- **TypeScript**：类型安全的 JavaScript 超集
- **Flask**：后端框架，用于处理视频下载逻辑

## 前端技术

- **Pinia**：状态管理
- **Vite**：构建工具
- **Sass/Scss**：CSS 预处理器

## 后端技术

- **Node.js (v22+)**：运行时环境
- **Axios**：HTTP 客户端
- **FFmpeg**：视频处理（如需）
- **Requests**：用于发送 HTTP 请求，获取网页内容
- **BeautifulSoup**：用于解析 HTML 内容，提取视频信息
- **moviepy**：用于合并下载的视频和音频文件

## 开发工具

- **ESLint**：代码质量检查
- **Prettier**：代码格式化
- **Volar**：Vue 开发工具

# 🚀 快速开始

## 环境要求

- Node.js v22.x
- pnpm v8.x
- Git

## 安装依赖

```bash
pnpm install
```

## 开发模式

```bash
pnpm dev
```

## 构建应用

```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

# ✨ 功能特性

## 当前版本 (v1.0.0)

- ✅ B站视频下载功能
- ✅ 多清晰度选择支持
- ✅ 下载队列管理
- ✅ 跨平台支持 (Windows/macOS/Linux)
- ✅ 响应式用户界面

## 计划功能

- 🔲 下载历史记录
- 🔲 自定义下载路径
- 🔲 主题切换功能

# 🏗️ 项目结构

```
bilibili-downloader/
├── electron/          # Electron 主进程代码
├── src/               # 前端源代码
│   ├── assets/        # 静态资源
│   ├── components/    # Vue 组件
│   ├── stores/        # Pinia 状态管理
│   ├── utils/         # 工具函数
│   └── views/         # 页面组件
├── build/             # 构建相关配置
├── public/            # 公共资源
├── server/            # 后端服务代码
│   ├── __init__.py    # Flask 应用初始化
│   ├── routes.py      # 路由定义
│   ├── utils.py       # 工具函数
│   └── download.py    # 视频下载逻辑
└── package.json       # 项目配置
```

# 📬 联系开发者

如有任何问题或建议，欢迎通过以下方式联系我：

- CSDN: [Pu_Nine_9-CSDN博客](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉


## English Version
# 📌 Project Overview
Hello everyone! I'm NINE. This is my second full-stack project — Bilibili Downloader. It is a cross-platform desktop application for downloading Bilibili video content, developed using the modern front-end technology stack and supports Windows, macOS, and Linux platforms.

# 🛠️ Technology Stack

## Core Frameworks

- **Electron (v28+)**: Cross-platform desktop application framework
- **Vue3**: Front-end framework
- **TypeScript**: A type-safe superset of JavaScript
- **Flask**: Back-end framework for handling video download logic

## Front-end Technologies

- **Pinia**: State management
- **Vite**: Build tool
- **Sass/Scss**: CSS preprocessor

## Back-end Technologies

- **Node.js (v22+)**: Runtime environment
- **Axios**: HTTP client
- **FFmpeg**: Video processing (if needed)
- **Requests**: For sending HTTP requests and obtaining web content
- **BeautifulSoup**: For parsing HTML content and extracting video information
- **moviepy**: For merging downloaded video and audio files

## Development Tools

- **ESLint**: Code quality check
- **Prettier**: Code formatting
- **Volar**: Vue development tool

# 🚀 Quick Start

## Environment Requirements

- Node.js v22.x
- pnpm v8.x
- Git

## Install Dependencies

```bash
pnpm install
```

## Development Mode

```bash
pnpm dev
```

## Build the Application

```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

# ✨ Features

## Current Version (v1.0.0)

- ✅ Bilibili video download function
- ✅ Support for multiple clarity options
- ✅ Download queue management
- ✅ Cross-platform support (Windows/macOS/Linux)
- ✅ Responsive user interface

## Planned Features

- 🔲 Download history
- 🔲 Customizable download path
- 🔲 Theme switching function

# 🏗️ Project Structure

```
bilibili-downloader/
├── electron/          # Electron main process code
├── src/               # Front-end source code
│   ├── assets/        # Static resources
│   ├── components/    # Vue components
│   ├── stores/        # Pinia state management
│   ├── utils/         # Utility functions
│   └── views/         # Page components
├── build/             # Build-related configuration
├── public/            # Public resources
├── server/            # Back-end service code
│   ├── __init__.py    # Flask application initialization
│   ├── routes.py      # Route definition
│   ├── utils.py       # Utility functions
│   └── download.py    # Video download logic
└── package.json       # Project configuration
```

# 📬 Contact the Developer

If you have any questions or suggestions, feel free to contact me through the following ways:

- CSDN: [Pu_Nine_9-CSDN博客](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉


## 日本語版 (Japanese Version)
# 📌 プロジェクト概要
こんにちは、NINEです。これは私の2番目のフルスタックプロジェクトです。Bilibili Downloaderは、Bilibiliのビデオコンテンツをダウンロードするためのクロスプラットフォームデスクトップアプリケーションで、モダンなフロントエンド技術スタックを使用して開発され、Windows、macOS、Linuxの3つのプラットフォームをサポートしています。

# 🛠️ 技術スタック

## コアフレームワーク

- **Electron (v28+)**: クロスプラットフォームデスクトップアプリケーションフレームワーク
- **Vue3**: フロントエンドフレームワーク
- **TypeScript**: タイプセーフなJavaScriptのスーパーセット
- **Flask**: ビデオダウンロードロジックを処理するためのバックエンドフレームワーク

## フロントエンド技術

- **Pinia**: ステート管理
- **Vite**: ビルドツール
- **Sass/Scss**: CSSプリプロセッサ

## バックエンド技術

- **Node.js (v22+)**: ランタイム環境
- **Axios**: HTTPクライアント
- **FFmpeg**: ビデオ処理（必要に応じて）
- **Requests**: HTTPリクエストを送信してウェブコンテンツを取得するためのもの
- **BeautifulSoup**: HTMLコンテンツを解析してビデオ情報を抽出するためのもの
- **moviepy**: ダウンロードされたビデオとオーディオファイルを結合するためのもの

## 開発ツール

- **ESLint**: コード品質チェック
- **Prettier**: コードフォーマッティング
- **Volar**: Vue開発ツール

# 🚀 クイックスタート

## 環境要件

- Node.js v22.x
- pnpm v8.x
- Git

## 依存関係のインストール

```bash
pnpm install
```

## 開発モード

```bash
pnpm dev
```

## アプリケーションのビルド

```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

# ✨ 機能

## 現在のバージョン (v1.0.0)

- ✅ Bilibiliビデオのダウンロード機能
- ✅ 複数の画質オプションのサポート
- ✅ ダウンロードキューの管理
- ✅ クロスプラットフォームのサポート (Windows/macOS/Linux)
- ✅ レスポンシブユーザーインターフェース

## 計画機能

- 🔲 ダウンロード履歴
- 🔲 カスタマイズ可能なダウンロードパス
- 🔲 テーマ切り替え機能

# 🏗️ プロジェクト構造

```
bilibili-downloader/
├── electron/          # Electronメインプロセスコード
├── src/               # フロントエンドソースコード
│   ├── assets/        # 静的リソース
│   ├── components/    # Vueコンポーネント
│   ├── stores/        # Piniaステート管理
│   ├── utils/         # ユーティリティ関数
│   └── views/         # ページコンポーネント
├── build/             # ビルド関連の設定
├── public/            # 公開リソース
├── server/            # バックエンドサービスコード
│   ├── __init__.py    # Flaskアプリケーションの初期化
│   ├── routes.py      # ルート定義
│   ├── utils.py       # ユーティリティ関数
│   └── download.py    # ビデオダウンロードロジック
└── package.json       # プロジェクト設定
```

# 📬 開発者に連絡する

質問や提案があれば、以下の方法で連絡してください。

- CSDN: [Pu_Nine_9-CSDNブログ](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉


## 한국어 버전 (Korean Version)
# 📌 프로젝트 개요
안녕하세요, NINE입니다. 이 프로젝트는 Bilibili Downloader로, Bilibili의 동영상 콘텐츠를 다운로드하는 크로스 플랫폼 데스크톱 애플리케이션입니다. 현대적인 프론트엔드 기술 스택을 사용하여 개발되었으며, Windows, macOS, Linux 세 플랫폼을 지원합니다.

# 🛠️ 기술 스택

## 코어 프레임워크

- **Electron (v28+)**: 크로스 플랫폼 데스크톱 애플리케이션 프레임워크
- **Vue3**: 프론트엔드 프레임워크
- **TypeScript**: 타입 안전한 JavaScript의 슈퍼셋
- **Flask**: 비디오 다운로드 로직을 처리하는 백엔드 프레임워크

## 프론트엔드 기술

- **Pinia**: 상태 관리
- **Vite**: 빌드 도구
- **Sass/Scss**: CSS 프리프로세서

## 백엔드 기술

- **Node.js (v22+)**: 런타임 환경
- **Axios**: HTTP 클라이언트
- **FFmpeg**: 비디오 처리 (필요 시)
- **Requests**: HTTP 요청을 보내고 웹 콘텐츠를 가져옴
- **BeautifulSoup**: HTML 콘텐츠를 파싱하여 비디오 정보를 추출함
- **moviepy**: 다운로드된 비디오와 오디오 파일을 합침

## 개발 도구

- **ESLint**: 코드 품질 검사
- **Prettier**: 코드 포맷팅
- **Volar**: Vue 개발 도구

# 🚀 빠른 시작

## 환경 요구 사항

- Node.js v22.x
- pnpm v8.x
- Git

## 종속성 설치

```bash
pnpm install
```

## 개발 모드

```bash
pnpm dev
```

## 애플리케이션 빌드

```bash
# Windows
pnpm build:win

# macOS
pnpm build:mac

# Linux
pnpm build:linux
```

# ✨ 기능

## 현재 버전 (v1.0.0)

- ✅ Bilibili 비디오 다운로드 기능
- ✅ 다중 해상도 선택 지원
- ✅ 다운로드 대기열 관리
- ✅ 크로스 플랫폼 지원 (Windows/macOS/Linux)
- ✅ 반응형 사용자 인터페이스

## 계획 기능

- 🔲 다운로드 기록
- 🔲 사용자 정의 다운로드 경로
- 🔲 테마 전환 기능

# 🏗️ 프로젝트 구조

```
bilibili-downloader/
├── electron/          # Electron 메인 프로세스 코드
├── src/               # 프론트엔드 소스 코드
│   ├── assets/        # 정적 리소스
│   ├── components/    # Vue 컴포넌트
│   ├── stores/        # Pinia 상태 관리
│   ├── utils/         # 유틸리티 함수
│   └── views/         # 페이지 컴포넌트
├── build/             # 빌드 관련 설정
├── public/            # 공용 리소스
├── server/            # 백엔드 서비스 코드
│   ├── __init__.py    # Flask 애플리케이션 초기화
│   ├── routes.py      # 라우트 정의
│   ├── utils.py       # 유틸리티 함수
│   └── download.py    # 비디오 다운로드 로직
└── package.json       # 프로젝트 설정
```

# 📬 개발자에게 연락하기

문제나 제안이 있다면, 다음 방법으로 연락해 주세요.

- CSDN: [Pu_Nine_9-CSDN 블로그](https://blog.csdn.net/nineeea?spm=1000.2115.3001.5343)  
Happy Coding! 🎉
