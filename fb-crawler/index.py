from selenium import webdriver
from time import sleep

SCROLL_PAUSE_TIME = 50

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/groups/712362623017935")

# set cookies
driver.add_cookie({"name":"c_user","domain":".facebook.com","value":"???"})
driver.add_cookie({"name":"xs","domain":".facebook.com","value":"???"})
driver.refresh()

while(True):
    js="window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)
    sleep(SCROLL_PAUSE_TIME)


# driver.get(driver.current_url)
# sleep(2)
# driver.refresh()


# 這邊是取得所有 cookies
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)

# driver.quit()