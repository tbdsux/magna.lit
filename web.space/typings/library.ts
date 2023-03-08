import { ManhwaProps } from "./manhwa";

export interface LibraryMangaProps {
  manga: Omit<ManhwaProps, "chapters">;
  uid: string;
  date_added: number;
  slug: string;
  source: string;
  key: string;
}
