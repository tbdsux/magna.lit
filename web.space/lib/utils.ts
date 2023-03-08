export const joinParams = (p: string | string[]) =>
  Array.isArray(p) ? p.join() : p;
