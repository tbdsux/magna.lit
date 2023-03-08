import { defineStore } from "pinia";
import { InternalAPIProps } from "~~/typings/api";
import { LibraryMangaProps } from "~~/typings/library";

const useLibraryStore = defineStore("library", {
  state: () => {
    return {
      items: [] as LibraryMangaProps[],
    };
  },

  getters: {
    isUIDExists: (state) => {
      return (uid: string) =>
        state.items.filter((i) => i.uid === uid).length > 0;
    },
  },

  actions: {
    async fetchLibraryItems() {
      const config = useRuntimeConfig();

      const r = await $fetch<InternalAPIProps<LibraryMangaProps[]>>(
        `${config.public.internalApi}/library`,
        {
          method: "GET",
          parseResponse: JSON.parse,
        }
      );

      this.items = r.data ?? [];

      return this.items;
    },
  },
});

export { useLibraryStore };
