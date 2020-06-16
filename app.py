from time import sleep
from selenium import webdriver
from pprint import pprint
import os

from classes.login import Login
from classes.followers import Followers

browser = webdriver.Chrome(executable_path=os.path.abspath('./driver/chromedriver.exe'))

login = Login(browser)
login.doLogin()

topics = [
    'moda',
    'modaebeleza'
]

followers = Followers(browser, topics)
followers.getFollowers()

browser.close()
