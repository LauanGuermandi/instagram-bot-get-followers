from time import sleep
from selenium import webdriver
from pprint import pprint
import os

from classes.config import Config

class Login:
    def __init__(self, browser):
        self.browser = browser 
        self.cfg = Config()
        if not self.cfg.username:
            exit()

    def doLogin(self):
        self.browser.implicitly_wait(2)
        self.browser.get('https://www.instagram.com/')

        sleep(0)

        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(self.cfg.username)
        password_input.send_keys(self.cfg.password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(2)
        
        goLink = self.browser.find_element_by_xpath("//button[text()='Salvar informações']")
        goLink.click()
        sleep(2)
        
        goLink = self.browser.find_element_by_xpath("//button[text()='Ativar']")
        goLink.click()
        sleep(2)
