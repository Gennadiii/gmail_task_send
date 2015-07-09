from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep
from datetime import datetime

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day+1
now = datetime.now()

if datetime.weekday(now) == 4: # Task given on Friday
    try: # If it's not the end of a month
        datetime.toordinal(now.replace(year,month,day+1))
        date = str(day+2) + '.' + str(month) + '.' + str(year)
    except ValueError:
        try: # if there's last day after Friday
            datetime.toordinal(now.replace(year,month,day))        
            date = '1' + '.' + str(month+1) + '.' + str(year)
        except ValueError: # Friday is the last day
            date = '2' + '.' + str(month+1) + '.' + str(year)
    subject = 'GMCL. Tasks for Monday (' + date + ')'

else: # Task given on any other day
    try: # If it's not the end of a month
        datetime.toordinal(now.replace(year,month,day))
        date = str(day) + '.' + str(month) + '.' + str(year)
    except ValueError: # If it's the end of a month
        date = '1' + '.' + str(month+1) + '.' + str(year)
    subject = 'GMCL. Tasks for ' + weekday[datetime.weekday(now)+1] + ' (' + date + ')'

task = '''
Hi,

main tasks for GMCL team:

1. Verify your bugs

2. iOS & Android new builds' check 

Thanks!
'''

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://accounts.google.com')
elem = driver.find_element_by_id('Email')
elem.send_keys('g.mishchevskii@gmail.com')
elem.send_keys(Keys.RETURN)
driver.find_element_by_id('next').click()
sleep(1)
driver.find_element_by_id('PersistentCookie').click()
driver.find_element_by_id('Passwd').send_keys('ctktybevNtcn')
driver.find_element_by_id('signIn').click()
driver.get('https://mail.google.com/mail/u/0/?pli=1#inbox?compose=new')
sleep(8)
driver.find_element_by_name('to').send_keys('hof.gmcl2@playtika.com')
driver.find_element_by_name('to').send_keys(Keys.RETURN)
driver.find_element_by_name('subjectbox').send_keys(subject)
driver.find_element_by_xpath("//div[@role='textbox']").send_keys(task)
exit()
