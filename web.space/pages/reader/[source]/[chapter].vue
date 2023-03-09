<script setup lang="ts">
import { decodeChapter } from "~~/lib/hash";
import { joinParams } from "~~/lib/utils";
import { ScraperAPIProps } from "~~/typings/api";
import { ChapterProps } from "~~/typings/manhwa";

const route = useRoute();
const config = useRuntimeConfig();

const { source, chapter } = route.params;

const params = new URLSearchParams({
  chapter: decodeChapter(joinParams(chapter)),
  source: joinParams(source),
});

const { data } = await useFetch<ScraperAPIProps<ChapterProps>>(
  `${config.public.apiPybs4}/chapter-manhwa?${params.toString()}`
);

useHead({
  title: `${data.value?.data?.title}`,
});
</script>

<template>
  <div>
    <div v-if="data != null" class="">
      <PageHeader>
        <div class="inline-flex">
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
              d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"
            />
          </svg>

          <h4 class="text-sm font-bold ml-2">{{ data.data?.title }}</h4>
        </div>
      </PageHeader>

      <hr class="my-6" />

      <ul class="w-1/2 mx-auto py-6">
        <li v-for="item in data.data?.images" class="w-full h-full">
          <img
            referrerpolicy="no-referrer"
            :src="item.replace('http://', 'https://')"
            :alt="item.replace('http://', 'https://')"
            class="w-full h-full object-cover rounded-lg bg-gray-100"
          />
        </li>
      </ul>
    </div>
  </div>
</template>
