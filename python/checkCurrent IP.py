import requests
response= requests.get('http://ipecho.net/plain')
print ("My Original IP Address:",response.text)
input("")
