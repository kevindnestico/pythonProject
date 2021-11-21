from selenium.webdriver.common.by import By
from orangeHRM.Pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.welcome_link_id = "welcome"
        self.logout_partial_link_id = "Logout"
        self.recruitment_link_id = "menu_recruitment_viewRecruitmentModule"

    def click_welcome(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, self.logout_partial_link_id).click()

    def click_recruitment(self):
        self.driver.find_element(By.ID, self.recruitment_link_id).click()
