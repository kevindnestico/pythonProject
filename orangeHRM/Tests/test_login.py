import time
import unittest
import HtmlTestRunner

from orangeHRM.Pages.LoginPage import LoginPage
from orangeHRM.Pages.HomePage import HomePage
from orangeHRM.qa_settings import BASE_URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class OrangeHRMLogin(unittest.TestCase):

    def setUp(self):
        s = Service("/Users/kevinnestico/PycharmProjects/pythonProject/drivers/chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        pass

    def test_login_one(self):
        driver = self.driver
        self.assertIn("OrangeHRM", driver.title)

        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        assert "Dashboard" in driver.page_source

        home_page = HomePage(driver)
        home_page.click_welcome()
        home_page.click_logout()
        time.sleep(2)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/kevinnestico/PycharmProjects/pythonProject"
                                                                  "/orangeHRM/Reports"))
