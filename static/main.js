const { createApp } = Vue

const TaskApp = {
  data() {
    return {
      task: 'new task',
      tasks: [
        { title: 'One' },
        { title: 'Two' }
      ]
    }
  },
  delimiters: ['{', '}']

}

createApp(TaskApp).mount('#app')