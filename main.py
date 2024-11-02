from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#put the access url of your modem here
driver.get("http://192.168.0.1/login.html")

# Enter login password
# replace your modem password with "admin"
driver.find_element(By.ID, "login-password").send_keys("admin")

# Click "Login" button
driver.find_element(By.ID, "save").click()

# Set wait timer to 5 seconds
wait = WebDriverWait(driver, 5)

# wait and check if modem settings is loaded ( "Administration" panel button is shown)
admin_panel = WebDriverWait(driver, 200).until(
    expected_conditions.visibility_of_element_located((By.ID, "sub-menu"))).find_element(By.ID, "system")

#click "Administration" panel
admin_panel.click()

# wait and check if "Administration" panel is loaded ("Reboot" button is shown)
reboot_button = WebDriverWait(driver, 200).until(
    expected_conditions.visibility_of_element_located((By.NAME, "reboot")))

# click "Reboot" button
driver.execute_script("arguments[0].click();", reboot_button)
