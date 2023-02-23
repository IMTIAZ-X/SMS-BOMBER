import requests

number=str(input(" Enter Your Number : "))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

requests.get(api)
