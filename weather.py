from bs4 import BeautifulSoup
import requests
import selenium.webdriver as webdriver
driver = webdriver.Firefox(executable_path="/home/lilaraj/Desktop/geckodriver")

class Instagram:
    def get_page(self,user_name):
        try:
            driver.get("https://www.instagram.com/"+user_name)
            soup = BaseException(driver.page_source,)
        
        except Exception as ex:
            print("Failed to get instgram account")
            r = None
        return r
instaobj = Instagram()
username = "saurav_mgr"
page_resp = instaobj.get_page(username)
print("status code" , page_resp.status_code)
#print("text :",page_resp.text)
