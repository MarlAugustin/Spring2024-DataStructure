# Python scrapes a web page using BeautifulSoup
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# If you start your own repl, click on Packages (box) on left, search for BeautifulSoup4 and add.
# On a local system, pip install urllib bs4

from urllib.request import HTTPError, urlopen
import requests
from bs4 import BeautifulSoup
import time

rootsite = urlopen(
    "https://www.blueletterbible.org/")
#print(file.read())
soup = BeautifulSoup(rootsite, 'html.parser')
link_queue = []
visited_links = []
hashtable = {}
# beautifulsoup makes it easy to find tags like <title>
for link in soup.find_all('a'):
  try:
    if "javascript" in link.get('href'):
      pass
    else:
      if "html" in link.get('href') and "http" not in link.get('href'):
        link_queue.append(rootsite.url + link.get('href'))
      if "https://" in link.get('href') or "http://" in link.get('href'):
        if "?" not in link.get('href'):
          link_queue.append(link.get('href'))
        else: 
          pass
  except:
    pass
# print(soup.find_all('a'))
print("original size:", len(link_queue))
while len(link_queue) > 0:
  try:
    time.sleep(1)
    first_link = urlopen(link_queue[0])
    link_queue.pop(0)
    if (first_link.geturl() not in visited_links):
      first_link_soup = BeautifulSoup(first_link, 'html.parser')
      visited_links.append(first_link.geturl())
      titletag = first_link_soup.find('title')
      if type(titletag) is type(None):
        pass
      else:
        hashtable.update({titletag.get_text().lower(): first_link.geturl()})
        print("title:", titletag.get_text())
  except HTTPError as err:
    if err.code == 403:
      print("403 error")
      link_queue= []
      pass
    else:
      print("HTTP Error: " + str(err.code))
      link_queue= []
      pass
    

user_search = input(
    "Enter a word to search for in the titles of the web pages: ").lower()
if user_search in hashtable:
  print("Value of " + user_search + " ", hashtable[user_search])
else:
  print("Key not found")
