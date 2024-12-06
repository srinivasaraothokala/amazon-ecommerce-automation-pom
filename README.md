Amazon E-Commerce Automation Using Selenium with Page Object Model (POM)
Overview
This project is a comprehensive automation framework for testing the Amazon e-commerce website. Built using Selenium and Python, it implements the Page Object Model (POM) design pattern, ensuring that the framework is modular, maintainable, and scalable.

Features
Automates testing workflows such as login, product search, and navigation.
Implements Page Object Model (POM) for clear separation of test scripts and page locators.
Captures screenshots of test execution for debugging.
Includes reusable utilities for browser configuration and test setup.
Technologies Used
Programming Language: Python
Testing Tool: Selenium WebDriver
Framework: Pytest
Design Pattern: Page Object Model (POM)
Browser: Google Chrome (using ChromeDriver)
Project Structure
Amazon E-Commerce Automation/
│
├── pages/                 # Contains POM classes for each web page
│   ├── home_page.py       # Amazon home page locators and methods
│   ├── login_page.py      # Amazon login page locators and methods
│
├── tests/                 # Contains test scripts for different scenarios
│   ├── test_login.py      # Test script for login functionality
│   ├── test_search.py     # Test script for product search functionality
│
├── utils/                 # Utility scripts for reusable components
│   ├── browser_config.py  # Browser setup and configuration
│
├── screenshots/           # Stores screenshots captured during test execution
│
├── requirements.txt       # List of required Python libraries
├── README.md              # Documentation for the project
├── .gitignore             # Specifies files and directories to be ignored by Git
├── venv/                  # Python virtual environment (not pushed to Git)
Setup and Installation
Prerequisites
Python 3.12 or above
Google Chrome browser
ChromeDriver (ensure compatibility with your Chrome version)
Steps to Install
Clone the repository:

git clone https://github.com/yourusername/amazon-automation-pom.git
cd amazon-automation-pom
Set up a virtual environment:

python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
Install dependencies:

pip install -r requirements.txt
How to Run the Tests
Run specific test scripts:

pytest tests/test_login.py
pytest tests/test_search.py
Test execution will:

Perform the actions specified in the scripts.
Capture screenshots (if specified) in the screenshots/ folder.
Key Design Details
Page Object Model (POM): Separates web element locators and methods from test scripts for better readability and maintainability.
Scalable Framework: New pages and test cases can be easily added.
Screenshots for Debugging: Screenshots are taken during test failures for troubleshooting.
Sample Code
Home Page POM Example (home_page.py):
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()
Test Case Example (test_search.py):
import pytest
from utils.browser_config import BrowserConfig
from pages.home_page import HomePage

@pytest.fixture(scope="function")
def setup():
    browser = BrowserConfig()
    driver = browser.start_browser()
    yield driver
    driver.quit()

def test_search_product(setup):
    driver = setup
    driver.get("https://www.amazon.com")
    home_page = HomePage(driver)
    home_page.search_product("laptop")
    assert "laptop" in driver.title
Future Enhancements
Add support for additional test scenarios, such as:
Checkout workflows
Wishlist management
Implement logging and reporting.
Integrate Continuous Integration (CI) tools like Jenkins.
Contributing
Contributions are welcome! Feel free to raise issues, suggest improvements, or create pull requests.

Contact
For queries or suggestions, contact:

Name: Srinivasa Rao Thokala
Email: srinivasaraothokala62@gmail.com
