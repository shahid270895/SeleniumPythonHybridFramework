from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@id='Email']"
    textbox_password_xpath = "//input[@id='Password']"
    button_login_xpath = "//button[@class='button-1 login-button']"
    button_logout_xpath = "//li//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def clickLoginBtn(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickLogoutBtn(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()
