<script setup lang="ts">
import { toast } from "vue3-toastify";

const config = useRuntimeConfig();

const props = defineProps({
  itemKey: {
    type: String,
    required: true,
  },
});

const removing = ref(false);

const removeItem = async () => {
  try {
    removing.value = true;

    const r = await fetch(
      `${config.public.internalApi}/library/i/${props.itemKey}`,
      {
        method: "DELETE",
      }
    );

    const resp = await r.json();

    if (!r.ok) {
      throw new Error(resp.message);
    }

    toast.success("Successfully removed manga from library.");
    await navigateTo("/");
  } catch (e) {
    toast.error(String(e));
    console.error(e);
  } finally {
    removing.value = false;
  }
};
</script>

<template>
  <button
    @click="removeItem"
    :disabled="removing"
    title="Remove from Library"
    class="py-1 px-8 text-sm inline-flex uppercase items-center bg-red-400 hover:bg-red-500 duration-300 rounded-lg text-white"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      stroke-width="1.5"
      stroke="currentColor"
      class="w-5 h-5"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        d="M6 18L18 6M6 6l12 12"
      />
    </svg>

    <small v-if="removing" class="ml-2"> Removing... </small>
    <small v-else class="ml-2"> Remove </small>
  </button>
</template>
