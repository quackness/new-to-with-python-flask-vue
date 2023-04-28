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
        //info on what I am sending 
        'Content-Type': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
      })
      //fetch is converts the input body into a json object/json body and sends it to a server
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
      //json() turns  a string into a json object
    },
    async createTask() {
      await this.getTasks()
      await this.sendRequest(window.location + 'create', 'post', JSON.stringify(this.task))
      await this.getTasks()
      this.task.title = ""
    },
    async deleteTask(task) {
      await this.sendRequest(window.location + 'delete', 'post', JSON.stringify(task))
      await this.getTasks()
    },
    async completeTask(task) {
      await this.sendRequest(window.location + 'complete', 'post', JSON.stringify(task))
      await this.getTasks()
    }
  },
  delimiters: ['{', '}']
}

createApp(TaskApp).mount('#app')