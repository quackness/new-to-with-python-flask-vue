const { createApp } = Vue

const TaskApp = {
  data() {
    return {
      task: 'new task'
    }
  },
  delimiters: ['{', '}']

}

createApp(TaskApp).mount('#app')