<script setup lang="ts">
import { useLibraryStore } from "~~/stores/library";

const store = useLibraryStore();

const { data, pending } = useLazyAsyncData(
  "library",
  async () => await store.fetchLibraryItems(),
  {
    server: false,
  }
);
</script>

<template>
  <div class="p-8">
    <div v-if="!pending">
      <div class="grid grid-cols-5 gap-8">
        <NuxtLink
          v-for="item in data"
          :to="`/library/${item.key}`"
          class="h-72 w-auto rounded-lg relative group"
        >
          <div
            class="absolute bottom-0 inset-x-0 px-3 py-2 leading-none bg-black/70 text-center rounded-b-lg"
          >
            <span class="text-white text-[0.825rem]">
              {{ item.manga.title }}
            </span>
          </div>

          <img
            referrerpolicy="no-referrer"
            :src="item.manga.image"
            :alt="item.manga.title"
            class="w-full h-full object-cover rounded-lg"
          />
        </NuxtLink>
      </div>
    </div>

    <div v-else>
      <p>Fetching...</p>
    </div>
  </div>
</template>
