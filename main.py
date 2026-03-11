import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# --- CẤU HÌNH SIÊU TỐC ---
chrome_options = Options()
chrome_options.add_argument("--headless") # Chạy ẩn hoàn toàn (không hiện cửa sổ)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--blink-settings=imagesEnabled=false") # Chặn tải ảnh để load web cực nhanh
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Profile để bỏ qua bước đăng nhập
path_to_user_data = r"C:\Users\Tên_Máy\AppData\Local\Google\Chrome\User Data" 
chrome_options.add_argument(f"--user-data-dir={path_to_user_data}")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def get_fast_code():
    # Dùng choices nhanh hơn nhiều so với vòng lặp
    chars = string.ascii_uppercase + string.digits
    return "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])

driver.get("https://www.minecraft.net/en-us/redeem")
time.sleep(2) # Chỉ đợi load trang lần đầu

print("🚀 ĐANG CHẠY CHẾ ĐỘ TURBO (ẨN DANH)...")

while True:
    try:
        start_time = time.time() # Tính thời gian mỗi lượt
        
        code = get_fast_code()
        
        # Dùng JavaScript để nhập code (Nhanh hơn send_keys thông thường)
        input_el = driver.find_element(By.CSS_SELECTOR, "input[id*='code']")
        driver.execute_script("arguments[0].value = '';", input_el) # Xóa nhanh
        input_el.send_keys(code)
        
        # Click bằng JavaScript (Bỏ qua việc chờ đợi hoạt họa của nút)
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", submit_btn)
        
        end_time = time.time()
        print(f"✅ Sent: {code} | Speed: {round(end_time - start_time, 2)}s")

        # Microsoft có cơ chế chống spam. Nếu để 0s sẽ bị Block ngay.
        # 0.8s - 1.2s là giới hạn chịu đựng của Server.
        time.sleep(0.8) 
        
    except Exception:
        driver.refresh()
        time.sleep(1)
