<script setup lang="ts">
import { DialogPanel } from "@headlessui/vue";
import { CheckCircleIcon } from "@heroicons/vue/20/solid";
import { genUID } from "~~/lib/uid";
import { useLibraryStore } from "~~/stores/library";

const store = useLibraryStore();

const props = defineProps({
  image: {
    type: String,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
  url: {
    type: String,
    required: true,
  },
  slug: {
    type: String,
    required: true,
  },

  source: {
    type: String,
    required: true,
  },
});

const open = ref(false);
const openModal = () => (open.value = true);
const closeModal = () => (open.value = false);
</script>

<template>
  <div class="h-72 w-auto rounded-lg relative group">
    <span
      v-if="store.isUIDExists(genUID(props.title, props.source))"
      class="absolute -top-1 -right-1 text-green-500 z-[999]"
    >
      <CheckCircleIcon aria-hidden="true" class="h-4 w-4" />
    </span>
    <div
      @click="openModal"
      class="cursor-pointer absolute w-full h-full group-hover:flex hidden bg-black/50 items-center justify-center rounded-lg p-2"
    >
      <div class="text-center">
        <span class="text-white">
          {{ props.title }}
        </span>
      </div>
    </div>

    <img
      referrerpolicy="no-referrer"
      :src="props.image"
      :alt="props.title"
      class="w-full h-full object-cover rounded-lg"
    />
  </div>

  <Modal :open="open" @closeModal="closeModal">
    <DialogPanel
      class="w-full max-w-4xl min-h-[14rem] transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
    >
      <ManhwaViewInfoDetails
        @closeModal="closeModal"
        :slug="props.slug"
        :source="props.source"
      />
    </DialogPanel>
  </Modal>
</template>
