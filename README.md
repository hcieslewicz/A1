# A1 automation

This project provide example of automation of web testing using selenium, python and Firefox browser.

## Getting Started

Get the copy of this example using git:
```
git clone https://github.com/hcieslewicz/A1.git
```


### Prerequisites

To have it running You need to have:
* Python 2.7 - https://www.python.org/
* Selenium - You can download Python bindings for Selenium from the PyPI page for selenium [package](https://pypi.python.org/pypi/selenium). Better way is to get it use [pip](https://pip.pypa.io/en/latest/installing/) to install the selenium package. Using pip, you can install selenium like this:
```
pip install selenium
```
You can download Python bindings for Selenium from the PyPI page for selenium [package](https://pypi.python.org/pypi/selenium). 
* Firefox - https://github.com/mozilla/geckodriver/releases. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

## Running the tests

To run the test You have to call python with the main test scrypt. On Windows open command prompt and type:

```
python.exe testtask.py
```

## Test examples
In this projects there are two test:
* test_a_page_load - this test check, if the search page was opened and and proper logo is present on the page. The purpose of it, is to check, if the page is accessible. This is really basic test and should be executed before other tests.
* test_filter_by_registration_date_and_sort - this test check simple filtering and sorting by going threw those steps:
  - go to search page,
  - filter results by first registration date (required is 2015 and later ),
  - sort results by price (descending),
  - check if all results are correct (all registrations year is above declared and all results are sorted by price descending, including all search page results).

## Authors

* **Hubert Cieslewicz** (https://github.com/hcieslewicz)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
