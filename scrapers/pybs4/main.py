from fastapi import FastAPI, Response, status

import sources
from sources.response import BaseResponse

app = FastAPI()


@app.get("/")
def index():
    return "Python BS4 Scraper for Magna.Lit"


@app.get("/search")
def search_manhwa(q: str, source: str, response: Response):
    if q == "" or source == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BaseResponse(error=True, message="Need queries.")

    src = sources.SOURCES.get(source)
    if src is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BaseResponse(
            error=True, message="Source is unknown or not defined from the API"
        ).json()

    try:
        r = src.search(q)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return BaseResponse(
            error=True,
            message=f"A problem has occured while doing some work. Error: {str(e)}",
        ).json()

    return r.json()


@app.get("/manhwa")
def manhwa(manhwa: str, source: str, response: Response):
    if manhwa == "" or source == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BaseResponse(error=True, message="Need queries.")

    src = sources.SOURCES.get(source)
    if src is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BaseResponse(
            error=True, message="Source is unknown or not defined from the API"
        ).json()

    try:
        r = src.get_manhwa(manhwa)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return BaseResponse(
            error=True,
            message=f"A problem has occured while doing some work. Error: {str(e)}",
        ).json()

    return r.json()


@app.get("/chapter-manhwa")
def chapter_manhwa(chapter: str, source: str, response: Response):
    if chapter == "" or source == "":
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BaseResponse(error=True, message="Need queries.")

    src = sources.SOURCES.get(source)
    if src is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return BaseResponse(
            error=True, message="Source is unknown or not defined from the API"
        ).json()

    try:
        r = src.get_chapter(chapter)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return BaseResponse(
            error=True,
            message=f"A problem has occured while doing some work. Error: {str(e)}",
        ).json()

    return r.json()
