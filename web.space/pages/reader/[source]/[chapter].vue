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
      <div class="text-[0.825rem] font-bold py-2 px-6">
        <h4>{{ data.data?.title }}</h4>
      </div>

      <hr class="my-6" />

      <ul class="w-1/2 mx-auto py-6">
        <li v-for="item in data.data?.images" class="w-full h-full">
          <img
            referrerpolicy="no-referrer"
            :src="item"
            :alt="item"
            class="w-full h-full object-cover rounded-lg"
          />
        </li>
      </ul>
    </div>
  </div>
</template>
