from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import math


class Followers:
    def __init__(self, browser, topics):
        self.browser = browser
        self.topics = topics
        
    def getFollowers(self):
        for topic in self.topics:
            self.browser.get('https://www.instagram.com/explore/tags/' + topic)
            sleep(1)
            
            self.followPeoples()
            
    def followPeoples(self):
        firstImage = self.browser.find_element_by_css_selector(".v1Nh3 a")
        firstImage.click()
        sleep(2)
        
        likesButton = self.browser.find_element_by_css_selector('.Nm9Fw button.sqdOP')
        likesButton.click()
        
        size = 160/len(self.topics)
        size = math.floor(size)
        
        for x in range(size):
            try:
                followButton = self.browser.find_element_by_xpath("//button[text()='Seguir']")
                followButton.click()
            except WebDriverException:
                sleep(1)
                cancelButton = self.browser.find_element_by_css_selector("button.aOOlW.HoLwm")
                cancelButton.click()
            sleep(1)
                

