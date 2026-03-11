```python
# Import modules
import random
import string
import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome (chromedriver phải cùng version Chrome)
service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 20)

# Get characters
uc = string.ascii_uppercase
dg = string.digits

# Open login page
driver.get("https://www.minecraft.net/en-us/login")

print("Login with Microsoft rồi quay lại console")
input("Nhấn ENTER khi login xong...")

os.system('cls')

# click navigation sau khi login
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/div/div/nav/a"))).click()
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/main/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/a"))).click()
    time.sleep(2)
except:
    print("Không tìm thấy nút chuyển trang, có thể layout web đã đổi")

# create random code
def create_code():
    q = random.randint(1, 3)

    if q == 1:
        # XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
        parts = ["".join(random.choice(uc + dg) for _ in range(5)) for _ in range(5)]
        return "-".join(parts)

    elif q == 2:
        # V-XXXXX-XXXXX-XXXXX-XXXXX-XXXXX
        parts = ["".join(random.choice(uc + dg) for _ in range(5)) for _ in range(5)]
        return "V-" + "-".join(parts)

    else:
        # 10 digits
        return "".join(random.choice(dg) for _ in range(10))


# infinite loop
while True:
    try:
        code = create_code()
        print("Trying:", code)

        input_box = wait.until(EC.presence_of_element_located((By.XPATH,
            "/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[1]/div/input"
        )))

        input_box.send_keys(Keys.CONTROL + "a")
        input_box.send_keys(code)

        driver.find_element(By.XPATH,
            "/html/body/div[1]/div/div[3]/div/div[1]/main/div/div/div/div/div[2]/div/div/div/form/div/div[2]/button"
        ).click()

        time.sleep(3)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
```
