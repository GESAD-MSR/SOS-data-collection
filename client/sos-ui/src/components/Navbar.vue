<template>
  <div class="bg-gray-200 mt-5 px-3 rounded-lg flex items-center shadow-md h-16 w-1/4">
    <router-link
      to="/list"
      class="inline-block text-center w-2/5 m-auto px-2 py-2 shadow-lg bg-gray-600 text-white uppercase tracking-wider rounded-lg font-semibold"
    >Tech List</router-link>

    <router-link
      to="/add"
      class="inline-block text-center w-2/5 m-auto px-2 py-2 shadow-lg bg-gray-600 text-white uppercase tracking-wider rounded-lg font-semibold"
    >Add Tech</router-link>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({});
</script>