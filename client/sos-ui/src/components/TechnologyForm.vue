<template>
  <div class="w-full flex flex-col items-center max-w-6xl">
    <div class="w-1/2 flex flex-col items-center border-2 border-gray-500 p-8">
      <div class="w-full px-3 mb-6 md:mb-0">
        <label
          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
          for="grid-first-name"
        >Tech Name</label>
        <input
          class="appearance-none block w-full bg-white-200 text-gray-700 border border-gray-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:border-gray-500"
          type="text"
          placeholder="Docker"
        />
      </div>
      <div class="w-full px-3 mb-6 md:mb-0">
        <label
          class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
          for="grid-first-name"
        >SO Tags</label>
        <input
          class="appearance-none block w-full h-32 bg-white-200 text-gray-700 border border-gray-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:border-gray-500"
          type="text"
          placeholder="docker-compose"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
export default Vue.extend({
  data: function () {
    return {
      tagList: [],
    };
  },

  methods: {
    addTag: function () {
      return;
    },

    clearTags: function () {
      this.tagList = [];
    },
  },
});
</script>