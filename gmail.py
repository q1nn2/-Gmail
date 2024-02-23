import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestGmailLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.gmail.com")

    def test_gmail_login(self):
        # Enter your email and password
        email = "your_email@gmail.com"
        password = "your_password"

        # Find the e-mail input field
        email_field = self.driver.find_element_by_id("identifierId")
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)

        # Find the password field and enter the password
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

        # Check that we have successfully logged into the mail (you can add other checks)
        self.assertTrue("inbox" in self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
