import requests
import json
from bs4 import BeautifulSoup

MAIN_LINK = "https://www.dndbeyond.com/magic-items?filter-partnered-content="
PAGES_LINK = "https://www.dndbeyond.com/magic-items?filter-partnered-content=&page="
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
HEADERS = {'User-Agent': USER_AGENT,
           "Accept-Language": "en-US,en;q=0.9,en-AU;q=0.8",
           }
SEARCH_FILTERS = {
    "page_list": {"class": "b-pagination-list paging-list j-tablesorter-pager j-listing-pagination"},
    "page_list_links": {"class": "b-pagination-item"},
    
}
MAGIC_ITEMS = []
# Dict of magic items
# Name/id
#   Rarity
#   Type
#   Attunement
#   Source Book


def main():
    '''Main'''
    soup = fetchPage(MAIN_LINK)

    # Get page numbers
    page_numbers_list = soup.find("ul", SEARCH_FILTERS["page_list"])
    page_numbers_list = page_numbers_list.find_all("a", SEARCH_FILTERS["page_list_links"])
    lastPage = int(page_numbers_list[-1].getText())

    # Main loop
    if lastPage > 1:
        for pageNumber in range(1, lastPage+1):
            print(f"Parsing page: {pageNumber}")
            pageParse(pageNumber)
    else:
        pageParse(1)

    with open(file='magic_items.json', mode='w', encoding="utf-8") as file:
        json.dump(MAGIC_ITEMS, file)


def pageParse(pageNumber: int):
    """Parses list of items on page and adds to global list"""
    # Build link with page number input
    link = PAGES_LINK + str(pageNumber)
    soup = fetchPage(link)

    # The List
    itemList = soup.find_all("div", {"class": "info", "data-type": "magic-items"})

    # The Split Parse per item
    for item in itemList:
        href = item.find_all("a", {"class": "link"})[-1]["href"].split("/magic-items/")[-1]
        itemID = href.split("-")[0]
        name = item.find("span", {"class": "name"}).get_text().strip()
        name = name.lstrip("Partnered Content").split("\n")[0]
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
    '''Returns a BeautifulSoup object of link provided'''
    try:
        page = requests.get(link, headers=HEADERS, timeout=10)
    except requests.HTTPError as e:
        print("HTTPError: Requesting Page Failed: " + link)
        raise e
    return BeautifulSoup(page.content, 'html.parser')


if __name__ == "__main__":
    main()
