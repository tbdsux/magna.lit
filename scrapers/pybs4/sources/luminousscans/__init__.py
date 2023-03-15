from urllib.parse import quote

from sources.base import BaseSource
from sources.response import BaseResponse
from sources.utils import request

BASE_URL = "https://luminousscans.com"


class LuminousScans(BaseSource):
    @staticmethod
    def search(query: str) -> BaseResponse:
        r = request(BASE_URL + f"/?s={quote(query)}")

        try:
            container = r.find("div", class_="postbody")
            results_container = container.find_all("div", class_="bs")
        except Exception as e:
            print(e)
            return BaseResponse(error=False, data=[])

        results = []
        for i in results_container:
            _img = i.find("img").get("src")
            _title = i.find("div", class_="tt").get_text().strip()
            _url = i.find("a").get("href")
            _slug = _url.replace(BASE_URL, "").strip()

            results.append({"image": _img, "title": _title, "url": _url, "slug": _slug})

        return BaseResponse(error=False, data=results)

    @staticmethod
    def get_manhwa(manhwa: str) -> BaseResponse:
        main_url = BASE_URL + f"/{manhwa.strip('/')}"
        r = request(main_url)

        container = r.find("div", class_="postbody")

        # get manhwa title
        _title = container.find("h1", class_="entry-title").get_text().strip()

        # get manhwa image
        _image = container.find("img", class_="wp-post-image").get("src")

        _authors = []

        _tags_details = container.find("div", class_="tsinfo").find_all(
            "div", class_="imptdt"
        )
        for i in _tags_details:
            # get author
            if "author" in i.get_text().strip().lower():
                _authors = [k.strip() for k in i.find("i").get_text().split(",")]

        # get genres
        _genres = [
            i.text.strip() for i in container.find("span", class_="mgen").find_all("a")
        ]

        # get summary
        _summary = (
            container.find("div", class_="entry-content entry-content-single")
            .get_text()
            .strip()
        )

        # get chapters
        _chapters_container = container.find("div", id="chapterlist")
        _chapters_all = _chapters_container.find_all("li")
        _chapters = []

        for i in _chapters_all:
            _chapter_url = i.find("a").get("href")
            _chapter_title = i.find("span", class_="chapternum").get_text().strip()
            _chapter_release = i.find("span", class_="chapterdate").get_text().strip()

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

        container = r.find("div", class_="chapterbody")

        # get chapter title
        _title = container.find("h1", class_="entry-title").get_text().strip()

        # get chapter images
        _chapter_images_container = container.find("div", id="readerarea")
        _images = [
            i.find("img").get("src").strip()
            for i in _chapter_images_container.find_all("p")
        ]

        return BaseResponse(error=False, data={"title": _title, "images": _images})
