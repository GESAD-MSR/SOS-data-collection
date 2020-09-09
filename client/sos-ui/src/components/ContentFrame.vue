<template>
  <div class="bg-white w-1/2 p-12">
    <TechnologyForm />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TechnologyForm from "@/components/TechnologyForm.vue";

export default Vue.extend({
  data: function () {
    return {
      activeContent: "",
    };
  },
  components: { TechnologyForm },
});
</script>