# pybs4

A scraper utilizing python mainly.

Uses: `requests`, `bs4`, `lxml`

### Note:

This doesn't work on some sites, please check carefully.

## How to add sources?

(to be improved)

- Create a directory name of the new source

- Extend the base scraper class

  ```python
  # __init__.py

  from sources.base import BaseSource

  class MyNewSource(BaseSource):
      pass
      # implement base functions in here
  ```

  You can use the file as basis [`leviatanscans/__init__.py`](./sources/leviatanscans/__init__.py)

- Add the source in the [`__init__.py`](./sources/__init__.py)

  ```python
  # DEFINE NEW SOURCES IN HERE
  SOURCES = {
      "leviatanscans": LeviatanScans,
      "mynewsource": MyNewSource,
    }
  ```

### Check the source if compatible with this scraper

```python
import requests

r = requests.get(website)
assert r.status_code == 200
```

If it doesn't return `200` it won't work.
