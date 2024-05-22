import allure
from framework.base_test import BaseTest


@allure.feature('User API')
class TestUsers(BaseTest):

    @allure.story('Get all users')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_users(self):
        with allure.step('Sending GET request to fetch all users'):
            response = self.client.get('users')

        with allure.step('Validating the response'):
            assert len(response) > 0
            assert response[0]['id'] == 1

    @allure.story('Create a new user')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user(self):
        new_user = {
            "name": "John Doe",
            "username": "johndoe",
            "email": "johndoe@example.com"
        }

        with allure.step('Sending POST request to create a new user'):
            response = self.client.post('users', data=new_user)