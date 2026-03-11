import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 1. Cấu hình Tối ưu tốc độ
chrome_options = Options()
# Nếu muốn chạy ẩn (không hiện cửa sổ Chrome) để cực nhanh, hãy bỏ dấu # dòng dưới:
# chrome_options.add_argument("--headless") 

chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# QUAN TRỌNG: Sửa đường dẫn Profile của bạn vào đây để tự Login
path_to_user_data = r"C:\Users\Tên_Máy\AppData\Local\Google\Chrome\User Data" 
chrome_options.add_argument(f"--user-data-dir={path_to_user_data}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def get_25_chars():
    chars = string.ascii_uppercase + string.digits
    # Tạo mã 25 ký tự siêu tốc
    return "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])

# Vào thẳng trang nhập code
driver.get("https://www.minecraft.net/en-us/redeem")

# Đợi 2 giây cho trang load lần đầu
time.sleep(2)

print("--- ĐANG BẮT ĐẦU VÃ CODE TỐC ĐỘ CAO ---")

while True:
    try:
        code = get_25_chars()
        
        # Tìm ô nhập (Dùng Xpath ngắn nhất để tăng tốc)
        input_field = driver.find_element(By.CSS_SELECTOR, "input[id*='code']")
        
        # Xóa và nhập cực nhanh
        input_field.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        input_field.send_keys(code)
        
        # Click nút Submit
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        print(f"Sent: {code}")

        # Tốc độ phản hồi của Server Microsoft khoảng 1-2s. 
        # Để dưới 1s dễ bị "Access Denied" (Bị chặn IP tạm thời)
        time.sleep(1.5) 
        
    except Exception:
        # Nếu lỗi (do load chậm) thì reload lại trang và tiếp tục
        driver.refresh()
        time.sleep(2)
