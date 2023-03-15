import os
import sys

sys.path.append(os.getcwd())

from sources.luminousscans import LuminousScans  # noqa: E402
from utils import SourceTester  # noqa: E402

test = SourceTester(
    cl=LuminousScans,
    search_query="gods",
    manhwa_slug="series/1677679234-level-up-with-all-gods",
    chapter_url="https://luminousscans.com/leveling-up-with-the-gods-chapter-73/",
)


if __name__ == "__main__":
    test.run()
