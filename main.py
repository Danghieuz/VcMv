import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# --- Cấu hình tối ưu ---
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Chặn ảnh để web load nhẹ, nhập code cho nhanh
chrome_options.add_argument("--blink-settings=imagesEnabled=false") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def get_code():
    # Tạo mã 25 ký tự cực nhanh
    chars = string.ascii_uppercase + string.digits
    return "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])

# --- BƯỚC 1: ĐĂNG NHẬP THỦ CÔNG ---
print("👉 BƯỚC 1: Hãy tự đăng nhập trên cửa sổ Chrome vừa hiện ra.")
driver.get("https://www.minecraft.net/en-us/login")

# Bot sẽ đợi ở đây, không bao giờ tự thoát
input("\nSau khi đã vào đến trang 'Redeem' (trang nhập code), hãy nhấn ENTER tại đây để bắt đầu vã...")

# --- BƯỚC 2: VÃ CODE TỐC ĐỘ CAO ---
print("\n🚀 Đang bắt đầu... Đừng đóng trình duyệt nhé!")

while True:
    try:
        code = get_code()
        
        # Tìm ô nhập bằng CSS Selector cho nhanh
        # Minecraft thường dùng ID có chữ 'redeem-code-input'
        input_el = driver.find_element(By.CSS_SELECTOR, "input[id*='code'], input[type='text']")
        
        # Nhập mã bằng JavaScript (tốc độ ánh sáng, không bị dính mã cũ)
        driver.execute_script(f"arguments[0].value = '{code}';", input_el)
        
        # Tìm và Click nút Submit
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", submit_btn)

        print(f"Thử mã: {code}")
        
        # Thời gian nghỉ: 1.0 giây là mức 'vàng' để không bị khóa IP sớm
        time.sleep(1.0) 

    except Exception as e:
        print("Có lỗi nhỏ, đang load lại trang...")
        driver.get("
