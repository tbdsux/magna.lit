import os
import sys

sys.path.append(os.getcwd())


from sources.flamescans import FlameScans  # noqa: E402
from utils import SourceTester  # noqa: E402

test = SourceTester(
    cl=FlameScans,
    search_query="solo",
    manhwa_slug="series/1678921321-solo-necromancy",
    chapter_url="https://flamescans.org/solo-necromancy-chapter-78/",
)

if __name__ == "__main__":
    test.run()
