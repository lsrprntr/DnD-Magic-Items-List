import urllib.request, urllib.parse, urllib.error
import json
from bs4 import BeautifulSoup

MAIN_LINK = "https://www.dndbeyond.com/magic-items?filter-partnered-content="
PAGES_LINK = "https://www.dndbeyond.com/magic-items?filter-partnered-content=&page="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
HEADERS = {'User-Agent': USER_AGENT, "Accept-Language": "en-US, en;q=0.5"}
SEARCH_FILTERS = {"class": "b-pagination-list paging-list j-tablesorter-pager j-listing-pagination"}

MAGIC_ITEMS = []
# Dict of magic items
# Name/id
#   Rarity
#   Type
#   Attunement
#   Source Book

def main():
    soup = fetchPage(MAIN_LINK)

    # Get page numbers
    page_numbers_list = soup.find("ul", SEARCH_FILTERS).find_all("a", {"class": "b-pagination-item"})
    lastPage = int(page_numbers_list[-1].getText())

    # Main loop
    if lastPage > 1:
        for pageNumber in range(1, lastPage+1):
            print(f"Parsing page: {pageNumber}")
            pageParse(pageNumber)
            break
    else:
        pageParse(1)

    with open(file='magic_items.json', mode='w', encoding="utf-8") as file:
        json.dump(MAGIC_ITEMS, file)



def pageParse(pageNumber: int):
    link = PAGES_LINK + str(pageNumber)
    test = "https://www.dndbeyond.com/magic-items?filter-type=0&filter-search=far+sight&filter-requires-attunement=&filter-effect-type=&filter-effect-subtype=&filter-has-charges=&filter-partnered-content="
    # Try request
    soup = fetchPage(test)

    # The List
    itemList = soup.find_all("div", {"class": "info", "data-type": "magic-items"})

    # The Split Parse
    for item in itemList:
        href = item.find_all("a", {"class": "link"})[-1]["href"].split("/magic-items/")[-1]
        print(href)
        itemID = href.split("-")[0]
        name = item.find("span", {"class": "name"}).get_text().strip()
        name = name.lstrip("Partnered Content").rstrip("\n\n\n\n").strip()
        print(name)
        rarity = item.find("span", {"class": "rarity"}).get_text().strip()
        itemType = item.find("span", {"class": "type"}).get_text().strip()

        # Building the item
        magic_item = {}
        magic_item["id"] = itemID
        magic_item["name"] = name
        magic_item["rarity"] = rarity
        magic_item["type"] = itemType

        MAGIC_ITEMS.append(magic_item)
        print(f"Added: {name}")



def fetchPage(link: str):
    response = urllib.request.Request(link, headers=HEADERS)
    try:
        page = urllib.request.urlopen(response)
    except:
        print("Error: Requesting Page Failed: " + link)
        raise

    return BeautifulSoup(page, 'html.parser')


if __name__ == "__main__":
    main()
