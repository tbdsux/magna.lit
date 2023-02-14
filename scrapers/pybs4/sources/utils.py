from __future__ import annotations

from typing import Any, Dict

import requests
from bs4 import BeautifulSoup

default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def request(url: str, headers: Dict[str, Any] = {}) -> BeautifulSoup:
    r = requests.get(url, headers=default_headers | headers)

    if r.status_code != 200:
        print(
            r.status_code, url
        )  # TODO: Only used for debugging, should be removed in the future.
        raise Exception("Failed to get request website url.")

    return BeautifulSoup(
        r.text,
        "lxml",
    )


def request_post(url: str, headers: Dict[str, Any] = {}) -> BeautifulSoup:
    r = requests.post(url, headers=default_headers | headers)

    if r.status_code != 200:
        print(
            r.status_code, url
        )  # TODO: Only used for debugging, should be removed in the future.
        raise Exception("Failed to get request website url.")

    return BeautifulSoup(
        r.text,
        "lxml",
    )
