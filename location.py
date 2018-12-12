from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import qrcode

loc = raw_input('Enter your precise location to search :')

driver = webdriver.Firefox()
driver.get("https://www.google.co.in/maps")
assert "Google Maps" in driver.title
searchBoxInput = driver.find_element(By.ID, "searchboxinput")
searchBoxInput.send_keys(loc)
searchBoxInput.send_keys(Keys.RETURN)
#webDriverWait = WebDriverWait(driver, 120)
#webDriverWait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'SHARE')]")))
raw_input("Press Enter only if you are sure about location and you see SHARE button else it will not work : ")
divShare = driver.find_element(By.XPATH, "//div[contains(text(),'SHARE')]")
share =  divShare.find_element_by_xpath("..")
share.click()
webDriverWait = WebDriverWait(driver, 380)
webDriverWait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'section-copy-link-input')]")))
link = driver.find_element(By.XPATH, "//input[contains(@class, 'section-copy-link-input')]")
googleLink = link.get_attribute("value")
qr = qrcode.QRCode(
    version= None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(googleLink)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('location.png')
assert "No results found." not in driver.page_source
driver.close()
