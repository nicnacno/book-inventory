#check for library.csv, if it doesn't exist, create it (with warning message that none was found)

"""library.csv format
isbn (manual input)
title (from openlibrary)
author code (from openlibrary via second API query)
page count 
publish date
"""
#for csv management
import csv

#for openlibrary API query 
import json
import requests
import urllib.parse


#test isbn:    0140328726  or  9780140328721
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/ 
# book_response = requests.get("https://openlibrary.org/isbn/9780140328721.json")

isbnID = "0140328726"
url = "https://openlibrary.org/isbn/" + isbnID + ".json" #modifiable input for api

book_response = requests.get(url) #query for isbn from openlibrary
#for valid query test in implementation
if book_response.status_code == 200:
    print("query successful")
else:
    print("invalid query, please try again")


data = book_response.json() #type is dict
title = data["title"]
published = data["publish_date"]
pages = data["number_of_pages"]

#TDB how to handle multiple authors
authors = data["authors"] #list of author keys
author = authors[0]["key"] #returns first author