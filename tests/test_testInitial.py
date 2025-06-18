import csv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))    

@pytest.mark.smoke
def test_testInitial():
    driver.get("https://www.freerangetesters.com")
    titulo = driver.title
    assert titulo == "Free Range Testers"
    
