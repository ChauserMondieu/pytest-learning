import pytest


class MyPlugin:
    def pytest_sessionfinish(self):
        import allure
        allure.title("we import allure")
        print("allure test run reporting finished")


pytest.main(["-s", "-v", "../test"], plugins=[MyPlugin()])

