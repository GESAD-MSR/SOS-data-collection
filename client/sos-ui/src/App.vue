<template>
  <div id="app">
    <header>
      <navbar />
    </header>
    <div class="bg-gray-800 w-full h-screen p-32">
      <router-view />
    </div>
    <footer></footer>
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