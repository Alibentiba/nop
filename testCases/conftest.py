import pytest
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the ChromeDriver executable



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser you want to use: chrome or firefox")


@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
      driver_path = '/usr/local/bin/chromedriver'
      service = Service(driver_path)
      driver = webdriver.Chrome(service=service)
      driver.maximize_window()
      return driver

    elif browser_name == "Edge":
        driver = webdriver.Edge()
        driver.maximize_window()
        return driver

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


def pytest_configure(config):
    config._metadata['Environment'] = 'Test'
    config._metadata['Browser'] = 'Chrome'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    # This is an optional hook provided by the pytest-metadata plugin.
    # If the plugin is not installed, this function will not be called.

    # Modify the metadata here
    if 'Environment' in metadata:
        metadata['Environment'] = 'Prod'
        metadata.pop('java_home', None)
        metadata.pop('Plugins', None)










