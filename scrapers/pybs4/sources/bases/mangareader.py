"""
Details:
    This source base is for websites that use the `MangaReader` Wordpress theme.
"""

from sources.response import BaseResponse
from sources.utils import request


class MangaReader:
    @staticmethod
    def search(base_url: str, url: str) -> BaseResponse:
        r = request(url)

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
            _slug = _url.replace(base_url, "").strip()

            results.append({"image": _img, "title": _title, "url": _url, "slug": _slug})

        return BaseResponse(error=False, data=results)

    @staticmethod
    def get_manhwa(url: str) -> BaseResponse:
        r = request(url)

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
            # special case for flamescans
            .replace(
                "Additional Notes\nOfficial English: Webtoons",
                "",
            )
            .strip()
        )

        # get chapters
        _chapters_container = container.find("div", id="chapterlist")
        _chapters_all = _chapters_container.find_all("li")
        _chapters = []

        for i in _chapters_all:
            _chapter_url = i.find("a").get("href")
            _chapter_title = (
                i.find("span", class_="chapternum")
                .get_text()
                .replace(
                    "\n", " "  # weird but other sites have \n in between title texts
                )
                .strip()
            )
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
                "url": url,
            },
        )

    @staticmethod
    def get_chapter(url: str) -> BaseResponse:
        r = request(url)

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
