import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager # Tự động tải driver

# Cấu hình Chrome
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # Giữ trình duyệt không đóng
# chrome_options.add_argument("--user-data-dir=C:\\Users\\Tên_User\\AppData\\Local\\Google\\Chrome\\User Data") # Dùng Profile để đỡ phải login lại

# Khởi tạo Driver tự động (Không cần quan tâm file .exe ở đâu nữa)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def generate_code(mode):
    uc, dg = string.ascii_uppercase, string.digits
    if mode == 1:
        return "-".join(["".join(random.choice(uc + dg) for _ in range(5)) for _ in range(5)])
    elif mode == 2:
        return "V-" + "-".join(["".join(random.choice(uc + dg) for _ in range(5)) for _ in range(5)])
    else:
        return "".join(random.choice(dg) for _ in range(10))

# Truy cập trang
driver.get("https://www.minecraft.net/en-us/redeem")

print("--- VUI LÒNG ĐĂNG NHẬP TRÊN TRÌNH DUYỆT ---")
input("Sau khi đăng nhập xong, nhấn Enter tại đây để bắt đầu treo máy...")

while True:
    try:
        code = generate_code(random.randint(1, 3))
        print(f"Đang thử: {code}")

        # Xpath xịn: Tìm ô input có chứa chữ 'code' trong thuộc tính
        input_field = driver.find_element(By.XPATH, "//input[contains(@id, 'code') or contains(@placeholder, 'code')]")
        
        input_field.send_keys(Keys.CONTROL + 'a')
        input_field.send_keys(Keys.BACKSPACE)
        input_field.send_keys(code)
        
        # Tìm nút bấm Submit/Redeem có chứa text
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit' or contains(., 'Redeem')]")
        submit_btn.click()
        
        time.sleep(4) # Đợi 4 giây để tránh bị Microsoft khóa nhanh quá
        
    except Exception as e:
        print(f"Đang đợi trang load hoặc gặp lỗi: {e}")
        time.sleep(2)
