import time
import unittest
import HtmlTestRunner

from orangeHRM.Pages.LoginPage import LoginPage
from orangeHRM.Pages.HomePage import HomePage
from orangeHRM.Pages.VacanciesPage import VacanciesPage
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

    def test_vacancySearch(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        home_page = HomePage(driver)
        home_page.click_recruitment()

        vacancies_page = VacanciesPage(driver)
        vacancies_page.click_vacancy()
        vacancies_page.click_vacancy_jt()
        vacancies_page.select_vacancy_jt("Account Assistant")
        vacancies_page.click_search()
        time.sleep(2)
        assert "No results found." not in driver.page_source

    def test_addVacancy(self):
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()

        home_page = HomePage(driver)
        home_page.click_recruitment()

        vacancies_page = VacanciesPage(driver)
        vacancies_page.click_vacancy()
        vacancies_page.click_add_vacancy()
        vacancies_page.click_add_vacancy_jt()
        vacancies_page.select_add_vacancy_jt("Account Assistant")
        vacancies_page.enter_vacancy_name("Jr. Treasury Assistant")
        vacancies_page.enter_hiring_manager("Kevin Mathews")
        vacancies_page.enter_no_positions("3")
        vacancies_page.enter_job_description("Assistant treasurers are responsible for managing and overseeing the "
                                             "financial accounts of their organization, as well as providing global "
                                             "oversight and guidance for all cash-management activities")
        vacancies_page.click_save()
        time.sleep(2)
        assert "Edit" in driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        pass


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/kevinnestico/PycharmProjects/pythonProject"
                                                                  "/orangeHRM/Reports"))
