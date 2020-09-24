<template>
  <div class="w-4/5 max-w-full mb-4 shadow-lg flex flex-col items-start rounded p-8 bg-white">
    <div class="flex">
      <label class="text-lg block uppercase tracking-wide text-gray-700 font-bold mr-3">Tech:</label>
      <p>{{name}}</p>
    </div>
    <div class="flex mt-2">
      <div class="grid grid-cols-4 items-center gap-3 border-t-2 border-gray-500">
        <label
          class="mt-2 text-lg col-span-4 block uppercase tracking-wide text-gray-700 font-bold mr-3"
        >Tags:</label>
        <div v-for="(tag, index) in tags" :key="index" class="col-span-1">{{tag}}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  props: ["name", "tags"],
});
</script>