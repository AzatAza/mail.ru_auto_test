from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, app):
        self.app = app

    def custom_find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Cant{locator}",
        )
        return element

    def frame_switch(self, locator):
        WebDriverWait(self.app.driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it(locator))

    def click_element(self, locator, wait_time=10):
        """
        Click_element == click()
        """
        element = self.custom_find_element(locator, wait_time)
        element.click()

    def fill_element(self, data, locator, wait_time=10):
        """
        Fill element == send_keys()
        """
        element = self.custom_find_element(locator, wait_time)
        if data:
            element.send_keys(data)

    def get_text(self, locator, wait_time=10):
        """
        Get element text
        """
        element = self.custom_find_element(locator, wait_time)
        return element.text
