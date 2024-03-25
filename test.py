import requests
from main import HEADERS,PROXIES

test = "https://www.dndbeyond.com/magic-items?filter-type=0&filter-search=circlet&filter-requires-attunement=&filter-effect-type=&filter-effect-subtype=&filter-has-charges=&filter-partnered-content=t"
test2 = "https://www.dndbeyond.com/magic-items?filter-type=0&filter-search=spider+staff&filter-requires-attunement=&filter-effect-type=&filter-effect-subtype=&filter-has-charges=&filter-partnered-content="
page = requests.get(test, headers=HEADERS, timeout=10)

print(page.status_code)
print(page.close)