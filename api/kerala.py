from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://www.ceo.kerala.gov.in/electoralrolls.html")
user_id = driver.find_element("id","distNo")
user_id.send_keys("1")
password = driver.find_element("id","lacNo")
password.send_keys("1")
submit = driver.find_element("id","listCmd")
submit.click()
table_id =  driver.find_element("id", 'lst_datatable_acparts')
sleep(1)
rows = table_id.find_elements(By.TAG_NAME, "tr") 
link = rows[1].find_elements(By.TAG_NAME, "td")[3]
print(link.text)
a=link.find_element(By.TAG_NAME,"a")
driver.get(a.get_attribute("href"))
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
sleep(5)
download = driver.find_element("id","downloadRollPdf")
download.click()