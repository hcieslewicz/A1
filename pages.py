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

    def registration_year(self):
        year_list = self.find_element(*self.locator.SPEC_LIST).find_elements_by_tag_name("li")

        return int(year_list[0].text.encode('ascii', 'ignore').decode('ascii').replace('\u2022', '').strip())

    def price(self):
        return int(self.find_element(*self.locator.PRICE).text.split(' ')[0].replace('.', ''))

    def convert(self, expression):
        try:
            return int(expression[2])
        except:
            pass

        try:
            return eval('self.'+expression[2])
        except:
            return expression[2]

    def check_results(self, expression_list):
        self.last_value = None
        while True:
            for result in self.find_elements(*self.locator.SEARCH_RESULTS):
                for expression in expression_list:
                    # expr_arg1 = eval('self.'+ expression[0])
                    if expression[0] == 'price':
                        expr_arg1 = self.price()
                    elif expression[0] == 'registration_year':
                        expr_arg1 = self.registration_year()
                    else:
                        raise AssertionError("Not valid argument for expression")

                    expr_arg2 = expression[1]

                    if expression[2] == 'last_value':
                        if self.last_value == None:
                            if expression[0] == 'price':
                                self.last_value = self.price()
                            elif expression[0] == 'registration_year':
                                self.last_value = self.registration_year()

                    expr_arg3 = self.convert(expression)
                    condition = eval(str(expr_arg1) + ' ' + expr_arg2 + ' ' + str(expr_arg3))
                    assert condition, "%s is not %s than %s" % (expr_arg1, expr_arg2, expr_arg3)

                    if expression[2] == 'last_value':
                        self.last_value = expr_arg1

            pagination_list = self.find_element(*self.locator.PAGINATIOM).find_elements_by_tag_name("li")
            next_button = pagination_list[-2].find_element_by_tag_name('a')
            if not next_button.is_enabled() or "disabled" in next_button.get_attribute("class"):
                break
            else:
                self.open(next_button.get_attribute('href'))
                #next_button.click()

    def is_results_found(self):
        return "No results found." not in self.driver.page_source


class MainPage(Page):
    pass


class LoginPage(Page):
    pass


class SignUpPage(Page):
    pass
