import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# Đã tắt headless để bạn nhìn thấy cửa sổ
chrome_options.add_experimental_option("detach", True) 
chrome_options.add_argument("--blink-settings=imagesEnabled=false") # Vẫn chặn ảnh để nhanh

# QUAN TRỌNG: Đóng Chrome trước khi chạy dòng này
path_to_user_data = r"C:\Users\Tên_Máy\AppData\Local\Google\Chrome\User Data" 
chrome_options.add_argument(f"--user-data-dir={path_to_user_data}")

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.minecraft.net/en-us/redeem")
    
    print("🚀 Đang chạy... Nếu thấy cửa sổ Chrome hiện lên là thành công!")
    
    while True:
        chars = string.ascii_uppercase + string.digits
        code = "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])
        
        # Nhập code bằng Javascript (Siêu nhanh)
        input_el = driver.find_element(By.CSS_SELECTOR, "input[id*='code']")
        driver.execute_script(f"arguments[0].value = '{code}';", input_el)
        
        # Click Submit
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", submit_btn)
        
        print(f"Đã thử: {code}")
        time.sleep(1.2) # Giữ tốc độ an toàn

except Exception as e:
    print(f"❌ LỖI RỒI: {e}")
    input("Nhấn Enter để thoát...") # Giữ cửa sổ CMD không bị mất để bạn đọc lỗi
