import sources from "./sources.json";

const allSources = [
  { name: "None", scraper: "", source: "", working: false, website: "" },
  ...sources,
];

export { allSources };
