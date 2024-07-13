from bs4 import BeautifulSoup 
import requests


hdrs={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'} 


def allNews(url, hdrs):
    page = requests.get(url, headers = hdrs)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find("h1").get_text()
    all_paragraphs = soup.find_all('p')
    news = ""
    for paragraph in all_paragraphs:
        para = paragraph.get_text()
        para = para.strip()
        news += para
    return title, news

url = "https://indianexpress.com/elections/bjp-hyderabad-madhavi-latha-burqa-clad-women-voting-elections-9325267/"

t, n = allNews(url, hdrs)

print("Title", t)

