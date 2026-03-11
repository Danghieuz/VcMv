import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 1. Cấu hình tối ưu tốc độ
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# Chặn tải ảnh để trang web load nhẹ như bay
chrome_options.add_argument("--blink-settings=imagesEnabled=false") 
chrome_options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Hàm tạo code dùng choices (nhanh hơn choice nhiều lần)
chars = string.ascii_uppercase + string.digits
def get_fast_code(loai):
    if loai == 1:
        return "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])
    elif loai == 2:
        return "V-" + "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])
    else:
        return "".join(random.choices(string.digits, k=10))

# 3. Chạy chương trình
driver.get("https://www.minecraft.net/en-us/redeem")
print("\n--- ĐĂNG NHẬP TRÊN WEB XONG THÌ QUAY LẠI ĐÂY ---")
input("👉 Nhấn Enter để bắt đầu vã code...")

print("\n🚀 ĐANG CHẠY CHẾ ĐỘ TURBO... NHẤN CTRL+C TRONG CMD ĐỂ DỪNG.")

while True:
    try:
        # 1. Tạo mã ngẫu nhiên
        loai = random.randint(1, 3)
        code_fake = get_fast_code(loai)
        
        # 2. Tìm ô nhập bằng CSS Selector (Nhanh nhất trong các loại tìm kiếm)
        # Tìm ô input có ID chứa chữ 'code' hoặc ô input đầu tiên
        input_field = driver.find_element(By.CSS_SELECTOR, "input[id*='code'], input[type='text']")
        
        # 3. DÙNG JAVASCRIPT ĐỂ ĐIỀN CODE (Tốc độ ánh sáng)
        # Cách này không cần CONTROL+A hay BACKSPACE, nó ghi đè thẳng luôn
        driver.execute_script(f"arguments[0].value = '{code_fake}';", input_field)
        
        # 4. Tìm và nhấn nút Submit bằng Javascript
        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        driver.execute_script("arguments[0].click();", submit_btn)
