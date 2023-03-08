export interface ScraperAPIProps<T = never> {
  error: boolean;
  data?: T;
  message?: string;
}

export type InternalAPIProps<T> = ScraperAPIProps<T>;
