import pytest
from selenium import webdriver


# a = 101


# @pytest.mark.skipif(a > 100, reason="donot want to run")
# segregating the test cases on the basis of tags

@pytest.mark.sanity
def test_registration_validate_001():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
    driver.close()


@pytest.mark.smoke
def test_registration_invalid_002():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
    driver.close()


@pytest.mark.sanity
def test_registration_validate_003():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
    driver.close()


@pytest.mark.smoke
def test_registration_invalid_004():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
    driver.close()
