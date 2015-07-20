from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
driver.implicitly_wait(30)

email = driver.find_element_by_id('Email')
nextt = driver.find_element_by_id('next')
remember_check_point = driver.find_element_by_id('PersistentCookie')
password = driver.find_element_by_id('Passwd')
sign_in_button = driver.find_element_by_id('signIn')

email.send_keys('g.mishchevskii@gmail.com')
elem.send_keys(Keys.RETURN)
nextt.click()
remember_check_point.click()
password.send_keys('*')
sign_in_button.click()


driver.get('https://mail.google.com/mail/u/0/?pli=1#inbox?compose=new')

send_to = driver.find_element_by_name('to')
subject_field = driver.find_element_by_name('subjectbox')
letter_field = driver.find_element_by_xpath("//div[@role='textbox']")

send_to.send_keys('hof.gmcl2@playtika.com')
send_to.send_keys(Keys.RETURN)
subject_field.send_keys(subject)
letter_field.send_keys(task)

exit()
