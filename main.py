from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Hàm nhập code an toàn hơn
def submit_code(driver, code):
    try:
        # Đợi tối đa 10 giây cho đến khi ô nhập xuất hiện (tránh lỗi chưa load xong trang)
        wait = WebDriverWait(driver, 10)
        
        # 1. Tìm ô nhập Code (Sử dụng Xpath thông minh)
        # Cách này tìm bất cứ thẻ input nào có placeholder chứa chữ 'code' hoặc 'Code'
        input_xpath = "//input[contains(@placeholder, 'code') or contains(@placeholder, 'Code') or @id='redeem-code-input']"
        enter_code = wait.until(EC.presence_of_element_located((By.XPATH, input_xpath)))
        
        enter_code.clear() # Xóa sạch ô cũ
        enter_code.send_keys(code)
        
        # 2. Tìm nút bấm Submit/Redeem
        # Tìm nút (button) có chữ 'Redeem' hoặc 'Submit'
        btn_xpath = "//button[contains(text(), 'Redeem') or @type='submit']"
        submit_btn = driver.find_element(By.XPATH, btn_xpath)
        submit_btn.click()
        
        print(f"Đã thử: {code}")
        
    except Exception as e:
        print(f"Lỗi tìm phần tử: {e}")
