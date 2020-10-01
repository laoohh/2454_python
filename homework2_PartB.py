# this code try to crape finance.yahoo.com for a stock index data 'SP500' to draw chart

import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import matplotlib.pyplot as plt

# driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "C:/Users/Hwang/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe"
URL = "https://finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC"

browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(5)


class YahooFinance:
    onelineData=[]

    def parseringData(self, textContent):
        # Beautiful soup removes HTML tags from our content if it exists.
        self.indeedRawData = textContent
        soup = BeautifulSoup(textContent, features="html.parser")
        #rawString = soup.get_text().strip()

        self.onelineData = []
        htmlStringList = soup.select('td')
        for eliment in htmlStringList:
            elimentText = eliment.get_text().strip()
            elimentText = re.sub(",", "", elimentText)
            self.onelineData.append(elimentText)

        #print(self.onelineData)


# back to main
# put all jobs into a DataFrame
df = pd.DataFrame(columns=['Date','Close'])

for line in range(1,200):
    onelineXPATH = '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(line)+']'
    content = browser.find_elements_by_xpath(onelineXPATH)

    eventList=[]
    for e in content:
        textContent = e.get_attribute('innerHTML')
        # parser web content
        data = YahooFinance()
        data.parseringData(textContent)
        stockData = {'Date': data.onelineData[0],
                     'Close': float(data.onelineData[5])  }
        df = df.append(stockData, ignore_index=True)

# calculate the rolling mean
df['MA30'] = df['Close'].rolling(30).mean()
df['MA10'] = df['Close'].rolling(10).mean()
print(df)

# plot the Close price and moving averages
plt.figure(figsize=(12, 8))
df['Close'].plot(label='Close')
df['MA10'].plot(label='MA10')
df['MA30'].plot(label='MA30')
plt.legend()
plt.ylabel("Adjusted Close")
plt.title('New York Stock Market SP500 Index Daily Chart')
plt.show()


