import socket

if socket.gethostname() != "debian-server":
    import unittest

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from webdriver.chrome import ChromeDriverManager


    def driver_initializer():
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        driver.maximize_window()
        return driver


    class TestSelenium(unittest.TestCase):

        def test_default(self) -> None:
            """"
            Test method to verify if selenium is working properly
            """
            if socket.gethostname() == "debian-server":
                self.assertTrue(True, "Skipped because we are on the server")

            driver = driver_initializer()

            driver.get("http://www.python.org")

            assert "Python" in driver.title

            driver.close()

        def test_user_page(self) -> None:
            """"
            Test method to verify user page is working by checking its title
            """
            if socket.gethostname() == "debian-server":
                self.assertTrue(True, "Skipped because we are on the server")

            driver = driver_initializer()

            driver.get("https//38600.ddns.net:9001/utilisateurs")

            assert "User" in driver.title

            driver.close()

        def test_user_page_group_table(self) -> None:
            """"
            Test method to verify if the group list is working properly
            Here we verify if the size is equal to 2 because this fuctionnality is not yet
            implemented and the page is static
            """
            if socket.gethostname() == "debian-server":
                self.assertTrue(True, "Skipped because we are on the server")

            driver = driver_initializer()

            driver.get("https//38600.ddns.net:9001/utilisateurs")

            table_content = driver.find_elements(By.CLASS_NAME, 'table-responsive')
            assert len(table_content) == 2
            driver.close()

        def test_admin_page_group_table(self) -> None:
            """"
            Test method to verify if the group list is working properly
            Here we verify if the size is equal to 2 because this functionality is not yet
            implemented and the page is static
            """
            if socket.gethostname() == "debian-server":
                self.assertTrue(True, "Skipped because we are on the server")

            driver = driver_initializer()

            driver.get("https//38600.ddns.net:9001/administrateurs")

            assert "Admin" in driver.title

            driver.close()
