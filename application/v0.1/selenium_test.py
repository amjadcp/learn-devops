import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

class VotingAppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Firefox options for headless mode
        options = Options()
        options.add_argument("--headless")  # Use add_argument for headless mode
        
        # Initialize the WebDriver with the specified options
        cls.driver = webdriver.Firefox(options=options)  # Use Firefox WebDriver
        cls.driver.get("http://localhost:8000")  # URL of your FastAPI app

    def test_vote_candidate1(self):
        # Find the vote button for candidate 1 and click it
        candidate1_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Vote for')]")
        candidate1_button.click()
        
        # Wait for a moment to allow the action to process
        time.sleep(2)

        # Check if the vote was successful (you may need to adjust this based on your response)
        success_message = self.driver.find_element(By.TAG_NAME, "body").text
        # self.assertIn("success", success_message.lower())  # Uncomment this line to check success

    def test_vote_candidate2(self):
        # Reload the page to reset state
        self.driver.get("http://localhost:8000")
        
        # Find the vote button for candidate 2 and click it
        candidate2_button = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Vote for')]")[1]
        candidate2_button.click()
        
        # Wait for a moment to allow the action to process
        time.sleep(2)

        # Check if the vote was successful (you may need to adjust this based on your response)
        success_message = self.driver.find_element(By.TAG_NAME, "body").text
        # self.assertIn("success", success_message.lower())  # Uncomment this line to check success

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
