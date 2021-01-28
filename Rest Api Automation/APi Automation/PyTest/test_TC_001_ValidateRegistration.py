from selenium import webdriver


def test_registration_validate_data():
    driver = webdriver.Chrome(executable_path="D:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get("https://thetestingworld.com/testings")
    driver.maximize_window()
