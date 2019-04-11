from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import requests
import os
username = "choco;ati_boy"
url = 'https://instagram.com/'+username
driver = webdriver.Firefox(executable_path="/home/lilaraj/Desktop/geckodriver")


driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
images = soup.find_all(class_="FFVAD")
os.mkdir(username)
for imagescr in images:
    image_url = imagesrc["src"]
    resp = requests.get(image_url)
    print("Downloading", image_url)
    image_data = resp.content
    with open(username+"/"+str(images.index(imagesrc))+".jpg", "wb") as f:
        f.write(image_data)
print("File are downloaded")