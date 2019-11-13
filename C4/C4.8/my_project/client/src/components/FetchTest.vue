<template>
  <div>
    <h1>Todos</h1>
    <table>
        <thead>
        <tr>
            <th>Uid</th>
            <th>Описание</th>
            <th>Выполнена?</th>
        </tr>
        </thead>
        <tbody>
          <tr v-for="(todo, index) in todos" :key="index">
            <td>{{ todo.uid }}</td>
            <td>{{ todo.description }}</td>
            <td>
              <span v-if="todo.is_completed">Выполнено</span>
              <span v-else>Не выполнено</span>
            </td>
          </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'http://10.0.0.10:5000/api/tasks/';

export default {
  name: 'Fetch',
  data() {
    return {
      todos: [],
    };
  },
  methods: {
    getTodos() {
      axios.get(dataURL)
        .then((response) => {
          this.todos = response.data.tasks;
        });
    },
  },
  created() {
    this.getTodos();
  },
};
</script>
