import time
import unittest
import HtmlTestRunner

from orangeHRM.Pages.LoginPage import LoginPage
from orangeHRM.Pages.HomePage import HomePage
from orangeHRM.Pages.CandidatesPage import CandidatesPage
from orangeHRM.qa_settings import BASE_URL

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class CandidateSearch(unittest.TestCase):

    def setUp(self):
        s = Service("/Users/kevinnestico/PycharmProjects/pythonProject/drivers/chromedriver")
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        pass

    def test_candidateSearch(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        home_page = HomePage(driver)
        home_page.click_recruitment()

        candidates_page = CandidatesPage(driver)
        candidates_page.click_candidate_jt()
        candidates_page.select_candidate_jt()
        candidates_page.click_search()
        time.sleep(4)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/kevinnestico/PycharmProjects/pythonProject"
                                                                  "/orangeHRM/Reports"))
