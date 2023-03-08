<script setup lang="ts">
import { joinParams } from "~~/lib/utils";
import { InternalAPIProps } from "~~/typings/api";
import { LibraryMangaProps } from "~~/typings/library";

const route = useRoute();
const config = useRuntimeConfig();

const { key } = route.params;
const { data } = await useFetch<InternalAPIProps<LibraryMangaProps | null>>(
  `${config.public.internalApi}/library/i/${key}`,
  {
    key: `library-${joinParams(key)}`,
    method: "GET",
    headers: {
      "content-type": "application/json",
    },
  }
);

// if (data.value?.data == null) {
//   throw createError({
//     statusCode: 404,
//     message: "Manhwa / manga key does not exist in your library.",
//   });
// }

useHead({ title: `${data.value?.data?.manga.title}` });
</script>

<template>
  <div class="p-12">
    <div class="flex items-start">
      <div class="h-72 w-auto">
        <img
          referrerpolicy="no-referrer"
          :src="data?.data?.manga.image"
          :alt="data?.data?.manga.title"
          class="w-full h-full object-cover rounded-lg"
        />
      </div>

      <div class="w-3/4 ml-6">
        <h3 class="text-lg font-medium leading-6 text-gray-800">
          {{ data?.data?.manga.title }}
        </h3>

        <ul class="flex items-center">
          <li
            v-for="item in data?.data?.manga.authors"
            class="m-0.5 text-gray-500"
          >
            <small> @{{ item }} </small>
          </li>
        </ul>

        <div class="my-4">
          <p class="text-sm text-gray-500">
            {{ data?.data?.manga.summary }}
          </p>
        </div>

        <ul class="flex items-center">
          <li
            class="py-0.5 m-0.5 px-2 bg-gray-300 text-gray-700 rounded-lg"
            v-for="item in data?.data?.manga.genres"
          >
            <small>
              {{ item }}
            </small>
          </li>
        </ul>
      </div>
    </div>

    <hr class="my-12" />

    <LibraryChapters
      :slug="data?.data?.slug ?? ''"
      :source="data?.data?.source ?? ''"
      :item-key="Array.isArray(key) ? key.join() : key"
    />
  </div>
</template>
