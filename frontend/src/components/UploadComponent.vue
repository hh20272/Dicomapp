<template>
    <div>
      <input type="file" @change="onFileSelected" />
      <div v-if="response">{{ response }}</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        response: null,
      };
    },
    methods: {
      async onFileSelected(event) {
        try {
          const file = event.target.files[0];
          if (!file) return;
          
          const formData = new FormData();
          formData.append('file', file);
  
          // Replace with your FastAPI server's URL
          const url = 'http://localhost:8000/upload/';
  
          const response = await this.$http.post(url, formData);
          this.response = response.data;
        } catch (error) {
          this.response = 'Error uploading file!';
          console.error(error);
        }
      },
    },
  };
  </script>
  