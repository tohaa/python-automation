import pytest
from framework.api_client import ApiClient


class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = ApiClient()
