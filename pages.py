from base import Page
from locators import *


class SearchPage(Page):
    def __init__(self, driver):
        self.locator = SearchPageLocators
        super(SearchPage, self).__init__(driver)

    def check_page_loaded(self):
        return True if self.find_element(*self.locator.LOGO) else False

    def filter_by_first_registration(self, filter_year):
        self.find_element(*self.locator.FILTER_YEAR).click()
        self.find_element(*self.update_locator(filter_year, *self.locator.FILTER_YEAR_OPTION)).click()

        return SearchPage(self.driver)

    def sort_by_price(self, sort='descending'):
        if sort == 'descending':
            self.find_element(*self.locator.FILTER_PRICE_DESC).click()
        else:
            self.find_element(*self.locator.FILTER_PRICE_ASC).click()

        return SearchPage(self.driver)

    def get_registration_year(self):
        year_list = self.find_element(*self.locator.SPEC_LIST).find_elements_by_tag_name("li")

        return int(year_list[0].text.encode('ascii', 'ignore').decode('ascii').replace('\u2022', '').strip())

    def get_price(self):
        return int(self.find_element(*self.locator.PRICE).text.split(' ')[0].replace('.', ''))

    def check_results(self, filter_year):
        last_price = 0

        while True:
            for result in self.find_elements(*self.locator.SEARCH_RESULTS):
                registration_year = self.get_registration_year()
                price = self.get_price()

                assert price > 0, "Car price is 0 or below"
                if last_price == 0:
                    last_price = price

                assert registration_year >= filter_year, "Filtered result year is below declared"
                assert price <= last_price, "Descending sorted result price is greater than previous one"
                last_price = price

            pagination_list = self.find_element(*self.locator.PAGINATIOM).find_elements_by_tag_name("li")
            next_button = pagination_list[-2].find_element_by_tag_name('a')
            if not next_button.is_enabled() or "disabled" in next_button.get_attribute("class"):
                break
            else:
                self.open(next_button.get_attribute('href'))
                # next_button.click()
                # I prefer calling Get directly instead of Click, cause of no need of using any time.sleep to have page
                # completely load. This prevents situation when page contains old data, when selenium pase it.

    def is_results_found(self):
        return "No results found." not in self.driver.page_source


class MainPage(Page):
    pass


class LoginPage(Page):
    pass


class SignUpPage(Page):
    pass
