import requests
import bs4

url = "https://github.com/" #urlを指定
text = requests.get(url) #requestでurlの内容を取得
page = bs4.BeautifulSoup(text.text, "html.parser") #

title = page.title.string #タイトルの取得

print(title)