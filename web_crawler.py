import time
import requests
import bs4
import urllib
from bs4 import BeautifulSoup


def continue_crawl(article_chain, target_url):
    if article_chain[-1] == target_url:
        print ("We have reached the target URL! " + article_chain[-1])
        return False
    elif len(article_chain)>25:
        print("We have crawled more than 25 links! Aborting Search!")
        return False
    elif article_chain[-1] in article_chain[:-1]:
        print(article_chain[-1]+" is looping over the existing links!")
        return False
    else:
        return True

def wait_some_sec(sec):
    time.sleep(sec)


def find_first_link(url):
    # get the html text from the page
    response = requests.get(url)
    html = response.text
    # pass it to bs4
    soup = bs4.BeautifulSoup(html, "html.parser")
    # find first link
    article_link = None
    content_div = soup.find(
        id="mw-content-text").find(class_="mw-parser-output")
    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get('href')
            break
    if not article_link:
        return
    #Complete the first link
    article_link = urllib.parse.urljoin("https://en.wikipedia.org", article_link)
    # return first link
    return article_link


# Any random url to start
# https://en.wikipedia.org/wiki/American_Board_of_Medical_Specialties this URL works
start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
# Array of URL's
article_chain = [start_url]
#time to wait before clicking next link, so that wikipedia does not suspect that it's a program.
wait_time = 2
while continue_crawl(article_chain, target_url):
    first_link = find_first_link(article_chain[-1])
    # if the first link comes empty
    print (article_chain[-1])
    if not first_link:
        print ("We do not have links in this article.\nSo stopping further searches!")
        break
    article_chain.append(first_link)
    # wait for some time
    wait_some_sec(wait_time)
