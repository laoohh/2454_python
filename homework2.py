# this code try to crape Indeed Canada website to get interesting job list

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re


# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://ca.indeed.com/"
browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(3)


# class definition
# this class encapsulation the web manipulation
class IndeedWeb:
    indeedRawData = ""

    def __init__(self):
        self.indeedRawData = ""

    def search(self, what, where):
        # send_keys to "What" and "Where", then click "Find jobs"

        # Find the search input.
        time.sleep(2)
        searchWhat = browser.find_element_by_css_selector('#text-input-what')
        searchWhat.send_keys(what)
        time.sleep(2)

        # Find the "Find jobs" button
        button = browser.find_element_by_css_selector(".icl-WhatWhere-button")
        button.click()  # Click the button.
        time.sleep(1)

    def changeDistanceFilter(self):
        # within 25 kilometres  : //*[@id="filter-distance"]/button
        # 50                      // *[ @ id = "filter-distance-menu"] / li[6] / a
        time.sleep(2)
        dropList = browser.find_element_by_xpath('//*[@id="filter-distance"]/button')
        dropList.click()  # Click the Distance dropList.
        time.sleep(2)
        selection = browser.find_element_by_xpath('//*[@id="filter-distance-menu"]/li[6]/a')
        selection.click()  # Click the selection of 50 kilometres.
        time.sleep(2)

    def changeSalaryFilter(self):
        # Salary estimate       : //*[@id="filter-salary-estimate"]/button
        # 60,000                  // *[ @ id = "filter-salary-estimate-menu"] / li[2] / a
        time.sleep(2)
        dropList = browser.find_element_by_xpath('//*[@id="filter-salary-estimate"]/button')
        dropList.click()  # Click the Salary dropList.
        time.sleep(2)
        selection = browser.find_element_by_xpath('//*[@id="filter-salary-estimate-menu"]/li[2]/a')
        selection.click()  # Click the selection of $60,000.
        time.sleep(2)

    def changeJobTypeFilter(self):
        # job type              : //*[@id="filter-job-type"]/button
        # Full time               //*[@id="filter-job-type-menu"]/li[1]/a/span[1]
        time.sleep(3)
        dropList = browser.find_element_by_xpath('//*[@id="filter-job-type"]/button')
        dropList.click()  # Click the job type dropList.
        time.sleep(3)
        selection = browser.find_element_by_xpath('//*[@id="filter-job-type-menu"]/li[1]/a/span[1]')
        selection.click()  # Click the selection of Full time.
        time.sleep(3)

    def changeFilters(self):
        # change one or more filters
        time.sleep(1)

        # Temporary un-used because indeed website will return a page to request email
        #self.changeDistanceFilter()
        #self.changeSalaryFilter()
        #self.changeJobTypeFilter()

    def clickNextPage(self):
        # click NextPage
        # resultsCol > nav > div > ul > li:nth-child(3) > a
        # //*[@id="resultsCol"]/nav/div/ul/li[3]/a

        # How many pages could be retrieved is random, normally 2-3 pages,
        # because sometime indeed website will return a popup page to request email
        time.sleep(3)
        try:
            nextPageLink = browser.find_element_by_xpath('//*[@id="resultsCol"]/nav/div/ul/li[3]/a')
            nextPageLink.click()  # Click the nextPageLink.
            return True
        except:
            return False

    def getText(self,htmlStringList):
        result = ""
        for eliment in htmlStringList:
            result = eliment.get_text()
            break
        return result.strip()

    def parseringJob(self, textContent):
        # Beautiful soup removes HTML tags from our content if it exists.
        self.indeedRawData = textContent
        soup = BeautifulSoup(textContent, features="html.parser")
        #rawString = soup.get_text().strip()

        jobTitle = self.getText(soup.select('.title'))
        company = self.getText(soup.select('.company'))
        location = self.getText(soup.select('span[class="location accessible-contrast-color-location"]'))
        salary = self.getText(soup.select('.salaryText'))
        description = self.getText(soup.select('.summary'))
        description = re.sub(r"\n", " ", description)

        job = Job(jobTitle,company,location,salary,description)
        return job

    def showIndeed(self):
        print("indeed RawData:   " + self.indeedRawData)
        print("")


# class definition of Job
# this class contain clean data of job
class Job:
    jobTitle = ""
    company = ""
    location = ""
    salary = ""
    description = ""

    def __init__(self, jobTitle, company, location, salary, description):
        self.jobTitle = jobTitle
        self.company = company
        self.location = location
        self.salary = salary
        self.description = description

    def showJob(self):
        print("Job Title:   " + self.jobTitle)
        print("Company:     " + self.company)
        print("Location:    " + self.location)
        print("Salary:      " + self.salary)
        print("Description: " + self.description)
        print("")


# back to main

# Change to what job you want to search
what = "data analyst"
where = "Vancouver BC"

# list of jobs
jobList = []

# web search and click, methods of class IndeedWeb
jobHunter = IndeedWeb()
jobHunter.search(what, where)
jobHunter.changeFilters()

# hasPage to control if there is a page (used when click next page)
hasPage = True
while hasPage:
    content = browser.find_elements_by_css_selector(".clickcard")

    for e in content:
        try:
            textContent = e.get_attribute('innerHTML')
            # parser web content and return a clean job object of class Job
            job = jobHunter.parseringJob(textContent)
            jobList.append(job)
        except:
            # if fail to parser, there might be indeed return a popup page
            # and request you to input email address, have to end scrape
            hasPage = False
            break

    if hasPage:
        # if clickNextPage fail, hasPage will be False, so end the while loop
        hasPage = jobHunter.clickNextPage()

# show all the jobs in the list
for job in jobList:
    job.showJob()

# put all jobs into a DataFrame
df = pd.DataFrame(columns=['JobTitle','Company','Location','Salary','Description'])
for job in jobList:
    jobDict = { 'JobTitle': job.jobTitle,
                'Company' : job.company,
                'Location': job.location,
                'Salary'  : job.salary,
                'Description': job.description }
    df = df.append(jobDict, ignore_index=True)

# write DataFrame to csv file
df.to_csv('IndeedJobs.csv', index=None)
time.sleep(1)

# read the csv file into a new DataFrame, then show the DataFrame
dfnew = pd.read_csv('IndeedJobs.csv')

print("++++++++++++++++++++++++++++")
print("   Indeed Jobs DataFrame")
print("++++++++++++++++++++++++++++")
print(dfnew.head(2))
print("...")
print(dfnew.tail(2))


'''
-- showJob() result sample --

Job Title:   Budget Financial Analyst
Company:     BC Housing
Location:    Burnaby, BC
Salary:      
Description: Completion of a bachelor degree in accounting or finance, or a bachelor degree in a relevant subject area and completion of an advanced accounting diploma or…

Job Title:   Data Analyst
Company:     Fine Tune Communications (authorized dealer of Cha...
Location:    Richmond, BC
Salary:      $21 - $24 an hour
Description: Expert of data models, data mining, database design, and data visualization.
Develop and test data models to increase data accuracy.

Job Title:   database analyst
Company:     Skynet Wireless Inc
Location:    Langley, BC
Salary:      $31.50 an hour
Description: Operate database management systems to analyze data.
Develop and implement data administration policy, standards and models.

'''


'''
++++++++++++++++++++++++++++
   Indeed Jobs DataFrame
++++++++++++++++++++++++++++
                           JobTitle  ...                                        Description
0  Strategic Pricing & Data Analyst  ...  Analyze data related to return on investment f...
1      Applications Systems Analyst  ...  Reporting to the Director of Development and P...

[2 rows x 5 columns]
...
                                 JobTitle  ...                                        Description
21                     Salesforce Analyst  ...  Deep understanding of dimensional data modelli...
22  Data Visualization Software Developer  ...  ConeTec is seeking a full-time programmer expe...

[2 rows x 5 columns]

'''