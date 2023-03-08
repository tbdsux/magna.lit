export interface SearchResultsProps {
  image: string;
  title: string;
  url: string;
  slug: string;
}

export interface ChapterProps {
  title: string;
  images: string[];
}

export interface ManhwaChapterProps {
  title: string;
  url: string;
  release: string;
}

export interface ManhwaProps {
  title: string;
  image: string;
  authors: string[];
  genres: string[];
  summary: string;
  chapters: ManhwaChapterProps[];
  url: string;
}
