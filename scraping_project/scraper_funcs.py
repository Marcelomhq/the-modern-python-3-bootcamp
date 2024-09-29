 #url https://quotes.toscrape.com/
import requests
from bs4 import BeautifulSoup
from time import sleep
from csv_funcs import dict_quotes, csv_file1

base_url = "https://quotes.toscrape.com"

def scraper_func():
    all_quotes = []    
    url = "/page/1/"

    while url:
        res = requests.get(f"{base_url}{url}")
        print(f"Now scrapping{base_url}{url} ...")
        soup = BeautifulSoup(res.text, features="html.parser")
        quotes = soup.find_all(class_="quote")
        for quote in quotes:
            all_quotes.append({
                    "quote":quote.find(class_ = "text").get_text(),
                    "author":quote.find(class_ = "author").get_text(),
                    "bio-link":quote.find("a")["href"]
                })
            
        next_btn = soup.find(class_ = "next")
        url = next_btn.find('a')['href'] if next_btn else None
        
        print("waiting 3 seconds")
        # sleep(3)
        
    dict_quotes(all_quotes)
    print(f"Quotes, Authors and Bio Links saved into csv {csv_file1} succesfully")

def bio_link_scraper(link):
    res1 = requests.get(f"{base_url}{link}")
    soup1 = BeautifulSoup(res1.text, features="html.parser")
    author_info = soup1.find(class_="author-details")
    author_info = (f'Author born on {(author_info.find(class_ = "author-born-date").get_text())} {author_info.find(class_ = "author-born-location").get_text()}')
    return author_info


if __name__ == '__main__':
    # scraper_func()
    link = "/author/C-S-Lewis"
    bio_link_scraper(link)
    print("running scrapper only")
    
