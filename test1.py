from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Chrome(r"C:\Users\jsaidane\PycharmProjects\FirstpythonProject\Drivers\chromedriver.exe")
    driver.get("https://google.com")
    yield
    driver.close()
    print("test completed")
def test_launch(test_setup):
    element = driver.find_element(By.NAME, "q")
    element.send_keys("hello")
    element.send_keys(Keys.ENTER)