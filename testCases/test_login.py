import pytest
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getAppURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("--------------------Test_001_Login---------------------")
        self.logger.info("--------------------Verifying Home Page Title test---------------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        actualTitle=self.driver.title
        if actualTitle=="Your store. Login1":
            assert True
            self.driver.close()
            self.logger.info("--------------------Home Page Title is passed---------------------")
        else:
            self.driver.save_screenshot(".\\screenShots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("--------------------Home Page Title is failed---------------------")
            assert False

    def test_login(self, setup):
        self.logger.info("--------------------Verifying Login test---------------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.enterUserName(self.username)
        self.logger.info("--------------------Entered username---------------------")
        self.lp.enterPassword(self.password)
        self.logger.info("--------------------Entered password---------------------")
        self.lp.clickLoginBtn()
        self.logger.info("--------------------Clicked on login button---------------------")
        actualTitle=self.driver.title
        if actualTitle=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("--------------------Login test is passed---------------------")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("--------------------Login test is failed---------------------")
            assert False

