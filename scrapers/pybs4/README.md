# pybs4

A scraper utilizing python mainly.

Uses: `requests`, `bs4`, `lxml`

### Note:

This doesn't work on some sites, please check carefully.

## How to Add new Source?

~TODO~

### Check the source if compatible with this scraper

```python
import requests

r = requests.get(website)
assert r.status_code == 200
```

If it doesn't return `200` it won't work.
