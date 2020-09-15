<template>
  <div class="w-2/5 max-w-6xl h-auto flex flex-col mb-5">
    <div>
      <form action="GET">
        <label for="tag filter" class="mr-2">Filter by tech name:</label>
        <input type="text" class="h-8 mb-3 border border-gray-300 focus:border-gray-500 rounded" />
        <button
          v-on:click="onFilter"
          class="bg-gray-600 hover:bg-gray-500 ml-3 rounded-lg shadow-md text-white p-1 uppercase tracking-wide text-sm font-bold"
        >filter</button>
      </form>
    </div>
    <hr class="border border-gray-500" />
    <div class="w-full mt-5 flex flex-col items-center">
      <details-card />
      <details-card />
      <details-card />
      <details-card />
      <details-card />
      <details-card />
      <details-card />
      <details-card />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import DetailsCard from "@/components/DetailsCard.vue";

export default Vue.extend({
  components: {
    DetailsCard,
  },

  methods: {
    onFilter(event: any) {
      event.preventDefault();
    },
  },
});
</script>