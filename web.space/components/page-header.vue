<script setup lang="ts">
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <div
    class="py-6 w-11/12 mx-auto text-sm font-medium tracking-wide text-gray-700"
  >
    <h3 class="">{{ props.title }}</h3>
  </div>

  <hr />
</template>
