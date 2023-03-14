from urllib.parse import quote

from sources.base import BaseSource
from sources.response import BaseResponse
from sources.utils import request

BASE_URL = "https://manganato.com"
MANHWA_CHAPTER_URL = "https://chapmanganato.com"


class Manganato(BaseSource):
    @staticmethod
    def search(query: str) -> BaseResponse:
        r = request(BASE_URL + f"/search/story/{quote(query)}")

        try:
            container = r.find("div", class_="panel-search-story")
            results_container = container.find_all("div", class_="search-story-item")
        except Exception as e:
            print(e)
            return BaseResponse(error=False, data=[])

        results = []
        for i in results_container:
            _img = i.find("img").get("src")
            _rtitle = i.find("h3")

            _title = _rtitle.get_text().strip()
            _url = _rtitle.find("a").get("href")
            _slug = _url.replace(MANHWA_CHAPTER_URL, "").strip()

            results.append({"image": _img, "title": _title, "url": _url, "slug": _slug})

        return BaseResponse(error=False, data=results)

    @staticmethod
    def get_manhwa(manhwa: str) -> BaseResponse:
        main_url = MANHWA_CHAPTER_URL + f"/{manhwa.strip('/')}"
        r = request(main_url)

        container = r.find("div", class_="container-main-left")

        # get manhwa title
        _title = container.find("h1").get_text().strip()

        # get manhwa image
        _image = container.find("span", class_="info-image").find("img").get("src")

        _all_tags_details = container.find(
            "table", class_="variations-tableInfo"
        ).find_all("tr")

        _authors = []
        _genres = []

        for i in _all_tags_details:
            _tag = i.find("td", class_="table-label").get_text().strip().lower()

            # get author
            if "author" in _tag:
                _r_authors = i.find("td", class_="table-value").find_all("a")
                _authors = [k.text.strip() for k in _r_authors]

            # get genre
            if "genre" in _tag:
                _r_genres = i.find("td", class_="table-value").find_all("a")
                _genres = [k.text.strip() for k in _r_genres]

        # get summary
        _summary_container = container.find(
            "div", class_="panel-story-info-description"
        )
        _summary = (
            _summary_container.get_text()
            .replace(_summary_container.find("h3").get_text().strip(), "")
            .strip()
        )

        # get chapters
        _chapters_container = container.find("ul", class_="row-content-chapter")
        _chapters_all = _chapters_container.find_all("li")
        _chapters = []

        for i in _chapters_all:
            _chapter_link = i.find("a")
            _chapter_url = _chapter_link.get("href")
            _chapter_title = _chapter_link.get_text().strip()
            _chapter_release = i.find("span", class_="chapter-time").get_text().strip()

            _chapters.append(
                {
                    "title": _chapter_title,
                    "url": _chapter_url,
                    "release": _chapter_release,
                }
            )

        return BaseResponse(
            error=False,
            data={
                "title": _title,
                "image": _image,
                "authors": _authors,
                "genres": _genres,
                "summary": _summary,
                "chapters": _chapters,
                "url": main_url,
            },
        )

    @staticmethod
    def get_chapter(chapter_url: str) -> BaseResponse:
        r = request(chapter_url)

        container = r.find("div", class_="body-site")

        # get chapter title
        _title = container.find("h1").get_text().strip().title()

        # get chapter images
        _chapter_images_container = container.find(
            "div", class_="container-chapter-reader"
        )
        _images = [
            i.get("src").strip() for i in _chapter_images_container.find_all("img")
        ]

        return BaseResponse(error=False, data={"title": _title, "images": _images})
