<script setup lang="ts">
import { encodeChapter } from "~~/lib/hash";
import { ScraperAPIProps } from "~~/typings/api";
import { ManhwaProps } from "~~/typings/manhwa";

const config = useRuntimeConfig();

const props = defineProps({
  slug: {
    type: String,
    required: true,
  },
  source: {
    type: String,
    required: true,
  },
  itemKey: {
    type: String,
    required: true,
  },
});

const params = new URLSearchParams({
  manhwa: props.slug,
  source: props.source,
});
const { pending, data, error } = useLazyFetch<ScraperAPIProps<ManhwaProps>>(
  `${config.public.apiPybs4}/manhwa?${params.toString()}`
);

if (error.value) {
  throw createError(error.value.message);
}
</script>

<template>
  <div>
    <div v-if="data">
      <ul class="">
        <li v-for="item in data?.data?.chapters">
          <NuxtLink
            :to="`/reader/${props.source}/${encodeChapter(item.url)}`"
            class="flex items-center justify-between py-2 text-sm border my-1 px-5 rounded-xl"
          >
            {{ item.title }}

            <small>{{ item.release }}</small>
          </NuxtLink>
        </li>
      </ul>
    </div>

    <div v-else>
      <small>Loading chapters...</small>
    </div>
  </div>
</template>
