import logging

import pytest

logger = logging.getLogger()


class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def before_start(self, request):
        ...
