export interface ManhwaProps {
  title: string;
  image: string;
  authors: string[];
  genres: string[];
  summary: string;
  url: string;
}

export interface LibraryMangaProps {
  manga: ManhwaProps;
  uid: string;
  date_added: number;
  slug: string;
  source: string;
  key: string;
}
