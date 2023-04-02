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
        {
          rel: "icon",
          type: "image/png",
          href: "/icon.png",
        },
      ],
    },
  },
  runtimeConfig: {
    public: {
      rootUrl:
        process.env.NODE_ENV === "development"
          ? "http://localhost:4200"
          : `http://${process.env.DETA_SPACE_APP_HOSTNAME}`,
    },
  },
});
