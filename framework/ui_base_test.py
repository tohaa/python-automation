import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure
import os


class UiBaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        if request.node.rep_call.failed:
            self._capture_screenshot(request.node.name)
        self.driver.quit()

    def _capture_screenshot(self, name):
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
