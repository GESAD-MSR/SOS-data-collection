<template>
  <div class="w-2/5 flex flex-col items-center max-w-6xl">
    <div class="w-2/3 flex flex-col items-center border-2 rounded border-gray-500 p-8">
      <form action="POST">
        <div class="w-full px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="tech-name"
          >Tech Name</label>
          <input
            v-model="techName"
            class="appearance-none block w-full bg-white-200 text-gray-700 border border-gray-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:border-gray-500"
            type="text"
            placeholder="Docker"
          />
        </div>
        <div class="w-full px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
            for="so-tag"
          >SO Tags</label>
          <textarea
            v-model="tags"
            class="appearance-none block w-full h-32 bg-white-200 text-gray-700 border border-gray-300 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:border-gray-500"
            cols="30"
            rows="10"
            placeholder="docker-compose"
          />
        </div>
        <div class="w-full px-3 mt-2">
          <button
            type="submit"
            class="bg-green-500 hover:bg-green-600 rounded-lg shadow-md h-10 w-1/4 text-white uppercase tracking-wide text-sm font-bold"
            v-on:click="onSubmit"
          >Save</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";

export default Vue.extend({
  data() {
    return {
      techName: "",
      tags: "",
    };
  },

  methods: {
    onSubmit(event: any) {
      event.preventDefault();

      const tagsList: Array<string> = this.tags
        .split(",")
        .map((item: string) => {
          const cutpoint: number =
            item.indexOf("*") != -1 ? item.indexOf("*") : item.indexOf("(");

          return cutpoint == -1 ? item.trim() : item.slice(0, cutpoint).trim();
        });

      const formData = {
        name: this.techName,
        tags: tagsList,
      };

      console.log(tagsList);
      const resp = axios
        .post("http://127.0.0.1:5000/tech/save", formData)
        .then((res) => console.log(res))
        .catch((error) => console.log(error));
    },

    clearTags: function () {
      this.tags = "";
    },
  },
});
</script>