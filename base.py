from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# this Base class is serving basic attributes for every single page inherited from Page class


class Page(object):
    def __init__(self, driver, base_url=''):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def find_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))

    def find_elements(self, *locator):
        return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(locator))

    def find_element_to_be_clickable(self, *locator):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(locator))

    def update_locator(self, value, *locator):
        by, loc = locator
        loc = loc.replace("\"]", "=\"" + str(value) + "\"]")
        return (by, loc)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
