from selenium import webdriver
from time import sleep
from random import randint

processed = 0
username = ""           # username of the user from which you want clone follower
google_username = ""    # Google ID
google_password = ""    # Google Password

# 1. Browse to Zomato
driver = webdriver.Chrome()
driver.get("https://www.zomato.com/" + username + "/network")
sleep(3)                # Safe Load

# 2. Login using Google
try:
    driver.find_element_by_link_text("Login").click()
    sleep(4)
    driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/section[2]/section/div[1]/div").click()
    sleep(4)
    driver.switch_to_window(driver.window_handles[1])
    sleep(3)
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(google_username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(google_password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
    sleep(8)
except EnvironmentError:
    print("Something went wrong while loading")
    driver.close()
    exit(1)

if len(driver.window_handles) != 1:
    print("ERROR: Google Authentication Failed. Set proper values and try again")
    driver.close()
    exit(1)
else:
    driver.switch_to_window(driver.window_handles[0])
    driver.refresh()
    sleep(3)

# 3. Start Following
for i in range(100):
    follow_list = driver.find_elements_by_id("icon-svg-title-Follow")
    if follow_list:
        for users in follow_list:
            try:
                users.find_element_by_xpath('..').click ()
                sleep(randint(0, 2))
                print("Processed count: " + repr(processed))
                processed += 1
            except:
                continue
    else:
        driver.find_element_by_xpath('//*[@id="root"]/main/div/div[2]/div[2]/section/div/div[3]/div[2]/div/a[6]').click()
        sleep(randint(2, 4))