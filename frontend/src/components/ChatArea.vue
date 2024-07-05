<template>
  <div class="p-4 space-y-4 overflow-y-auto max-h-96 w-5/6 h-5/6">
    <div v-for="(message, index) in messages" :key="index" class="pb-2">
      <p class="flex items-center"><strong class="mr-2">{{ message.user.username }}</strong> {{ message.message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ChatArea',
  props: {
    messages: {
      type: Array,
      required: true,
    },
  },
  updated() {
    this.$nextTick(() => {
      this.scrollToBottom();
    });
  },
  methods: {
    scrollToBottom() {
      this.$el.scrollTop = this.$el.scrollHeight;
    },
  },
};
</script>

<style scoped>
::-webkit-scrollbar {
  width: 0px;
}
</style>