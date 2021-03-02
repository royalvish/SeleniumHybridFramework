# Reading data from INI file by readproperties module

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time



class Test_001_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Exel: ", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):

            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actual_title = self.driver.title
            print(r)


            if actual_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    assert True
                    self.lp.clickLogout()
                    lst_status.append("Pass")

            elif actual_title != "Dashboard / nopCommerce administration":
                if self.exp == 'Fail':
                    lst_status.append("Pass")

            if "Fail" not in lst_status:
                assert True
                self.driver.close()
            else:
                assert False
                self.driver.close()



