from selenium import webdriver
import pytest

@pytest.mark.skip("Donot want to execute this test case in current build")
def test_registration_validate_001():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
    driver.close()


def test_registration_invalid_002():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
    driver.close()
