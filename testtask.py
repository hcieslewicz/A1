import unittest
from selenium import webdriver
from pages import *
from testcases import test_cases
from selenium.webdriver.firefox.options import Options


class TestPages(unittest.TestCase):
    def setUp(self):

        options = Options()
        #options.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.maximize_window()

        self.driver.get("https://www.autohero.com/de/search/")
        self.driver.implicitly_wait(2)

    def test_a_page_load(self):
        print "\n" + str(test_cases(0))
        page = SearchPage(self.driver)
        self.assertTrue(page.check_page_loaded())

    def test_filter_by_registration_date_and_sort(self):
        print "\n" + str(test_cases(1))
        filter_year = 2015
        search_page = SearchPage(self.driver)
        search_page.filter_by_first_registration(filter_year)
        search_page.sort_by_price('descending')
        assert search_page.is_results_found(), "No results found."

        exp_list = [
            ('registration_year',  '>=',  '2012'),
            ('price',  '<=',  'last_value')
        ]
        search_page.check_results(exp_list)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=5).run(suite)
