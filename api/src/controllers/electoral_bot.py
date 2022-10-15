
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from src.models.electoral import ElectoralRequest
from selenium.common.exceptions import StaleElementReferenceException

# class wait_for_text_to_match(object):
#     def __init__(self, locator, pattern):
#         self.locator = locator
#         self.pattern = re.compile(pattern)

#     def __call__(self, driver):
#         try:
#             element_text = EC.find_element(driver, self.locator).text
#             return self.pattern.search(element_text)
#         except StaleElementReferenceException:
#             return False

def get_captcha_bot(request:ElectoralRequest,driver) -> bytes:

    continue_button = driver.find_element("id", "continue")
    continue_button.click()

    user_name = driver.find_element("id", "name1")
    user_name.send_keys(request.name)

    birthdate_checkbox = driver.find_element("id", "radDob")
    birthdate_checkbox.click()

    yearSelect = Select(driver.find_element("id", "yearList"))
    yearSelect.select_by_visible_text(request.year)

    monthSelect = Select(driver.find_element("id", "monthList"))
    monthSelect.select_by_visible_text(request.month)

    daySelect = Select(driver.find_element("id", "dayList"))
    daySelect.select_by_visible_text(request.day)

    # ageSelect = Select(driver.find_element("id","ageList"))
    # ageSelect.select_by_visible_text("23")

    father_name = driver.find_element("id", "txtFName")
    father_name.send_keys(request.fname)

    genderSelect = Select(driver.find_element("id","listGender"))
    genderSelect.select_by_visible_text(request.gender)

    StateSelect = Select(driver.find_element("id", "nameStateList"))
    StateSelect.select_by_visible_text(request.state)

    sleep(2)
    DistSelect = Select(driver.find_element("xpath","//select[@ng-model='selectedDistrict']"))
    DistSelect.select_by_visible_text(request.district)
    sleep(2)

    ACSelect = Select(driver.find_element("xpath","//select[@ng-model='selectedAC']"))
    ACSelect.select_by_visible_text(request.ac)

    vid = driver.find_element("id","captchaDetailImg")
    print(driver.current_url)
    screenshot = vid.screenshot_as_base64
    return screenshot


def get_cred_details(code:str,driver):
    captcha_text = driver.find_element("id","txtCaptcha")
    captcha_text.send_keys(code)
    search_button = driver.find_element("id","btnDetailsSubmit")
    
    
    w = WebDriverWait(driver, 10)
    # w.until(wait_for_text_to_match((By.ID, 'txtCaptcha'),r"^[a-zA-Z0-9]{6,}$"))
    w.until(lambda driver: len(driver.find_element("id","txtCaptcha").get_attribute("value")) >= 6)
    captcha_text.send_keys(Keys.RETURN)
    sleep(1)
    w.until(EC.presence_of_element_located((By.ID,'resultsTable')))
    table = driver.find_element("id","resultsTable")
    rows = table.find_elements(By.CSS_SELECTOR,"input")
    size = len(rows)
    print(size)
    name_set = ["state","district","ac_no","part_no"]
    num_arr = []
    for row in rows:
        nam = row.get_attribute('name')
        if nam in name_set:
            num_arr.append(row.get_attribute('value'))
    return num_arr



    