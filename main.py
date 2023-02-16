import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
email = str("ahmlamer@mun.ca") # ahmlamer@mun.ca
password = str("monny4lifeLL") # monny4lifeLL



driver = webdriver.Chrome(r'C:\Users\ahmla\OneDrive\Desktop\MUN\projects\leChcker\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('https://crm.stuaff.mun.ca/myAccount/career/postings.htm');
login = driver.find_element(By.XPATH , "/html/body/div[3]/div/div/div[3]/div/div/p[1]/a")
login.click()
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)

password_field.send_keys(Keys.ENTER)

dropDwn = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/div/div/button")
dropDwn.click()

time.sleep(1)

careerCenter = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[3]/div[1]/nav/ul/li[2]/a")
careerCenter.click()
#
# dropDwn = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[4]/div/div/button")
# dropDwn.click()

time.sleep(0.5)

jobPosting = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/table/tbody/tr[1]/td[1]/a[1]/img")
jobPosting.click()

time.sleep(0.5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(0.5)

careerJobs = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div[3]/div[1]/div/div[2]/div/div/div/div/table[1]/tbody/tr/td[2]/a")
careerJobs.click()


num = 1
for i in range(101):
    try:
        driver.switch_to.window(driver.window_handles[1])
        job = driver.find_element(By.XPATH, ("/html/body/main/div[2]/div/div/div/div/div/div/div[2]/div[3]/table/tbody/tr[" + str(num) + "]/td[1]/a"))
        job.click()
        num+= 1
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        time.sleep(1)
    except:
        break



time.sleep(1000) # Let the user actually see something!
time.sleep(1000) # Let the user actually see something!
driver.quit()