<div align=center>
    <img src="./banner.png" />
    <p>A manga, manhwa, manhua reader / scraper / aggregator in Deta Space.</p>
</div>

## Sources

- [Leviatanscans](https://en.leviatanscans.com/home/)

### Request new source?

Please use the [issues](https://github.com/tbdsux/magna.lit/issues) for requesting new website sources.

If you want to contribute, please check the guide in [scrapers](./scrapers/) (incomplete...)

### Note

Support the original translator's works by reading the content from their own website.

## Development

### Project Structure

- [`web.space`](./web.space/)

Main frontend website build with Nuxt.js

- [`internal-api`](./internal-api/)

Express.js internal api for `web.space`. I separated the api from the builtin Nuxt's server api dir to have more power with api design and easier development with `expressjs`.

- [`scrapers`](./scrapers/)

List of api tools used to scrape data from various sources.

##

**&copy; 2023 - present | tbdsux (Joshue Abance)**
