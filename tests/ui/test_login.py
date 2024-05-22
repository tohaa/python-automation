import allure
from framework.ui_base_test import UiBaseTest

@allure.feature('Login Page')
class TestLogin(UiBaseTest):

    @allure.story('Open login page')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_open_login_page(self):
        with allure.step('Open login page'):
            self.driver.get('https://example.com/login')
            assert 'Example Domain' in self.driver.title

    @allure.story('Perform login')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_perform_login(self):
        with allure.step('Open login page'):
            self.driver.get('https://example.com/login')

        with allure.step('Enter login credentials'):
            self.driver.find_element_by_id('username').send_keys('your_username')
            self.driver.find_element_by_id('password').send_keys('your_password')
            self.driver.find_element_by_id('loginButton').click()

        with allure.step('Validate login'):
            assert 'Dashboard' in self.driver.title