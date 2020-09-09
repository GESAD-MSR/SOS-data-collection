<template>
  <div class="flex justify-center flex-col">
    <div class="items-start w-1/2">
      <tab-bar />
    </div>
    <content-frame />
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import TabBar from "@/components/TabBar.vue";
import ContentFrame from "@/components/ContentFrame.vue";

export default Vue.extend({
  name: "Home",
  components: { TabBar, ContentFrame },
});
</script>
