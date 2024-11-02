from tkinter import *
import tkinter as tk
from urllib.request import HTTPError, urlopen
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from tkinter import messagebox
import time

from nltk.downloader import ErrorMessage

frequent_words = {}
links = {}
link_queue = []
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def url_scrape(url):
  # this function is used to find the links from the given url. .
  #the algorithm is either big o of n or o of n^2
  #because of 'in' is used on a list, it could take 1 step or n step
  """
  A couple of working url to test, uncomment the one you want to test if you       don't want to type it.
  url = "https://docs.python.org/3/"
  url = "https://citelms.net/Internships/Summer_2018/Fan_Site/"
  url = "https://www.walmart.com/ip/Beats-Studio3-Wireless-Noise-Cancelling-Headphones-with-Apple-W1-Headphone-Chip-Matte-Black/321284247"
  url = "https://www.target.com/"
  url = "https://www.walmart.com/"
  url = "https://www.bandainamcoent.com/"
  url = "https://www.google.com/"
  """

  rootsite = urlopen(url)
  soup = BeautifulSoup(rootsite, 'html.parser')
  link_queue.append(rootsite.geturl() + "index.html")
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
    while len(link_queue) > 0:
      time.sleep(1)
      first_link = urlopen(link_queue[0])
      link_queue.pop(0)
      if (first_link.geturl() not in links):
        first_link_soup = BeautifulSoup(first_link, 'html.parser')
        titletag = first_link_soup.find('title')
        if type(titletag) is not type(None):
          links.update({titletag.get_text(): first_link.geturl()})
        else:
          pass


class Interface:

  def __init__(self, window):
    self.window = window
    self.window.title("Marlond Final Project")
    self.window.configure(background='#cccccc')
    window.geometry("550x400")
    self.frame_instructions = Frame(window, bg="grey")
    self.frame_instructions.pack(side=TOP)
    self.frame_results = Frame(window, bg="grey")
    self.frame_results.pack(side=BOTTOM)

    #Label
    self.label = Label(self.frame_instructions,
                       text="Enter the URL of the website you want to scrape",
                       width=36,
                       bg="#cccccc")
    self.label.grid(column=0, row=0)
    #Entry
    self.et_url = Entry(self.frame_instructions, width=20)
    self.et_url.grid(column=1, row=0)
    #Button
    self.btn_url_search = Button(self.frame_instructions,
                                 text="Set up",
                                 command=self.btn_url_search_clicked)
    self.btn_url_search.grid(column=2, row=0)

    #Label
    self.label_word = Label(self.frame_instructions,
                            width=36,
                            text="Enter the word you want to search",
                            bg="#cccccc")
    self.label_word.grid(column=0, row=2)

    #Entry
    self.et_word = Entry(self.frame_instructions, width=20)
    self.et_word.grid(column=1, row=2)
    #Button
    self.btn_search = Button(self.frame_instructions,
                             text="Search",
                             command=self.btn_search_clicked)
    self.btn_search.grid(column=2, row=2)

    #List url
    self.list_url_results = tk.Listbox(self.frame_results)
    self.list_url_results.bind("<<ListboxSelect>>",
                               self.list_url_results_clicked)
    self.list_url_results.grid(column=0, row=1)

    #array results
    self.txt_results = Text(self.frame_results, width=60)
    self.txt_results.grid(column=1, row=1)

  def btn_url_search_clicked(self):
    # It has the same run time as the url_scrape function
    try:
      url = self.et_url.get()
      url_scrape(url)
      if self.et_url.get() == "" and len(links) == 0:
        messagebox.showerror("Error", "Please enter a URL")
      if self.et_url.get() != "" and len(links) == 0:
        messagebox.showerror(
            "Error", "This website is not scopable." + "\n" +
            "Please enter a different website")
      else:
        for link in links:
          self.list_url_results.insert(END, link)
    # print(soup.getText())
    except HTTPError as err:
      if err.code == 403 or err.code == 503:
        messagebox.showerror("Error" + str(err.code),
                             "The website does not allow scrapping")
        links.clear()
      else:
        messagebox.showerror("Error", "HTTP Error: " + str(err.code))
        links.clear()

  def list_url_results_clicked(self, evt):
    """
      This function is used to show the link of the selected item in the       list on the text box. It also shows every word contained in the  link which appears more than once.
    """
    #the algorithm is either big o of n or o of n^2
    #because of 'in' is used on a dictionnary, it could take 1 step or n steps
    w = evt.widget
    selected_title = w.get(w.curselection())
    self.txt_results.delete(1.0, END)
    self.txt_results.insert(
        INSERT,
        "The link for the title {} is {}".format(selected_title,
                                                 links[selected_title]))
    self.txt_results.insert(INSERT, "\n")
    self.txt_results.insert(INSERT, "Words contained in the page:\n")
    url = links[selected_title]
    rootsite = urlopen(url)
    soup = BeautifulSoup(rootsite, 'html.parser')
    # print(soup.getText())
    frequent_words = {}
    for text in soup.getText().split():
      if text in stop_words or text in links:
        pass
      else:
        if text in frequent_words:
          frequent_words[text] += 1
        else:
          frequent_words[text] = 1
    dict(sorted(frequent_words.items(), key=lambda item: item[1],
                reverse=True))
    for word in frequent_words:
      if frequent_words[word] > 1:
        self.txt_results.insert(
            INSERT, "The word {} has been found {} times".format(
                word, frequent_words[word]) + " \n")

  def btn_search_clicked(self):
    #the algorithm is either big o of n or o of n^2
    #because of 'in' is used on a list, it could take 1 step or n steps
    if links == {}:
      messagebox.showerror("Url List empty", "You must set up a url first")
      pass
    else:
      searched_word = self.et_word.get()
      self.txt_results.delete(1.0, END)
      self.txt_results.insert(INSERT, "Words contained in the page:\n")
      found = False
      for link in links:
        url = links[link]
        rootsite = urlopen(url)
        soup = BeautifulSoup(rootsite, 'html.parser')
        if searched_word in soup.getText().split():
          count = soup.getText().split().count(searched_word)
          found = True
          self.txt_results.insert(
              INSERT,
              "The word {} appeared {} times in the page {} the title is {} \n"
              .format(searched_word, count, links[link], link))
      if found == False:
        messagebox.showinfo(
            "Word not found",
            "The word {} was not found in any pages".format(searched_word))


if __name__ == "__main__":
  window = Tk()
  Interface(window)
  window.mainloop()
