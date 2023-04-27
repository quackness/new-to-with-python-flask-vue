const { createApp } = Vue

const TaskApp = {
  data() {
    return {
      task: {

      },
      tasks: []
    }
  },
  async created() {
    await this.getTasks()
  },
  methods: {

    async sendRequest(url, method, data) {
      const myHeaders = new Headers({
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      })
      const response = await fetch(url, {
        method: method,
        headers: myHeaders,
        body: data
      })
      return response
    },

    async getTasks() {
      const response = await this.sendRequest(window.location, 'get')
      this.tasks = await response.json()
    },
    async createTask() {
      await this.getTasks()
      await this.sendRequest(window.location + 'create', 'post', JSON.stringify(this.task))
      await this.getTasks()
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')