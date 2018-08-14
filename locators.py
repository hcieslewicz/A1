from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name


class SearchPageLocators(object):

    LOGO                = (By.CSS_SELECTOR, 'a[data-qa-selector="logo-link"]')
    FILTER_YEAR         = (By.CSS_SELECTOR, 'div[data-qa-selector="filter-year"]')
    FILTER_YEAR_OPTION  = (By.CSS_SELECTOR, 'option[data-qa-selector-value"]')
    FILTER_PRICE_DESC   = (By.CSS_SELECTOR, 'option[data-qa-selector-value="offerPrice.amountMinorUnits.desc"]')
    FILTER_PRICE_ASC    = (By.CSS_SELECTOR, 'option[data-qa-selector-value="offerPrice.amountMinorUnits.asc"]')
    SPEC_LIST           = (By.CSS_SELECTOR, 'ul[data-qa-selector="spec-list"]')
    PRICE               = (By.CSS_SELECTOR, 'div[data-qa-selector="price"]')
    RESULTS_AMOUNT      = (By.CSS_SELECTOR, 'div[data-qa-selector="results-amount"]')
    PAGE_SIZE           = (By.NAME, 'pageSize')
    PAGINATIOM          = (By.CLASS_NAME, 'pagination')
    SEARCH_RESULTS      = (By.CSS_SELECTOR, 'a[data-qa-selector="ad"]')
    #SEARCH_RESULTS_LIST = (By.CSS_SELECTOR, 'div[data-qa-selector="ad-items"]')


class MainPageLocatars(object):
    pass


class LoginPageLocatars(object):
    pass


class SignUpPageLocatars(object):
    pass
