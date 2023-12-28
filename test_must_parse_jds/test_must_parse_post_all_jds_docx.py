# file: test_login_and_post.py

import pytest
from must_parse_jobssss.post_new_job_file import JobActions
from basic_plan.config_reader import readconfig_file
from unidecode import unidecode

#pytest test_must_parse_post_all_jds_docx.py -k "test_login or test_post_new_job_must_parse_TC010_extreme_test_density" --html=report.html


class TestLoginAndPost:
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

    def test_post_new_job_must_parse_TC008_complex_document_structure(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc008')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        
        
  
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc008_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc008_job_tilte')
        assert job_type == readconfig_file("jds_verification", 'tc008_job_type')
        assert department == readconfig_file("jds_verification", 'tc008_department')
        assert location_type == readconfig_file("jds_verification", 'tc008_location_type')
        assert location == readconfig_file("jds_verification", 'tc008_location')

        job_actions.save_and_exit()

          

          


    def test_post_new_job_must_parse_TC009_Unexpected_Page_Breaks(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc009')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        
  
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc009_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc009_job_tilte')
        assert job_type[0] == readconfig_file("jds_verification", 'tc009_job_type')
        #assert department == readconfig_file("jds_verification", 'tc009_department')
        assert location_type[0] == readconfig_file("jds_verification", 'tc009_location_type')
        assert unidecode(location[0]) == unidecode(readconfig_file("jds_verification", 'tc009_location'))

        job_actions.save_and_exit()


    def test_post_new_job_must_parse_TC010_extreme_test_density(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc010')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        

  
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc010_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc010_job_tilte')
        assert job_type[0] == readconfig_file("jds_verification", 'tc010_job_type')
        #assert department == readconfig_file("jds_verification", 'tc010_department')
        assert location_type[0] == readconfig_file("jds_verification", 'tc010_location_type')
        assert unidecode(location[0]) == unidecode(readconfig_file("jds_verification", 'tc010_location'))

        job_actions.save_and_exit()


    def test_post_new_job_must_parse_TC011_invisible_text(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc011')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
      
  
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc011_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc011_job_tilte')
        assert job_type[0] == readconfig_file("jds_verification", 'tc011_job_type')
        #assert department == readconfig_file("jds_verification", 'tc011_department')
        assert location_type[0] == readconfig_file("jds_verification", 'tc011_location_type')
        assert unidecode(location[0]) == unidecode(readconfig_file("jds_verification", 'tc011_location'))

        job_actions.save_and_exit()



    def test_post_new_job_must_parse_TC012_very_small_font_sizes(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc012')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        
        
  
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc012_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc012_job_tilte')
        assert job_type[0] == readconfig_file("jds_verification", 'tc012_job_type')
        #assert department == readconfig_file("jds_verification", 'tc012_department')
        #assert location_type[0] == readconfig_file("jds_verification", 'tc012_location_type')
        assert unidecode(location[0]) == unidecode(readconfig_file("jds_verification", 'tc012_location'))

        job_actions.save_and_exit()


    def test_post_new_job_must_parse_TC013_complex_tables(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc013')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)

  
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc013_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc013_job_tilte')
        assert job_type[0] == readconfig_file("jds_verification", 'tc013_job_type')
        #assert department == readconfig_file("jds_verification", 'tc013_department')
        assert location_type[0] == readconfig_file("jds_verification", 'tc013_location_type')
        assert unidecode(location[0]) == unidecode(readconfig_file("jds_verification", 'tc013_location'))

        job_actions.save_and_exit()


    def test_post_new_job_must_parse_TC014_with_watermarks(self, driver_setup):
        job_actions = driver_setup

        folder_path_for_must_parse_case = readconfig_file("jds_location", 'docx_tc014')

        must_parse_jd_paths = job_actions.get_file_paths(folder_path_for_must_parse_case)
        
        
        job_actions.post_new_job_must_parse(file_path_exist=True, file_path=str(folder_path_for_must_parse_case))
        company_name = job_actions.get_input_value_by_name('company')
        job_title = job_actions.get_input_value_by_name('position')

        job_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[1]", 'rgb(0, 185, 141)')
        job_type = [element['text'] for element in job_type_elements]

        department_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[2]", 'rgb(0, 185, 141)')
        department = [element['text'] for element in department_elements]

        location_type_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[3]", 'rgb(0, 185, 141)')
        location_type = [element['text'] for element in location_type_elements]

        location_elements = job_actions.extract_highlighted_elements("(//div[@class='w-full compensation-tags flex flex-wrap gap-[6px]'])[4]", 'rgb(0, 185, 141)')
        location = [element['text'] for element in location_elements]


        assert company_name == readconfig_file("jds_verification", 'tc014_company_name')
        assert job_title == readconfig_file("jds_verification", 'tc014_job_tilte')
        assert job_type[0] == readconfig_file("jds_verification", 'tc014_job_type')
        #assert department == readconfig_file("jds_verification", 'tc014_department')
        assert location_type[0] == readconfig_file("jds_verification", 'tc014_location_type')
        assert unidecode(location[0]) == unidecode(readconfig_file("jds_verification", 'tc014_location'))

        job_actions.save_and_exit()