<template>
  <!-- <div class="tech-form"> -->
  <form class="w-full max-w-lg">
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
        <label
          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
          for="grid-first-name"
        >First Name</label>
        <input
          class="appearance-none block w-full bg-white-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none"
          id="grid-first-name"
          type="text"
          placeholder="Jane"
        />
      </div>
    </div>
    <div class="flex flex-wrap -mx-3 mb-6">
      <div class="w-full px-3">
        <label
          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
          for="grid-password"
        >Password</label>
        <input
          class="appearance-none block w-full bg-white-200 text-gray-700 border rounded py-3 px-4 mb-3 leading-tight focus:outline-none"
          id="grid-first-name"
          type="text"
          placeholder="Jane"
        />
      </div>
    </div>
  </form>
  <!-- </div> -->
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({});
</script>