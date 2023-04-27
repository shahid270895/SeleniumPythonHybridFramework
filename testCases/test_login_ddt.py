import time

import pytest
from selenium import webdriver
from webdrivermanager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import xlUtils


class Test_002_DDT_Login:
    path = ".//testData/LoginData.xlsx"
    baseURL = ReadConfig.getAppURL()

    logger = LogGen.loggen()

    def test_ddt_login(self, setup):
        self.logger.info("---------------------Test_002_DDT_Login-------------------------")
        self.logger.info("--------------------Verifying DDT Login test---------------------")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows = xlUtils.getRowCount(self.path,'Sheet1')
        print("No. of rows : ", self.rows)

        lst_status = []

        for r in range(2,self.rows+1):
            self.user = xlUtils.readData(self.path,'Sheet1', r, 1)
            self.password = xlUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = xlUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.enterUserName(self.user)
            self.logger.info("--------------------Entered username---------------------")
            self.lp.enterPassword(self.password)
            self.logger.info("--------------------Entered password---------------------")
            self.lp.clickLoginBtn()
            time.sleep(5)
            self.logger.info("--------------------Clicked on login button---------------------")
            actualTitle=self.driver.title
            if actualTitle == "Dashboard / nopCommerce administration":
                if self.exp == 'pass':
                    self.logger.info("--------------------Clicked on logout button---------------------")
                    self.lp.clickLogoutBtn()
                    lst_status.append("pass")
                elif self.exp == 'fail':
                    self.logger.info("--------------------Clicked on logout button---------------------")
                    self.lp.clickLogoutBtn()
                    lst_status.append("fail")

            elif actualTitle != "Dashboard / nopCommerce administration":
                if self.exp == 'pass':
                    lst_status.append("fail")
                elif self.exp == 'fail':
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("--------------------DDT Login test is passed---------------------")
            self.driver.close()
            assert True
        else:
            self.logger.info("--------------------DDT Login test is failed---------------------")
            self.driver.close()
            assert False

        self.logger.info("----------------------Completed TC_002_DDT_Login----------------------")

