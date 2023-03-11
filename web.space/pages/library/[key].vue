<script setup lang="ts">
import { LinkIcon } from "@heroicons/vue/20/solid";
import { encodeChapter } from "~~/lib/hash";
import { joinParams } from "~~/lib/utils";
import { useLibraryStore } from "~~/stores/library";

const route = useRoute();
const store = useLibraryStore();

const { key } = route.params;
const { data, pending, error } = useLazyAsyncData(
  "item",
  async () => await store.fetchLibItem(joinParams(key))
);

// if (data.value?.data == null) {
//   throw createError({
//     statusCode: 404,
//     message: "Manhwa / manga key does not exist in your library.",
//   });
// }

useHead({ title: "Loading... | magna.lit" });

watch(data, (newData) => {
  if (newData != null) {
    useHead({ title: `${newData.manga.title} | magna.lit` });
  }
});
</script>

<template>
  <div class="p-12">
    <div v-if="pending">
      <div class="flex flex-col md:flex-row items-stretch">
        <div class="h-72 w-48 bg-gray-200 animate-pulse rounded-lg"></div>

        <div
          class="w-full h-96 mt-4 md:mt-0 md:ml-6 bg-gray-200 rounded-lg animate-pulse"
        ></div>
      </div>

      <hr class="my-12" />

      <ul>
        <li
          v-for="i in Array(5).keys()"
          class="bg-gray-200 animate-pulse rounded-lg h-10 my-1"
        ></li>
      </ul>
    </div>

    <div v-else>
      <div class="flex flex-col md:flex-row items-start justify-center">
        <div class="h-72 w-auto md:w-64">
          <img
            referrerpolicy="no-referrer"
            :src="data?.manga.image"
            :alt="data?.manga.title"
            class="w-full h-full object-cover rounded-lg"
          />
        </div>

        <div class="w-full md:ml-6 mt-4 md:mt-0">
          <h3 class="text-lg font-medium leading-6 text-gray-800">
            {{ data?.manga.title }}
          </h3>

          <ul class="flex flex-wrap items-center">
            <li v-for="item in data?.manga.authors" class="m-0.5 text-gray-500">
              <small> @{{ item }} </small>
            </li>
          </ul>

          <div class="my-4">
            <p class="text-sm text-gray-500">
              {{ data?.manga.summary }}
            </p>
          </div>

          <ul class="flex flex-wrap items-center">
            <li
              class="py-0.5 m-0.5 px-2 bg-gray-300 text-gray-700 rounded-lg"
              v-for="item in data?.manga.genres"
            >
              <small>
                {{ item }}
              </small>
            </li>
          </ul>

          <div class="mt-4">
            <a
              :href="data?.manga.url"
              target="_blank"
              rel="noreferrer"
              title="Visit Original Content"
              class="m-1 inline-flex items-center py-1 px-8 uppercase bg-gray-500 hover:bg-gray-600 text-white duration-300 rounded-lg"
            >
              <LinkIcon aria-hidden="true" class="h-5 w-5" />

              <small class="ml-2"> Visit </small>
            </a>
          </div>
        </div>
      </div>

      <hr class="my-12" />

      <ul class="">
        <li v-for="item in data?.chapters">
          <NuxtLink
            :to="`/reader/${data?.source}/${encodeChapter(item.url)}`"
            class="flex items-center justify-between py-2 text-sm border my-1 px-5 rounded-xl"
          >
            {{ item.title }}

            <small>{{ item.release }}</small>
          </NuxtLink>
        </li>
      </ul>
    </div>
  </div>
</template>
