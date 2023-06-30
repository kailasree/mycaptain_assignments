import requests
from bs4 import BeautifulSoup

wikipedia_url = "https://en.wikipedia.org/wiki/Taylor_Swift"

req = requests.get(wikipedia_url)
content = req.content

soup = BeautifulSoup(content, "html.parser")

body = soup.find("body", {"class":"skin-vector skin-vector-search-vue mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject page-Taylor_Swift rootpage-Taylor_Swift skin-vector-2022 action-view"}).text
print(body)
