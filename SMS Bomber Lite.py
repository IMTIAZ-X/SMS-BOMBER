import requests

number=str(input(" Enter The Number : +88"))

api="https://stage.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

resp = requests.get(api)
print(resp.text)
