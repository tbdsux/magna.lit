from urllib.parse import quote

from sources.base import BaseSource
from sources.response import BaseResponse
from sources.utils import request, request_post

BASE_URL = "https://en.leviatanscans.com/home"


class LeviatanScans(BaseSource):
    @staticmethod
    def get_chapter(chapter_url: str) -> BaseResponse:
        r = request(chapter_url)

        container = r.find("div", class_="c-page-content")

        # get chapter title
        _title = container.find("h1", id="chapter-heading").text.strip()

        # get chapter images
        _chapter_images_container = container.find("div", class_="reading-content")
        _images = [
            i.get("src").strip() for i in _chapter_images_container.find_all("img")
        ]

        return BaseResponse(error=False, data={"title": _title, "images": _images})

    @staticmethod
    def search(query: str):
        r = request(BASE_URL + f"?s={quote(query)}&post_type=wp-manga")

        try:
            container = r.find("div", class_="search-wrap")
            results_container = container.find_all("div", class_="row")
        except Exception as e:
            print(e)
            return BaseResponse(error=False, data=[])

        results = []

        for i in results_container:
            _img = i.find("img").get("src")
            _title = i.find("a").get("title")
            _url = i.find("a").get("href")
            _slug = _url.replace(BASE_URL, "").strip()

            results.append({"image": _img, "title": _title, "url": _url, "slug": _slug})

        return BaseResponse(error=False, data=results)

    @staticmethod
    def get_manhwa(manhwa: str):
        main_url = BASE_URL + f"/{manhwa.strip('/')}"
        r = request(main_url)

        container = r.find("div", class_="site-content")

        # get manhwa title
        _title = container.find("div", class_="post-title").text.strip()

        # get manhwa image
        _image = container.find("div", class_="summary_image").find("img").get("src")

        _tags_containers = container.find("div", class_="summary_content")
        _all_tags_details = _tags_containers.find_all("div", class_="post-content_item")

        _authors = [
            i.get_text().strip()
            for i in _tags_containers.find("div", class_="manga-authors").find_all("a")
        ]
        _summary = (
            _tags_containers.find("div", class_="manga-summary").get_text().strip()
        )

        _genres = []
        for i in _all_tags_details:
            _tag = i.find("h5").text.strip().lower()

            # get genre
            if "genre" in _tag:
                _r_genres = i.find_all("a")
                _genres = [k.get_text().strip() for k in _r_genres]

        # get chapters
        _chapters_r = request_post(main_url + "/ajax/chapters")
        _chapters_container = _chapters_r.find("div", class_="listing-chapters_wrap")
        _chapters_all = _chapters_container.find_all("li", class_="wp-manga-chapter")
        _chapters = []

        for i in _chapters_all:
            _chapter_url = i.find("a").get("href")
            _chapter_release = i.find(
                "span", class_="chapter-release-date"
            ).text.strip()
            _chapter_view = i.find("span", class_="view").text.strip()

            _chapter_title = (
                i.text.replace(_chapter_release, "").replace(_chapter_view, "").strip()
            )

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
