# file: test_login_and_post.py

import pytest
from empty_post_new_jobssss.empty_post_new_job import JobActions
from basic_plan.config_reader import readconfig_file


#pytest test_empty_post_all_jds_txt.py -k "test_login or test_post_new_job_TC001_empty_file" --html=report.html

class TestLoginAndEmptyPost:
    @pytest.fixture(scope="class")
    def driver_setup(self, request):
        job_actions = JobActions()
        job_actions.setup_driver()
        yield job_actions
        job_actions.teardown_driver()

    def test_login(self, driver_setup):
        job_actions = driver_setup

        # Call login method
        job_actions.login()

    def test_post_new_job_TC001_empty_file(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'txt_tc001')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
  
        job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=str(folder_path_for_empty_case_docx))


    def test_post_new_job_TC005_unicode_characters(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'txt_tc005')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
  
        job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=str(folder_path_for_empty_case_docx))


    def test_post_new_job_TC007_ascii_characters(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_empty_case_docx = readconfig_file("jds_location", 'txt_tc007')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_empty_case_docx)
        
  
        job_actions.post_new_job_empty_field_parse(file_path_exist=True, file_path=str(folder_path_for_empty_case_docx))


    

