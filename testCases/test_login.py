import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_tilte = self.driver.title

        if actual_tilte == "Your store. Login":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
