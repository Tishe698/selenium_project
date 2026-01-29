from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = "http://testshop.qa-practice.com/"
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url is not None:
            self.driver.get(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def hover(self, locator):
        element = self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def send_text(self, locator, text):
        element = self.find(locator)
        element.send_keys(text)
        return element

    def check_title(self, text):
        assert self.driver.title == text

    def wait_for_value(self, locator, expected_value, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value(locator, expected_value)
        )
        element = self.find(locator)
        actual = element.get_attribute("value")
        assert actual == expected_value, f"Expected '{expected_value}', got '{actual}'"
        return element
