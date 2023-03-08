export const genUID = (title: string, source: string) => {
  return `${title.toLowerCase().trim().replaceAll(" ", ".")}-${source}`;
};
