<template>
  <div class="flex items-center justify-center h-screen">
    <ChatArea :messages="messages" />
    <MessageInput @sendMessage="handleSendMessage" />
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import ChatArea from '../components/ChatArea.vue';
import MessageInput from '../components/MessageInput.vue';

const messages = ref([]);
let websocket = null;

const handleSendMessage = (message) => {
  if (message.trim() !== '' && websocket.readyState === WebSocket.OPEN) {
    websocket.send(JSON.stringify({ message: message }));
  }
};

onMounted(() => {
  websocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/');

  websocket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    messages.value.push(data);
  };

  websocket.onopen = () => {
    console.log('WebSocket connection established');
  };

  websocket.onclose = () => {
    console.log('WebSocket connection closed');
  };

  websocket.onerror = (error) => {
    console.error('WebSocket error:', error);
  };
});

onBeforeUnmount(() => {
  if (websocket) {
    websocket.close();
  }
});
</script>