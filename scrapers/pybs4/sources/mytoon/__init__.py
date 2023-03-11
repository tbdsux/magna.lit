from urllib.parse import quote

from sources.base import BaseSource
from sources.response import BaseResponse
from sources.utils import request

BASE_URL = "https://mytoon.net/"


class MyToon(BaseSource):
    @staticmethod
    def search(query: str) -> BaseResponse:
        r = request(BASE_URL + f"?s={quote(query)}")

        try:
            container = r.find("div", class_="comics-grid")
            results_container = container.find_all("div", class_="entry")
        except Exception as e:
            print(e)
            return BaseResponse(error=False, data=[])

        results = []

        for i in results_container:
            _img = i.find("img").get("src").strip()
            _title = i.find("h3", class_="name").get_text().strip()
            _url = i.find("a").get("href")
            _slug = "/" + _url.replace(BASE_URL, "")

            results.append({"image": _img, "title": _title, "url": _url, "slug": _slug})

        return BaseResponse(error=False, data=results)

    @staticmethod
    def get_manhwa(manhwa: str) -> BaseResponse:
        main_url = BASE_URL + f"/{manhwa.strip('/')}"
        r = request(main_url)

        container = r.find("section", class_="main").find("div", class_="container")

        # get manhwa title
        _title = container.find("h1").get_text().strip()

        # get manhwa image
        _image = container.find("img").get("src")

        # get authors
        _authors_container = container.find("div", class_="author")
        _authors = [k.text.strip() for k in _authors_container.find_all("a")]

        # get genres
        _genres_container = container.find("div", class_="genre")
        _genres = [k.text.strip() for k in _genres_container.find_all("a")]

        # get summary
        _summary = container.find("div", id="desc").find("p").get_text()

        # get chapters
        _chapters_container = container.find("div", class_="chapters-wrapper")
        _chapters_all = _chapters_container.find_all("div", class_="two-rows go-border")
        _chapters = []

        for i in _chapters_all:
            _chapter_url = i.find("a").get("href")
            _chapter_title = i.find("a").get_text().strip()
            _chapter_release = i.find("div", class_="chapter-date").get_text().strip()

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

        # get chapter title
        _title = r.find("a", class_="bg-tt").get_text().strip()

        # get chapter images
        _chapter_images_container = r.find("div", class_="chapter-content")
        _images = [
            i.get("src").strip() for i in _chapter_images_container.find_all("img")
        ]

        return BaseResponse(error=False, data={"title": _title, "images": _images})
