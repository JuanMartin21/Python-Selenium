from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
    SEND_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")

    def navigate_sandbox(self):
        self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing/")
        


    def click_send(self):
        self.click(self.SEND_BUTTON)

    
    