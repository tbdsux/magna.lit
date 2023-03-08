<script setup lang="ts">
import {
  DialogPanel,
  DialogTitle,
  Listbox,
  ListboxButton,
  ListboxOption,
  ListboxOptions,
} from "@headlessui/vue";
import {
  CheckIcon,
  ChevronUpDownIcon,
  MagnifyingGlassIcon,
} from "@heroicons/vue/20/solid";
import { watch } from "vue";
import { allSources } from "~~/lib/data";
import { ScraperAPIProps } from "~~/typings/api";
import { SearchResultsProps } from "~~/typings/manhwa";

const config = useRuntimeConfig();

const inputQuery = ref("");

const selectedSource = ref<typeof allSources[0]>(allSources[0]);

const open = ref(false);
const openModal = () => (open.value = true);
const closeModal = () => (open.value = false);

const searching = ref(false);
const searchFailed = ref(false);
const searchData = ref<SearchResultsProps[]>([]);

const searchManhwas = async () => {
  if (inputQuery.value.trim() === "" || selectedSource.value.name === "None")
    return;

  const params = new URLSearchParams({
    q: inputQuery.value,
    source: selectedSource.value.source,
  });

  searching.value = true;
  searchFailed.value = false;

  const r = await fetch(
    `${config.public.apiPybs4}/search?${params.toString()}`
  );

  const data: ScraperAPIProps<SearchResultsProps[]> = await r.json();
  searching.value = false;

  if (!r.ok) {
    console.error(data);
    searchFailed.value = true;

    return;
  }

  searchData.value = data.data ?? [];
  searchFailed.value = false;
};

watch(selectedSource, (newsrc, oldsrc) => {
  if (newsrc.name === oldsrc.name) return;

  searchData.value = [];
});
</script>

<template>
  <div>
    <button
      @click="openModal"
      class="inline-flex items-center bg-blue-400 hover:bg-blue-500 text-white duration-300 py-2 px-8 rounded-xl"
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
          d="M12 10.5v6m3-3H9m4.06-7.19l-2.12-2.12a1.5 1.5 0 00-1.061-.44H4.5A2.25 2.25 0 002.25 6v12a2.25 2.25 0 002.25 2.25h15A2.25 2.25 0 0021.75 18V9a2.25 2.25 0 00-2.25-2.25h-5.379a1.5 1.5 0 01-1.06-.44z"
        />
      </svg>

      <small class="ml-2">Add Manhwa</small>
    </button>
  </div>

  <Modal :open="open" @closeModal="closeModal">
    <DialogPanel
      class="w-full max-w-5xl min-h-screen transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
    >
      <div class="flex items-center justify-between">
        <div>
          <DialogTitle
            as="h3"
            class="text-lg font-medium leading-6 text-gray-900"
          >
            Add Manhwa
          </DialogTitle>
          <div class="mt-2">
            <p class="text-sm text-gray-500">
              Add a manhwa to your library from various sources
            </p>
          </div>
        </div>

        <div class="">
          <label for="sources" class="text-xs">Sources</label>

          <Listbox v-model="selectedSource">
            <div class="relative mt-1">
              <ListboxButton
                class="relative w-72 cursor-default rounded-lg bg-white py-2 pl-3 pr-10 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 text-[0.825rem]"
              >
                <span class="block truncate">{{ selectedSource.name }}</span>
                <span
                  class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2"
                >
                  <ChevronUpDownIcon
                    class="h-5 w-5 text-gray-400"
                    aria-hidden="true"
                  />
                </span>
              </ListboxButton>

              <transition
                leave-active-class="transition duration-100 ease-in"
                leave-from-class="opacity-100"
                leave-to-class="opacity-0"
              >
                <ListboxOptions
                  class="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none text-[0.825rem]"
                >
                  <ListboxOption
                    v-slot="{ active, selected }"
                    v-for="src in allSources"
                    :key="src.name"
                    :value="src"
                    as="template"
                  >
                    <li
                      :class="[
                        active ? 'bg-blue-100 text-blue-900' : 'text-gray-900',
                        'relative cursor-default select-none py-2 pl-10 pr-4',
                      ]"
                    >
                      <span
                        :class="[
                          selected ? 'font-medium' : 'font-normal',
                          'block truncate',
                        ]"
                        >{{ src.name }}</span
                      >
                      <span
                        v-if="selected"
                        class="absolute inset-y-0 left-0 flex items-center pl-3 text-blue-600"
                      >
                        <CheckIcon class="h-5 w-5" aria-hidden="true" />
                      </span>
                    </li>
                  </ListboxOption>
                </ListboxOptions>
              </transition>
            </div>
          </Listbox>
        </div>
      </div>

      <div class="my-4">
        <div class="flex flex-col">
          <label for="query" class="text-[0.825rem] text-gray-700"
            >Search Query</label
          >
          <div class="flex items-stretch">
            <input
              v-model="inputQuery"
              type="text"
              placeholder="Search for Manga, Manhwa or Manhua..."
              class="py-2 px-4 rounded-lg border text-[0.825rem] w-full"
            />

            <button
              @click="searchManhwas"
              :disabled="searching"
              class="inline-flex items-center py-2 px-6 rounded-lg ml-2 bg-blue-400 hover:bg-blue-500 text-white duration-300"
            >
              <MagnifyingGlassIcon aria-hidden="true" class="h-5 w-5" />

              <small class="ml-2">
                <span v-if="searching">Searching...</span>
                <span v-else>Search</span>
              </small>
            </button>
          </div>
        </div>

        <div class="mt-6">
          <div v-if="searching">
            <small>Searching...</small>
          </div>

          <div v-else class="grid grid-cols-4 gap-6">
            <ManhwaViewInfo
              v-for="result in searchData"
              :title="result.title"
              :image="result.image"
              :url="result.url"
              :slug="result.slug"
              :source="selectedSource.source"
            />
          </div>
        </div>
      </div>

      <div class="mt-4">
        <button
          type="button"
          class="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
          @click="closeModal"
        >
          Got it, thanks!
        </button>
      </div>
    </DialogPanel>
  </Modal>
</template>
