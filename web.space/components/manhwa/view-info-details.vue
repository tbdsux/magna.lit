<script setup lang="ts">
import { DialogTitle } from "@headlessui/vue";
import { LinkIcon, SquaresPlusIcon } from "@heroicons/vue/20/solid";
import { genUID } from "~~/lib/uid";
import { useLibraryStore } from "~~/stores/library";
import { ScraperAPIProps } from "~~/typings/api";
import { LibraryMangaProps } from "~~/typings/library";
import { ManhwaProps } from "~~/typings/manhwa";

const config = useRuntimeConfig();

const store = useLibraryStore();

const props = defineProps({
  slug: {
    type: String,
    required: true,
  },
  source: {
    type: String,
    required: true,
  },
});

const params = new URLSearchParams({
  manhwa: props.slug,
  source: props.source,
});
const { pending, data } = useLazyFetch<ScraperAPIProps<ManhwaProps>>(
  `${config.public.apiPybs4}/manhwa?${params.toString()}`
);

const emit = defineEmits(["closeModal"]);

const adding = ref(false);

const addManhwa = async () => {
  if (!data.value?.data) return;

  const { chapters, ...manga } = data.value.data;

  adding.value = true;

  const item: Omit<LibraryMangaProps, "key"> = {
    manga: manga,
    uid: genUID(data.value.data.title, props.source),
    ...props,
    date_added: new Date().getTime(),
  };

  const r = await fetch(`${config.public.internalApi}/library`, {
    method: "PUT",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify(item),
  });

  const d = await r.json();
  if (!r.ok) {
    // return
  }

  refreshNuxtData("library");

  emit("closeModal");
};
</script>

<template>
  <span v-if="pending"> Loading... </span>

  <div v-else>
    <div class="flex items-start justify-between">
      <div class="h-72 w-auto">
        <img
          referrerpolicy="no-referrer"
          :src="data?.data?.image"
          :alt="data?.data?.title"
          class="w-full h-full object-cover rounded-lg"
        />
      </div>

      <div class="w-3/4">
        <DialogTitle
          as="h3"
          class="text-lg font-medium leading-6 text-gray-800"
        >
          {{ data?.data?.title }}
        </DialogTitle>

        <ul class="flex items-center">
          <li v-for="item in data?.data?.authors" class="m-0.5 text-gray-500">
            <small> @{{ item }} </small>
          </li>
        </ul>

        <div class="my-4">
          <p class="text-sm text-gray-500">
            {{ data?.data?.summary }}
          </p>
        </div>

        <ul class="flex items-center">
          <li
            class="py-0.5 m-0.5 px-2 bg-gray-300 text-gray-700 rounded-lg"
            v-for="item in data?.data?.genres"
          >
            <small>
              {{ item }}
            </small>
          </li>
        </ul>

        <div class="mt-6 inline-flex items-center">
          <button
            v-if="
              store.isUIDExists(genUID(data?.data?.title ?? '', props.source))
            "
            :disabled="true"
            title="Add Manhwa to Library"
            class="m-1 inline-flex items-center py-2 px-6 uppercase bg-blue-500 hover:bg-blue-600 text-white duration-300 rounded-lg"
          >
            <SquaresPlusIcon aria-hidden="true" class="h-5 w-5" />

            <small class="ml-2"> Manga Exists in Library </small>
          </button>

          <button
            v-else
            :disabled="adding"
            @click="addManhwa"
            title="Add Manhwa to Library"
            class="m-1 inline-flex items-center py-2 px-6 uppercase bg-blue-500 hover:bg-blue-600 text-white duration-300 rounded-lg"
          >
            <SquaresPlusIcon aria-hidden="true" class="h-5 w-5" />

            <small v-if="adding" class="ml-2"> Adding... </small>
            <small v-else class="ml-2"> Add to Library </small>
          </button>

          <a
            :href="data?.data?.url"
            target="_blank"
            rel="noreferrer"
            title="Visit Manhwa"
            class="m-1 inline-flex items-center py-2 px-6 uppercase bg-gray-500 hover:bg-gray-600 text-white duration-300 rounded-lg"
          >
            <LinkIcon aria-hidden="true" class="h-5 w-5" />

            <small class="ml-2"> Visit </small>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
