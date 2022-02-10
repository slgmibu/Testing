from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

# for a full run replace testdata.csv with data.csv
with open("testdata.csv", newline='') as file:
    driver = webdriver.Chrome(service=Service('C:\\WebDriver\\bin\\chromedriver'))
    for index, row in enumerate(csv.reader(file)):
        email = row[0]
        url = row[1]
        print(index, url)
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, "[destination=section-1]").click()
        time.sleep(1)
        driver.find_element(By.ID, "FirstName").send_keys("Charlene TestMkt")
        driver.find_element(By.ID, "LastName").send_keys("Bulovic TestMkt")
        driver.find_element(By.ID, "EmailAddress").send_keys(email)
        driver.find_element(By.ID, "Phone").send_keys("4045121521")
        driver.find_element(By.CSS_SELECTOR, 'option[value="Female"]').click()
        driver.find_element(By.CSS_SELECTOR, "[destination=section-2]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'option[value="yu"]').click()
        driver.find_element(By.CSS_SELECTOR, "[destination=section-3]").click()
        time.sleep(1)
        driver.find_element(By.ID, "JobTitlePosition").send_keys("director")
        driver.find_element(By.CSS_SELECTOR, "[destination=section-4]").click()
        time.sleep(1)
        driver.find_element(By.NAME, "CompanyNameOrganization").send_keys("AARP")
        driver.find_element(By.NAME, "NumberDirectReports").send_keys("25+")
        driver.find_element(By.CSS_SELECTOR, "[destination=section-5]").click()
        time.sleep(1)
        driver.find_element(By.NAME, "HighestDegreeEarned").send_keys("Masters")
        driver.find_element(By.NAME, "YearsOfExperience").send_keys("20+")
        driver.find_element(By.CSS_SELECTOR, "[destination=section-6]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[destination=section-7]").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "button.section-button.submit").click()
