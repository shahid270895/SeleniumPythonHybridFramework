import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    elif browser=='edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    elif browser=='ie':
        driver = webdriver.Ie(IEDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure (config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Shahid Aftab'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
