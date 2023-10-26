
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

with open('pending_follow_requests.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'html.parser')
instagram_profile_links = soup.find_all('a', {'target': '_blank'})
usernames = [link.text for link in instagram_profile_links]

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())
driver.get('https://www.instagram.com/')
time.sleep(2)

username = 'YOUR_INSTAGRAM_USERNAME_HERE'
password = 'YOUR_INSTAGRAM_PASSWORD_HERE'
username_input = driver.find_element(By.CSS_SELECTOR,"input[name='username']" )
password_input = driver.find_element(By.CSS_SELECTOR,"input[name='password']" )

username_input.send_keys(username)
password_input.send_keys(password)


login_button = driver.find_element(By.XPATH , "//button[@type='submit']")
login_button.click()
time.sleep(5)


for username in usernames:
    print(username, end='')
    driver.get(f'https://instagram.com/{username}/')
    time.sleep(5)
    requested_button = driver.find_element(By.XPATH , "//button[@type='button']")
    requested_button.click()
    time.sleep(2)
    confirm_button = driver.find_element(By.CLASS_NAME, '_a9--')
    confirm_button.click()
    time.sleep(2)