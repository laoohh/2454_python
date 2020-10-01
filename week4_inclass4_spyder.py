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
