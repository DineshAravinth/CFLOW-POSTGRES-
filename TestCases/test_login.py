import pytest
from PageObjects.LoginPage import LoginPage
from TestCases.conftest import region
from Utilities.readProperties import ReadConfig
from time import sleep

class Test_001_Login:
    url = ReadConfig.getURL(region)

    def test_homepage(self, setup, region):
        driver = setup

        # Read credentials based on region
        url = ReadConfig.getURL(region)
        client_id = ReadConfig.getClientID(region)
        username = ReadConfig.getUsername(region)
        password = ReadConfig.getPassword(region)

        # Open URL and login
        driver.get(url)
        sleep(3)
        lp = LoginPage(driver)
        lp.setClientid(client_id)
        lp.setUserName(username)
        lp.setPassword(password)
        lp.clickLogin()
