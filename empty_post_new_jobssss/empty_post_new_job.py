# post_new_job_file.py

import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from basic_plan.config_reader import readconfig_file

class JobActions:
    def __init__(self):
        self.driver = None

    def setup_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_driver(self):
        self.driver.quit()

    def login(self):
        wait = WebDriverWait(self.driver, 10)

        self.driver.get(readconfig_file("Links", 'google_url'))
        self.driver.get(readconfig_file("Links", 'Login_Url'))

        email_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-full:nth-child(4)")))
        email_element.click()

        send_email_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".w-full:nth-child(4)")))
        send_email_element.send_keys(readconfig_file("Login_Credentials", 'Login_username'))

        password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".border:nth-child(1)")))
        password_element.click()

        send_password_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".border:nth-child(1)")))
        send_password_element.send_keys(readconfig_file("Login_Credentials", 'Login_password'))

        show_password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".absolute > svg")))
        show_password.click()

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary")))
        login_button.click()

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,\'Post new job\')]")))

    def post_new_job_empty_field_parse(self, file_path_exist=True, file_path=''):
        self.driver.get(readconfig_file("Links", 'Home_page'))

        # Select the element by its text content
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[text()="Post new job"]'))
        )
        element.click()

        upload = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "upload-document-first-state")))
        upload.click()

        if file_path_exist:
            time.sleep(2)
            pyautogui.write(file_path)
            pyautogui.press("enter")

            wait = WebDriverWait(self.driver, 80)
            autofill_button = wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[@type='button']/span[text()='Click to autofill']"))
            )

            document_name_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "uper-text")))
            document_name = document_name_element.text

            click_to_fill = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='button']/span[text()='Click to autofill']")))
            click_to_fill.click()

            autofill_button = WebDriverWait(self.driver, 310).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[@type='button']/span[text()='Parsed']")))

            if "Parsed" in autofill_button.text:
                company_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search here"][name="company"]')))

                job_title_input =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][name="position"]')))

                job_description_input_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '(//div[@class="editor-class rdw-editor-main"])[2]')))

                time.sleep(2)
                job_description_input_element.click()

                # Your conditions
                condition2 = company_name_input.get_attribute('value') == ''
                condition3 = job_title_input.get_attribute('value') == ''
                condition1 = not job_description_input_element.text.strip()

                # Asserting that all conditions are true
                assert condition1 and condition2 and condition3, "Assertion failed: Conditions not met"




    def get_file_paths(self, folder_path):
      file_paths = []
      if os.path.exists(folder_path) and os.path.isdir(folder_path):
          files = os.listdir(folder_path)
          file_paths = [rf'{folder_path}\{file}' for file in files]
      return file_paths

