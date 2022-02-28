import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fixtures.models.login import LoginData
from fixtures.pages.application import Application
logger = logging.getLogger("test")


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://mail.ru/",
        help="Site's URL",
    ),
    parser.addoption(
        "--email", action="store", default="account_for_test2@bk.ru", help="email",
    ),
    parser.addoption(
        "--password", action="store", default="StrongPassword", help="password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default="true",
        help="enter 'true' if you want run tests in headless mode of browser,\n"
        "enter 'false' - if not",
    ),


@pytest.fixture(scope="session")
def user_data(request):
    email = request.config.getoption("--email")
    password = request.config.getoption("--password")
    return LoginData(email, password)


@pytest.fixture()
def app(request):
    url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    # Driver's options
    chrome_options = Options()
    if headless == "false":
        chrome_options.headless = False
    else:
        chrome_options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    logger.info(f"Start app on {url}")
    app = Application(driver, url)
    yield app
    app.quit()
