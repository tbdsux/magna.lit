import { defineStore } from "pinia";
import { InternalAPIProps, ScraperAPIProps } from "~~/typings/api";
import { LibraryMangaProps } from "~~/typings/library";
import { ManhwaChapterProps, ManhwaProps } from "~~/typings/manhwa";

interface LibraryStoreProps {
  items: LibraryMangaProps[];
  current: LibraryMangaProps | null;
  currentChapters: ManhwaChapterProps[] | null;
}

const useLibraryStore = defineStore("library", {
  state: () => {
    return <LibraryStoreProps>{
      items: [] as LibraryMangaProps[],
      current: null,
      currentChapters: null,
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
      const r = await $fetch<InternalAPIProps<LibraryMangaProps[]>>(
        `/internal-api/library`,
        {
          method: "GET",
          parseResponse: JSON.parse,
        }
      );

      this.items = r.data ?? [];

      return this.items;
    },

    async fetchLibItem(key: string) {
      // reset
      this.current = null;
      this.currentChapters = null;

      // fetch key
      const k = await $fetch<InternalAPIProps<LibraryMangaProps | null>>(
        `/internal-api/library/i/${key}`,
        {
          method: "GET",
          parseResponse: JSON.parse,
        }
      );

      if (!k.data) {
        return null;
      }

      this.current = k.data;

      const params = new URLSearchParams({
        manhwa: k.data.slug,
        source: k.data.source,
      });

      const r = await $fetch<ScraperAPIProps<ManhwaProps>>(
        `/scrapers-pybs4/manhwa?${params.toString()}`,
        {
          method: "GET",
          parseResponse: JSON.parse,
        }
      );

      this.currentChapters = r.data?.chapters ?? null;

      return {
        ...this.current,
        chapters: this.currentChapters,
      };
    },
  },
});

export { useLibraryStore };
