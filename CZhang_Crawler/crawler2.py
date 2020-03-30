# This program fetches the HTML document for a parent URL, looks for the URLs
# within the HTML document, and prints the URLs visited along with all the URLs on
# that page (its children). Then it recursively does this again on each child URL

# import necessary modules
import sys
from queue import *
import requests
from requests import ConnectionError
from bs4 import BeautifulSoup
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import urllib3
import re
import threading
import _thread
import warnings
warnings. filterwarnings("ignore")
urllib3.disable_warnings()
urllib3.disable_warnings(urllib3.exceptions.NewConnectionError)

# Queues are synchronized in Python
all_urls = Queue()
visited_urls = set()
lock = threading.Lock()


def get_urls(new_url):

    # See if we can get a response from the url. If not, then finish.
    try:
        response = requests.get(new_url)
    except(ConnectionError, Exception):
        return
    if response == None:
        return

    # If was able to get a response, then test request status code
    if response != None:
        if response.status_code != 200:
            return
        # If there is a successful connection, begin process of opening html document
        if response.status_code == 200:
            # each thread will have its own parent and list of children
            children_list = []
            parent = new_url
            visited_urls.add(new_url)

            # Try to open the url
            try:
                html_page = urllib2.urlopen(new_url)
            except(ConnectionError, Exception):
                return

            # If the url could be opened, parse for the urls within the a href tags.
            # Add all children urls to indiv_list
            soup = BeautifulSoup(html_page, "lxml")
            for link in soup.findAll('a', attrs={'href': re.compile("^https?://")}):
                children_list.append(link.get('href'))
                all_urls.put(link.get('href'))

            # Only one thread at a time should print the parent and children
            lock.acquire()
            print(parent)
            for x in children_list:
                print ("    ", x)
            lock.release()

            # Create a thread for each url in the queue
            # Recursively call get_urls again on each item in the queue
            for x in list(all_urls.queue):
                if x not in visited_urls:
                    t = threading.Thread(target=get_urls, args=(x,))
                    t.start()


# Start by inputting a beginning url
#url = input("Enter the url: ")
url = str(sys.argv[1])
get_urls(url)
