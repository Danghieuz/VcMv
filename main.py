import random
import string
import time
import sys

# Thử import thư viện, nếu thiếu sẽ báo lỗi rõ ràng
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("❌ LỖI: Bạn chưa cài thư viện cần thiết!")
    print("👉 Hãy mở CMD và gõ: pip install selenium webdriver-manager")
    input("\nNhấn Enter để thoát...")
    sys.exit()

def get_code():
    chars = string.ascii_uppercase + string.digits
    return "-".join(["".join(random.choices(chars, k=5)) for _ in range(5)])

def main():
    try:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        # Chặn ảnh để tăng tốc
        chrome_options.add_argument("--blink-settings=imagesEnabled=false") 
        
        print("🚀 Đang khởi tạo trình duyệt... vui lòng đợi...")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Bước đăng nhập thủ công
        driver.get("https://www.minecraft.net/en-us/login")
        print("\n👉 BƯỚC 1: Hãy đăng nhập thủ công trên Chrome.")
        print("👉 BƯỚC 2: Sau khi vào trang nạp code, quay lại đây nhấn Enter.")
        
        input("\nNhấn ENTER tại đây để bắt đầu vã code...")

        print("\n🔥 Đang vã code... nhấn Ctrl+C để dừng.")
        
        while True:
            try:
                code = get_code()
                
                # Dùng CSS Selector (Hiện đại và nhanh nhất)
                # Tìm ô input có thuộc tính id chứa chữ 'code'
                input_el = driver.find_element(By.CSS_SELECTOR, "input[id*='code'], input[type='text']")
                
                # Nhập nhanh bằng Javascript
                driver.execute_script(f"arguments[0].value = '{code}';", input_el)
                
                # Tìm nút Submit
                submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                driver.execute_script("arguments[0].click();", submit_btn)

                print(f"Đã thử: {code}")
                time.sleep(1.2) #
