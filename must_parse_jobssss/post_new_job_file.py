# post_new_job_file.py

import os
import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from basic_plan.config_reader import readconfig_file
from selenium.common.exceptions import NoSuchElementException

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

    def get_input_value_by_name(self, name):
        element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//input[@name='{name}']")))
        return element.get_attribute("value")
    
    def extract_highlighted_elements(self, xpath, target_color):
        container = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        buttons = container.find_elements(By.CSS_SELECTOR, 'button[style*="background"]')
        
        highlighted_elements = []

        for button in buttons:
            background_color = button.get_attribute('style').split('background:')[1].split(';')[0].strip()

            if background_color == target_color:
                element_info = {
                    'text': button.find_element(By.CSS_SELECTOR, 'span').text.strip(),
                }
                highlighted_elements.append(element_info)

        return highlighted_elements
    

    def get_skills_sections(self):
        try:
            # Find all "section-skills" elements
            skills_sections = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "section-skills")))
            
            for skills_section in skills_sections:
                try:
                    # Find the heading element within the current skills section
                    heading_element = skills_section.find_element(By.CSS_SELECTOR, 'input[type="text"][required]')

                    # Extract and print the heading of the current section
                    heading = heading_element.get_attribute("value")
                    print('Heading:', heading)

                    # Find all skill elements within the current skills section
                    skill_elements = skills_section.find_elements(By.CLASS_NAME, "auto-complete-input")

                    # Extract and print the skills within the current section
                    skills = [element.get_attribute("value") for element in skill_elements]
                    print('Skills:', ', '.join(skills))
                    
                except NoSuchElementException:
                    pass
                    
        except NoSuchElementException:
            print("No skills sections found.")

    
    def post_new_job_must_parse(self, file_path_exist=True, file_path=''):
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
            
            time.sleep(3)
            

            
    def save_and_exit(self):
        time.sleep(2)
        if "Parsed" in self.driver.page_source:
            
            save_and_exit = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Review post"]')))
            save_and_exit.click()

            Publish = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="Publish this job"]')))
            Publish.click()

            view = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="View"]')))
            view.click()

            menu = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/div/div[1]/div/div/main/div[1]/div/div[1]/div[2]/button")))

            # Click the button
            menu.click()

            delete_job_element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//li[text()='Delete job']")))

            time.sleep(2)

            # Click the "Edit job" element
            delete_job_element.click()

            confirm_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="custom-modal"]/div/div/div/button[1]')))

            time.sleep(2)
            # Click the "Confirm" button
            confirm_button.click()

            time.sleep(5)

    def get_file_paths(self, folder_path):
      file_paths = []
      if os.path.exists(folder_path) and os.path.isdir(folder_path):
          files = os.listdir(folder_path)
          file_paths = [rf'{folder_path}\{file}' for file in files]
      return file_paths

