from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
import numpy as np
import requests
from io import BytesIO

driver = webdriver.Safari()
driver.get("https://www.google.com/recaptcha/api2/demo?authuser=2")
recaptcha_form = driver.find_element(By.ID , "recaptcha-demo")
recaptcha_form.click()

wait = WebDriverWait(driver, 10)

challenge_iframe = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//iframe[@title='recaptcha challenge expires in two minutes']")
))
driver.switch_to.frame(challenge_iframe)

word_element = wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "div.rc-imageselect-desc-no-canonical strong")
))
challenge_word = word_element.text

print("reCAPTCHA asks for:", challenge_word)



grid_table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#rc-imageselect-target table"))
)


class_attr = grid_table.get_attribute("class")


if "rc-imageselect-table-33" in class_attr:
    grid_size = 3
elif "rc-imageselect-table-44" in class_attr:
    grid_size = 4
else:
    print("Unknown grid layout:", class_attr)


first_tile_img = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.rc-imageselect-tile img"))
    )
src = first_tile_img.get_attribute("src")


resp = requests.get(src)
full_img = Image.open(BytesIO(resp.content)).convert("L")  # grayscale

# --- split into grid_size x grid_size ---
width, height = full_img.size
tile_w, tile_h = width // grid_size, height // grid_size

brightness_values = []
idx = 0
idxs = []
for row in range(grid_size):
    for col in range(grid_size):
        idx += 1
        # crop tile
        left, upper = col * tile_w, row * tile_h
        right, lower = left + tile_w, upper + tile_h
        tile = full_img.crop((left, upper, right, lower))

        # compute brightness
        arr = np.array(tile)
        brightness = arr.mean()

        brightness_values.append((idx, brightness))
        print(f"Tile {idx} (row {row}, col {col}): {brightness:.2f}")

trs = grid_table.find_elements(By.TAG_NAME, "tr")

idx = 0
for row_i, tr in enumerate(trs):
    tds = tr.find_elements(By.TAG_NAME, "td")
    for col_i, td in enumerate(tds):
        brightness = brightness_values[idx][1]  # take brightness from array
        print(f"Checking td at row {row_i}, col {col_i} -> brightness {brightness:.2f}")
        if brightness > 100:
            print(f" Clicking td index {idx} (row {row_i}, col {col_i})")
            td.click()
            time.sleep(0.3)  # small delay so it looks human
        idx += 1


driver.switch_to.default_content()

driver.quit()