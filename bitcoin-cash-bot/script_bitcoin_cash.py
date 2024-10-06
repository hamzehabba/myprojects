from appium import webdriver
import time

# تنظیمات برای اتصال به شبیه‌ساز یا دستگاه
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',  # یا نام دستگاه فیزیکی
    'appPackage': 'com.bitcoin.cashgiveaway',  # مثال: نام بسته اپلیکیشن
    'appActivity': 'com.bitcoin.cashgiveaway.MainActivity',  # فعالیت اصلی اپلیکیشن
    'noReset': True,
}

# اتصال به Appium
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# صبر برای باز شدن اپلیکیشن
time.sleep(5)

# پیدا کردن و کلیک روی دکمه "Claim" یا هر دکمه دیگر
claim_button = driver.find_element_by_id('com.bitcoin.cashgiveaway:id/claim_button')
claim_button.click()

# صبر برای انجام عملیات
time.sleep(5)

# بستن درایور
driver.quit()
