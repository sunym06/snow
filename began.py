import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = "com.xueqiu.android.view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

cancel_update = driver.find_element_by_id("com.xueqiu.android:id/image_cancel")
cancel_update = driver.find_element_by_id("com.xueqiu.android:id/image_cancel")
cancel_update.click()

select_bar = driver.find_element_by_xpath('//*[@text="自选"]')
select_bar.click()
time.sleep(3)
TouchAction(driver).tap(x=543, y=896).perform()
print('tap')
snow_bar = driver.find_element_by_xpath('//*[@text="雪球"]')
snow_bar.click()

per_icon = driver.find_element_by_id('user_profile_icon')
per_icon.click()

byPhone = driver.find_element_by_id('iv_login_phone')
byPhone.click()

phone = driver.find_element_by_id('register_phone_number')
phone.send_keys('15801287634')
register = driver.find_element_by_id('register_code')
register.send_keys('1234')
next = driver.find_element_by_id('button_next')
next.click()
sure = driver.find_element_by_id('md_buttonDefaultPositive')
sure.click()

close = driver.find_element_by_id('iv_action_back')
close.click()
leav = driver.find_element_by_id('md_buttonDefaultNegative')
leav.click()

back = driver.find_element_by_id('action_back')
back.click()




time.sleep(5)
driver.quit()