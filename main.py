from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

mainLink = "https://www.dndbeyond.com/magic-items"
pagesLink = "https://www.dndbeyond.com/magic-items?page="

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
headers = {'User-Agent': user_agent, "Accept-Language": "en-US, en;q=0.5"}

search_class = {"class": "b-pagination-list paging-list j-tablesorter-pager j-listing-pagination"}


def main():
    soup = fetchPage(mainLink)
    
    #Get page numbers
    page_numbers_list = soup.find("ul", search_class).find_all("a", {"class":"b-pagination-item"})
    lastPage = page_numbers_list[-1].getText()
    
    #Main loop
    for _ in range(2,lastPage):
        #something append list
        print("yes")
    return

def pageParse(pageNumber:int):
    link = pagesLink + str(pageNumber)
    
    #Try request
    soup = fetchPage(link)
    
    
    return


def fetchPage(link:str):
    response = urllib.request.Request(link, headers=headers)
    try:
        page = urllib.request.urlopen(response)
    except:
        print("Error: Requesting Page Failed: " + link)
        raise Exception()
    return BeautifulSoup(page, 'html.parser')
    
    
if __name__ == "__main__":
    main()