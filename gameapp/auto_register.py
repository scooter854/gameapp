from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from subprocess import call
import time
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

print("Initializing Variables\n")
options=Options()
options.headless=True
chrompath='/usr/local/bin/chromedriver'
driver=webdriver.Chrome(chrome_options=options, executable_path=chrompath)
fromaddr = "paytonmurray51@gmail.com"
toaddr = "paytonmurray51@gmail.com" 
msg = MIMEMultipart()    
msg['From'] = fromaddr   
msg['To'] = toaddr  
msg['Subject'] = "Car Registration"
body = "Your car has been successfully registered" 
msg.attach(MIMEText(body, 'plain'))  
filename = "registered.jpg"

print("accessing registration site\n")
driver.get("https://www.register2park.com")

time.sleep(2)

print("Selecting register vehicle\n")
driver.find_element_by_link_text('Register Vehicle').click()

time.sleep(2)

print("selecting Olympus apartments\n")
driver.find_element_by_id('propertyName').send_keys("Olympus Las Colinas")
driver.find_element_by_id('confirmProperty').click()

time.sleep(5)

print("Select Radio Button for Oylmpus\n")
driver.find_element_by_css_selector("input[type='radio'][value='14579']").click()
driver.find_element_by_id('confirmPropertySelection').click()

time.sleep(5)

print("select visitor registration\n")
driver.find_element_by_id('registrationTypeVisitor').click()

time.sleep(5)

print("adding vehicle information\n")
driver.find_element_by_id('vehicleApt').send_keys("106e")
driver.find_element_by_id('vehicleMake').send_keys("gmc")
driver.find_element_by_id('vehicleModel').send_keys("sierra")
driver.find_element_by_id('vehicleLicensePlate').send_keys("C695374")
driver.find_element_by_id('vehicleInformation').click()

time.sleep(15)

print("capture  screen-shot\n")
driver.save_screenshot('registered.jpg')

time.sleep(5)

print("closing browser\n")
driver.close()

print("prepping email...\n")
attachment = open("./registered.jpg", "rb") 

p = MIMEBase('application', 'octet-stream') 
 
p.set_payload((attachment).read()) 

encoders.encode_base64(p)    
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
 
msg.attach(p) 

s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 

s.login(fromaddr, 'payton95') 

text = msg.as_string() 

print("sent email\n")
s.sendmail(fromaddr, toaddr, text) 

print("Done!")
s.quit() 