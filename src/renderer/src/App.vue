<template>
  <div class="container">
    <h1>B站视频下载器</h1>
    <input v-model="url" placeholder="输入B站视频链接">
    <input v-model="customName" placeholder="自定义文件名（可选）">
    <button @click="handleDownload" :disabled="loading">
      {{ loading ? '下载中...' : '下载视频' }}
    </button>
    <p :class="messageClass">{{ message }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';

// 确保在 mainWorld 中暴露了 electronAPI
declare global {
  interface Window {
    electronAPI: {
      downloadVideo: (data: { url: string; customName?: string }) => Promise<any>;
    };
  }
}

const url = ref('');
const customName = ref('');
const message = ref('');
const loading = ref(false);

const messageClass = computed(() => ({
  'message': true,
  'error': message.value.includes('错误'),
}));

const handleDownload = async () => {
  if (!url.value) {
    message.value = '错误：请输入视频URL';
    return;
  }

  loading.value = true;
  try {
    const result = await window.electronAPI.downloadVideo({
      url: url.value,
      customName: customName.value,
    });
    message.value = result.message || '下载成功';
  } catch (err: any) { // 确保 err 类型为 any 或具体的错误类型
    message.value = `错误：${err.message}`;
  } finally {
    loading.value = false;
  }
};
</script>

<style>
.container {
  padding: 20px;
  max-width: 600px;
  margin: 0 auto;
}
.message {
  color: green;
}
.message.error {
  color: red;
}
</style>
