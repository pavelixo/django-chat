<template>
  <div class="fixed bottom-2 left-1/2 transform  -translate-y-1/2 -translate-x-1/2 w-11/12 max-w-3xl p-2 bg-transparent flex items-center gap-2">
    <input v-model="newMessage" type="text" @keyup.enter="sendMessage" placeholder="Type your message" class="p-2 border drop-shadow-2xl border-gray-300 rounded-full flex-1" />
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['sendMessage']);
const newMessage = ref('');

const sendMessage = () => {
  emit('sendMessage', newMessage.value);
  newMessage.value = '';
};
</script>