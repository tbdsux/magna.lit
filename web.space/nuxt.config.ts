// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: ["@pinia/nuxt"],
  css: ["~/assets/css/main.css"],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  app: {
    head: {
      link: [
        {
          rel: "stylesheet",
          href: "https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;500;600;700;800;900&display=swap",
        },
      ],
    },
  },
  runtimeConfig: {
    public: {
      apiPybs4:
        process.env.NODE_ENV === "development"
          ? "http://localhost:8000"
          : "/scrapers-pybs4",
      internalApi:
        process.env.NODE_ENV === "development"
          ? "http://localhost:8080"
          : "/internal-api",
    },
  },
});
