from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from orangeHRM.Pages.BasePage import BasePage


class VacanciesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.vacancy_link_id = "menu_recruitment_viewJobVacancy"
        self.vacancy_jt_drp_id = "vacancySearch_jobTitle"
        self.search_btn_id = "btnSrch"
        self.add_vacancy_btn_id = "btnAdd"
        self.add_vacancy_jt_drp_id = "addJobVacancy_jobTitle"
        self.add_vacancy_name_txt_id = "addJobVacancy_name"
        self.add_vacancy_manager_txt_id = "addJobVacancy_hiringManager"
        self.add_vacancy_no_positions_txt_id = "addJobVacancy_noOfPositions"
        self.add_vacancy_description_txt_id = "addJobVacancy_description"
        self.add_vacancy_save_btn_id = "btnSave"

    def click_vacancy(self):
        elem = self.driver.find_element(By.ID, self.vacancy_link_id)
        elem.click()

    def click_vacancy_jt(self):
        elem = self.driver.find_element(By.ID, self.vacancy_jt_drp_id)
        elem.click()

    def select_vacancy_jt(self, jt):
        element = self.driver.find_element(By.ID, self.vacancy_jt_drp_id)
        drp = Select(element)
        drp.select_by_visible_text(jt)

    def click_search(self):
        elem = self.driver.find_element(By.ID, self.search_btn_id)
        elem.click()

    def click_add_vacancy(self):
        elem = self.driver.find_element(By.ID, self.add_vacancy_btn_id)
        elem.click()

    def click_add_vacancy_jt(self):
        elem = self.driver.find_element(By.ID, self.add_vacancy_jt_drp_id)
        elem.click()

    def select_add_vacancy_jt(self, jt):
        elem = self.driver.find_element(By.ID, self.add_vacancy_jt_drp_id)
        drp = Select(elem)
        drp.select_by_visible_text(jt)

    def enter_vacancy_name(self, name):
        elem = self.driver.find_element(By.ID, self.add_vacancy_name_txt_id)
        elem.send_keys(name)

    def enter_hiring_manager(self, manager):
        elem = self.driver.find_element(By.ID, self.add_vacancy_manager_txt_id)
        elem.send_keys(manager)

    def enter_no_positions(self, positions):
        elem = self.driver.find_element(By.ID, self.add_vacancy_no_positions_txt_id)
        elem.send_keys(positions)

    def enter_job_description(self, description):
        elem = self.driver.find_element(By.ID, self.add_vacancy_description_txt_id)
        elem.send_keys(description)

    def click_save(self):
        elem = self.driver.find_element(By.ID, self.add_vacancy_save_btn_id)
        elem.click()


