from seleniumbase import BaseCase
from Locators.ValtechLocators import JobLocations
import requests


class JobLocationsTest(BaseCase):
    def navigate_google(self):
        # Step:1 Navigate to Google's Homepage
        self.get(JobLocations.BaseURL)

        if self.assert_element(JobLocations.GoogleAssert):
            print('Google search bar')

    def search_google(self):
        # Step:2 Type 'Valtech' in the Google Search Bar
        self.type(JobLocations.GoogleSearch, JobLocations.GoogleInput)

        # Select the first option for 'Valtech'
        self.click(JobLocations.ValtechOption)

        if self.assert_element(JobLocations.ValtechAssert):
            print("'Valtech' selected from Google dropdown")

    def open_website(self):
        # Step:3 Open the Valtech Website
        self.click(JobLocations.ValtechLink)

        if self.assert_title('Where Experiences are Engineered'):
            print('Title is visible')
        else:
            print('Title is not visible')

        self.click(JobLocations.Cookies, timeout=4)

        print(self.assert_no_404_errors() is None and 'No 404 errors detected.')

    def navigate_jobs_page(self):
        # Step:4 Navigate to 'Jobs' page through the header
        self.hover_on_element(JobLocations.MenuHover)

        if self.assert_element(JobLocations.HeaderAssert):
            print('The Header is visible')
        else:
            print('The Header is not visible')

        if self.assert_element(JobLocations.JobsButton):
            print("The 'Jobs' Button is visible")
        else:
            print("The 'Jobs' Button is not visible")

        self.click(JobLocations.JobsButton)

    def select_development_dropdown(self):
        # Step:5 Select 'Development' from dropdown
        if self.assert_element(JobLocations.DropDownDepartments, timeout=2):
            print('The Dropdown is visible')

            if self.get_current_url() == JobLocations.ValtechJobPage:
                print('Correct URL for the Jobs page')
            else:
                print(self.get_current_url())

            self.click(JobLocations.DropDownDepartments, timeout=2)

            if self.assert_element(JobLocations.Development):
                self.click(JobLocations.Development)
                print("'Development' is visible")
            else:
                print("'Development' is not visible")

            if self.get_current_url() == JobLocations.ValtechDevelopmentPage:
                print('Correct URL for the Development page')
            else:
                print(self.get_current_url())
        else:
            print('The Departments Dropdown is not visible')
            exit()

    def select_expertise_dropdown(self):
        if self.assert_element(JobLocations.DropDownExpertise):
            print('The Dropdown is visible')

            if self.get_current_url() == JobLocations.ValtechJobPage:
                print('Correct URL for the Jobs page')
            else:
                print(self.get_current_url())

            self.click(JobLocations.DropDownExpertise, timeout=2)

            if self.assert_element(JobLocations.TestQA):
                self.click(JobLocations.TestQA)
                print("'TestQA' is visible")
            else:
                print("'TestQA' is not visible")

            if self.get_current_url() == JobLocations.ValtechDevelopmentPage:
                print('Correct URL for the Development page')
            else:
                print(self.get_current_url())
        else:
            print('The Expertise Dropdown is not visible')
            exit()

    def calculate_open_positions(self):
        dropdown_qa = self.find_elements(JobLocations.DropDownList)
        print(f'There are {len(dropdown_qa)} available positions for QA engineers!')

    def print_locations_from_API(self):
        # Step:7 Count how many open positions are there for 'QA'
        url = 'https://www.valtech.com/link/379b3087e9c04147b68823d1b75a808a.aspx/getjsonresult/'
        response = requests.get(url)

        full_list = response.json()['list']
        total_qa_ads = [x for x in full_list if 'expertiseTestQA' in x['tags']]

        for i in total_qa_ads:
            offices = map(lambda x: x[6:], [k for k in i['tags'] if 'office' in k])
            countries = map(lambda x: x[7:], [k for k in i['tags'] if 'country' in k])
            location = offices if offices else countries if countries else []

            print(f"Job = {i['title']}, Location = {', '.join(location)}")

    def test_valtech_website(self):
        self.navigate_google()
        self.search_google()
        self.open_website()
        self.navigate_jobs_page()
        self.select_development_dropdown()
        self.select_expertise_dropdown()
        self.calculate_open_positions()
        self.print_locations_from_API()
