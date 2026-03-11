import random
import string
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # Thêm cái này
from selenium.webdriver.chrome.options import Options

# Cấu hình để trình duyệt không tự đóng
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Khởi tạo driver (Đảm bảo chromedriver.exe nằm cùng thư mục hoặc đúng đường dẫn)
driver = webdriver.Chrome(options=chrome_options)

uc = string.ascii_uppercase
dg = string.digits

def generate_code(mode):
    if mode == 1: # 5x5
        return "-".join(["".join(random.choice(uc + dg) for _ in range(5)) for _ in range(5)])
    elif mode == 2: # V-5x5
        parts = ["".join(random.choice(uc + dg) for _ in range(5)) for _ in range(5)]
        return "V-" + "-".join(parts)
    else: # 10 digits
        return "".join(random.choice(dg) for _ in range(10))

# --- Bắt đầu chạy ---
driver.get("https://www.minecraft.net/en-us/login")
time.sleep(2)

input("Hãy đăng nhập bằng Microsoft trên trình duyệt, sau đó nhấn Enter tại đây để tiếp tục...")

# Chuyển hướng đến trang redeem (Bạn nên tự copy link redeem dán vào đây cho chắc)
# driver.get("https://www.minecraft.net/en-us/redeem") 

while True: # Sử dụng vòng lặp while thay vì gọi đệ quy
    try:
        q = random.randint(1, 3)
        final_code = generate_code(q)
        print(f"Đang thử code: {final_code}")

        # Tìm ô input (Dùng cú pháp mới By.XPATH)
        # Lưu ý: Xpath của bạn có thể bị thay đổi bởi Minecraft, nếu lỗi hãy kiểm tra lại Xpath
        enter_code = driver.find_element(By.XPATH, "//input[@id='redeem-code-input'] or //input") 
        
        enter_code.send_keys(Keys.CONTROL + 'a')
        enter_code.send_keys(Keys.BACKSPACE)
        enter_code.send_keys(final_code)
        
        # Tìm nút submit và click
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()
        
        time.sleep(3) # Đợi web phản hồi
        
    except Exception as e:
        print(f"Có lỗi xảy ra hoặc không tìm thấy phần tử: {e}")
        time.sleep(5)
        continue # Tiếp tục vòng lặp nếu lỗi
