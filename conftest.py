import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en')


# @pytest.fixture(scope="function")
@pytest.fixture()
def browser(request):
    print("\nstart browser for test..")
    language = request.config.getoption("language")
    options.set_preference("intl.accept_languages", language)

    browser = webdriver.Firefox(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
