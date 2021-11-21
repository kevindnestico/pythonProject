from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from orangeHRM.Pages.BasePage import BasePage


class CandidatesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.candidate_jt_drp_id = "candidateSearch_jobTitle"
        self.search_btn_id = "btnSrch"

    def click_candidate_jt(self):
        self.driver.find_element(By.ID, self.candidate_jt_drp_id).click()

    def select_candidate_jt(self):
        element = self.driver.find_element(By.ID, self.candidate_jt_drp_id)
        drp = Select(element)
        drp.select_by_visible_text("Account Assistant")

    def click_search(self):
        self.driver.find_element(By.ID, self.search_btn_id).click()
