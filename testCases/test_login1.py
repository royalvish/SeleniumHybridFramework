# Reading data from INI file by readproperties module

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homepageTitle(self, setup):

        self.logger.info("***********Test_001_Login**************")
        self.logger.info("***********Verifying Home Page Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_tilte = self.driver.title

        if actual_tilte == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("*********Home Page Title Test is Failed*********")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("*******DashBoard Title Test is Passed*******")
            assert True
        else:
            assert False
