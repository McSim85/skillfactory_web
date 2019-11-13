<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

const dataURL = 'http://localhost:5000/api/tasks/';

export default {
  name: 'Fetch',
  data() {
    return {
      msg: 'Before request',
    };
  },
  methods: {
    getMesasge() {
      axios.get(dataURL)
        .then((response) => {
          console.table(response.data);
        });
    },
  },
  created() {
    this.getMesasge();
  },
};
</script>
