'''imports'''
import json
import requests
import pytest
from main import HEADERS, PROXIES
from main import fetchPage, pageParse

TEST_LINKS = [
    "https://www.dndbeyond.com/magic-items?filter-type=0&filter-search=Dragonguard+&filter-requires-attunement=&filter-effect-type=&filter-effect-subtype=&filter-has-charges=&filter-partnered-content=f",
    "https://www.dndbeyond.com/magic-items?filter-type=0&filter-search=Agony&filter-requires-attunement=&filter-effect-type=&filter-effect-subtype=&filter-has-charges=&filter-partnered-content=t",
]

def test():
    for link in TEST_LINKS:
        soup = fetchPage(link)


print(page.status_code)
print(page.close)
