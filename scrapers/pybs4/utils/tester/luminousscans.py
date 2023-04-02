import os
import sys

sys.path.append(os.getcwd())

from sources.luminousscans import LuminousScans  # noqa: E402
from utils import SourceTester  # noqa: E402

test = SourceTester(
    cl=LuminousScans,
    search_query="demon",
    manhwa_slug="series/1680246102-heavenly-demon-chronicles",
    chapter_url="https://luminousscans.com/1680246102-the-chronicles-of-heavenly-demon-chapter-201/",
)


if __name__ == "__main__":
    test.run()
