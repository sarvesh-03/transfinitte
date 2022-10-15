
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from models.electoral import ElectoralRequest


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

    father_name = driver.find_element("id", "txtFName")
    father_name.send_keys(request.fname)

    genderSelect = Select(driver.find_element("id","listGender"))
    genderSelect.select_by_visible_text(request.gender)

    StateSelect = Select(driver.find_element("id", "nameStateList"))
    StateSelect.select_by_visible_text(request.state)

    sleep(5)
    DistSelect = Select(driver.find_element("xpath","//select[@ng-model='selectedDistrict']"))
    DistSelect.select_by_visible_text(request.district)
    sleep(5)

    ACSelect = Select(driver.find_element("xpath","//select[@ng-model='selectedAC']"))
    ACSelect.select_by_visible_text(request.ac)

    vid = driver.find_element("id","captchaDetailImg")
    print(driver.current_url)
    screenshot = vid.screenshot_as_png
    return screenshot


def get_cred_details(code:str,driver):
    captcha_text = driver.find_element("id","txtCaptcha")
    captcha_text.send_keys(code)
    search_button = driver.find_element("id","btnDetailsSubmit")
    search_button.click()
    w = WebDriverWait(driver, 10)
    w.until(EC.presence_of_element_located((By.ID,'resultsTable')))
    table = driver.find_element("id","resultsTable")
    rows = table.find_elements(By.TAG_NAME,"tr")
    size = len(rows)
    ac_no = -1
    part_no = -1
    if size > 1:
        view = rows.find_element(By.TAG_NAME,"form")
        ac_view = view.find_element(By.NAME,"ac_no")
        part_view = view.find_element(By.NAME,"part_no")
        ac_no = ac_view.get_attribute("value")
        part_no = part_view.get_attribute("value")
    return [ac_no,part_no]



    