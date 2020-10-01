# exercise 1
import pandas as pd
PATH        = "./"
CSV_FILE    = 'grades.csv'
dataset     = { "NumericGrade":[99,98,84], "LetterGrade":['A+', 'A', 'B']}
dfOut       = pd.DataFrame( data = dataset)

# Here I have decided to use a tab separator.
# The default separator is a comma which also could work.
dfOut.to_csv(PATH + CSV_FILE, sep=',')

# Since I saved the file with a tab separator the instruction
# that reads the content must also use a tab separator.
dfIn        = pd.read_csv(PATH + CSV_FILE, sep=',')
print(dfIn)


# exsample 2
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PATH    = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
browser = None

# This loads webdriver from the local machine if it exists.
try:
    browser = webdriver.Chrome(PATH)
    print("The path to webdriver_manager was found.")

# If a webdriver not found error occurs it is then downloaded.
except:
    print("webdriver not found. Update 'PATH' with file path in the download.")
    browser = webdriver.Chrome(ChromeDriverManager().install())


# Example 4: Scraping Rotten Tomatoes
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://www.rottentomatoes.com/critics/latest_reviews"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

content = browser.find_elements_by_css_selector(".critics-latest-reviews__data-review .a")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="html.parser")
    print(soup.get_text())
    print("***")  # Go to new line.




# Exercese 4: rating
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://www.rottentomatoes.com/critics/latest_reviews"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

content = browser.find_elements_by_css_selector(".critics-latest-reviews__data-rating")
for e in content:
    start = e.get_attribute('innerHTML')
    # Beautiful soup allows us to remove HTML tags from our content if it exists.
    soup = BeautifulSoup(start, features="html.parser")
    print(soup.get_text())
    print("***")  # Go to new line.



#Example 6: Custom Parsing
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="html.parser")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    print(rawString)
    print("***")



#Example 7: Cleaning Up Our Output
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="html.parser")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    # print(rawString)
    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    location = eventArray[len(eventArray) - 1]
    print("Name:     " + eventName)
    print("Date:     " + eventDate)
    print("Time:     " + eventTime)
    print("Location: " + location)
    print("***")



#Example 8: Clicking
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(4)

button = browser.find_element_by_css_selector(".btn-lg")
for i in range(0,15):
    button.click()
    '''
    If you see the following error increase the sleep time:
    ElementClickInterceptedException: element click intercepted:
    '''
    print("Count: ", str(i))
    time.sleep(4)
print("done loop")


content = browser.find_elements_by_css_selector(".event-row")
for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="html.parser")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    # print(rawString)
    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2
    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    location = eventArray[len(eventArray) - 1]
    print("Name:     " + eventName)
    print("Date:     " + eventDate)
    print("Time:     " + eventTime)
    print("Location: " + location)
    print("***")




# Example 9: Sending Keys

import time
import re
from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://www.bcit.ca/"

browser = webdriver.Chrome(PATH)
browser.get(URL)

time.sleep(5)

# Find the search input.
search = browser.find_element_by_css_selector("#headersearch_query")
search.send_keys("Analytics")

# Find the search button - this is only enabled when a search query is entered
button = browser.find_element_by_css_selector("#headersearch_submit")
button.click()  # Click the button.

# Scrape the search results.   #.bcit-search-results__item
content = browser.find_elements_by_css_selector(".bcit-search-results__title a")

for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="html.parser")

    # Create a string delimiter with a unique character combination.
    content = soup.get_text(separator='??')
    contentList = content.split("??")

    newList = []
    for i in range(0, len(contentList)):
        tempString = contentList[i]
        tempString = tempString.strip()  # Remove leading and trailing spaces.
        tempString = re.sub(r"[\n\t]*", "", tempString)

        # Remove 2+ consecutive spaces.
        tempPhrase = re.sub('[ ]{2,}', '*', tempString)
        # Removes other special characters.
        tempPhrase = tempPhrase.encode('ascii', 'ignore').decode('ascii')

        if (len(tempPhrase) > 1):
            newList.append(tempPhrase)
    print(newList)





# exercise 12
class Child:  # Declare class.
    age = 0  # Declare and initialize age property.
    firstName = ""  # Declare and initialize firstName property.
    lastName = ""

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    # Declare a function to display details about the child.
    def showDetail(self):
        print("The child's name is:   " + self.firstName + " " + self.lastName );
        print(self.firstName +" " + self.lastName + "'s age is: " + str(self.age));


childA = Child("Jenny", "Douglas", 5)
childA.showDetail()

childB = Child("Mark", "Douglas",2)
childB.showDetail()



# exercise 12
class BankAccount:  # Declare class.
    accountNumber = 0
    balance = 0
    firstName = ""
    lastName = ""

    # This is our constructor. It initializes variables when the object is created.
    def __init__(self, accountNumber, balance, firstName, lastName):
        self.accountNumber = accountNumber
        self.balance = balance
        self.firstName = firstName
        self.lastName = lastName

    def addInterest(self, interestRate=0.03):
        self.balance = round( self.balance * (1+interestRate), 2)

    # Declare a function to display details about the child.
    def showDetail(self):
        print("Account owner :   " + self.firstName + " " + self.lastName );
        print("Account number:   " + str(self.accountNumber));
        print("Account Balance:  " + str(self.balance));
        print("")


accountA = BankAccount(20000101, 1000, "Jenny", "Douglas")
accountB = BankAccount(20001234, 12345678.99, "Mark", "Douglas")
accountA.addInterest()
accountB.addInterest()
accountA.showDetail()
accountB.showDetail()

# Exercise 14
# #Example 7: Cleaning Up Our Output
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

content = browser.find_elements_by_css_selector(".event-row")


class LibraryEvent:
    eventName = ""
    eventDate = ""
    eventTime = ""
    eventLocation = ""

    def __init__(self, eventName, eventDate, eventTime, eventLocation):
        self.eventName = eventName
        self.eventDate = eventDate
        self.eventTime = eventTime
        self.eventLocation = eventLocation

    def showEvent(self):
        print("Name:     " + self.eventName)
        print("Date:     " + self.eventDate)
        print("Time:     " + self.eventTime)
        print("Location: " + self.eventLocation)
        print("")


eventList = []

for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="html.parser")
    rawString = soup.get_text().strip()

    # Remove hidden characters for tabs and new lines.
    rawString = re.sub(r"[\n\t]*", "", rawString)

    # Replace two or more consecutive empty spaces with '*'
    rawString = re.sub('[ ]{2,}', '*', rawString)

    # Fine tune the results so they can be parsed.
    rawString = rawString.replace("Location", "Location*")
    rawString = rawString.replace("Registration closed", "Registration closed*")
    rawString = rawString.replace("Registration required", "Registration required*")
    rawString = rawString.replace("In Progress", "*In Progress*")
    rawString = rawString.replace("*/*", "/")
    rawString = rawString.replace("Full*", "*Full*")

    # print(rawString)
    eventArray = rawString.split('*')

    EVENT_NAME = 0
    EVENT_DATE = 1
    EVENT_TIME = 2

    eventName = eventArray[EVENT_NAME]
    eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
    eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
    location = eventArray[len(eventArray) - 1]

    eventObject = LibraryEvent(eventName, eventDate, eventTime, location)
    eventList.append(eventObject)

for event in eventList:
    event.showEvent()



# Exercise 14
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import re

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://vpl.bibliocommons.com/events/search/index"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)

content = browser.find_elements_by_css_selector(".event-row")

class LibraryEvent:
    eventName=""
    eventDate=""
    eventTime=""
    eventLocation=""

    def parseringEvent(self, rawString, EVENT_NAME=0, EVENT_DATE=1, EVENT_TIME=2, EVENT_LOC=-1):
        # Remove hidden characters for tabs and new lines.
        rawString = re.sub(r"[\n\t]*", "", rawString)

        # Replace two or more consecutive empty spaces with '*'
        rawString = re.sub('[ ]{2,}', '*', rawString)

        # Fine tune the results so they can be parsed.
        rawString = rawString.replace("Location", "Location*")
        rawString = rawString.replace("Registration closed", "Registration closed*")
        rawString = rawString.replace("Registration required", "Registration required*")
        rawString = rawString.replace("In Progress", "*In Progress*")
        rawString = rawString.replace("*/*", "/")
        rawString = rawString.replace("Full*", "*Full*")

        eventArray = rawString.split('*')

        self.eventName = eventArray[EVENT_NAME]
        self.eventDate = eventArray[EVENT_DATE].strip()  # remove leading and trailing spaces
        self.eventTime = eventArray[EVENT_TIME].strip()  # remove leading and trailing spaces
        self.eventLocation = eventArray[len(eventArray) + EVENT_LOC]


    def showEvent(self):
        print("Name:     " + self.eventName)
        print("Date:     " + self.eventDate)
        print("Time:     " + self.eventTime)
        print("Location: " + self.eventLocation)
        print("")


eventList=[]

for e in content:
    textContent = e.get_attribute('innerHTML')
    # Beautiful soup removes HTML tags from our content if it exists.
    soup = BeautifulSoup(textContent, features="html.parser")
    rawString = soup.get_text().strip()

    eventObject = LibraryEvent()
    eventObject.parseringEvent(rawString)
    eventList.append(eventObject)

for event in eventList:
    event.showEvent()

