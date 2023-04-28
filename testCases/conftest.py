from datetime import datetime
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager, IEDriverManager


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    elif browser == 'edge':
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path=IEDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)
    else:
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(45)

    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# @pytest.mark.hookwrapper(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#
#     timestamp = datetime.now().strftime('%H-%M-%S')
#
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#
#         #feature_request = item.funcargs['request']
#
#         #driver = feature_request.getfuncargvalue('browser')
#         #driver.save_screenshot('./screenShots/scr'+timestamp+'.png')
#
#         #extra.append(pytest_html.extras.image('D:/report/scr'+timestamp+'.png'))
#
#         # always add url to report
#         #extra.append(pytest_html.extras.url('http://www.example.com/'))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#             #extra.append(pytest_html.extras.image('D:/report/scr.png'))
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra


def pytest_html_report_title(report):
    report.title = "Automation_Report"


def capture_screenshot(name):
    driver.get_screenshot_as_file(name)


#######################pytest html report ###########################
# it hooks for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Shahid Aftab'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
