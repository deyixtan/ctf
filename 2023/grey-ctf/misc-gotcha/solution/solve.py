
import numpy
import pytesseract
from base64 import b64decode, decodebytes
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from PIL import Image

URL = "http://34.124.157.94:5003"

def get_score_text(driver):
    score_selector = ".container > h3:nth-child(2)"
    return driver.find_element(By.CSS_SELECTOR, score_selector).text.strip()

def get_captcha_image(driver):
    captcha_selector = ".img-fluid"
    elem = driver.find_element(By.CSS_SELECTOR, captcha_selector)
    src = elem.get_attribute("src")
    b64_str = src.split(",")[1]
    buffer = BytesIO(decodebytes(bytes(b64_str, "utf-8")))
    return Image.open(buffer)

def solve_captcha(image):
    return pytesseract.image_to_string(image)[:4].upper()

def send_answer(driver, answer):
    input_selector = "#captch_form"
    submit_selector = ".btn"
    driver.find_element(By.CSS_SELECTOR, input_selector).send_keys(answer)
    driver.find_element(By.CSS_SELECTOR, submit_selector).click()

def solve_questions(driver):
    max_score = "100"
    while True:
        score_text = get_score_text(driver)
        if max_score in score_text:
            break

        captcha_image = get_captcha_image(driver)
        answer = solve_captcha(captcha_image)
        send_answer(driver, answer)
    
if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get(URL)
    solve_questions(driver)
