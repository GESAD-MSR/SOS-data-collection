<template>
  <div id="app">
    <div class="bg-gray-800 flex flex-col items-center w-screen h-screen">
      <navbar />
      <router-view class="bg-gray-200 mt-5 w-full p-12 rounded shadow-md" />
    </div>
    <!-- <footer></footer> -->
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import Navbar from "@/components/Navbar.vue";

export default Vue.extend({
  components: {
    Navbar,
  },
});
</script>