from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import unittest


class TestSelenium(unittest.TestCase):

    def test_default(self) -> None:
        """"
        Test method to verify if selenium is working properly
        """
        driver = self.driver_intializer()

        driver.get("http://www.python.org")

        assert "Python" in driver.title

        driver.close()

    def test_user_page(self) -> None:
        """"
        Test method to verify user page is working by checking its title
        """
        driver = self.driver_intializer()

        driver.get("http://127.0.0.1:8000/utilisateurs")

        assert "User" in driver.title

        driver.close()

    def test_user_page_group_table(self) -> None:
        """"
        Test method to verify if the group list is working properly
        Here we verify if the size is equal to 2 because this fuctionnality is not yet
        implemented and the page is static
        """
        driver = self.driver_intializer()

        driver.get("http://127.0.0.1:8000/utilisateurs")

        table_content = driver.find_elements(By.CLASS_NAME, 'table-responsive')
        assert len(table_content) == 2
        driver.close()

    def test_admin_page_group_table(self) -> None:
        """"
        Test method to verify if the group list is working properly
        Here we verify if the size is equal to 2 because this functionality is not yet
        implemented and the page is static
        """
        driver = self.driver_intializer()

        driver.get("http://127.0.0.1:8000/administrateurs")

        assert "Admin" in driver.title

        driver.close()


    def driver_intializer(self):
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        return driver
