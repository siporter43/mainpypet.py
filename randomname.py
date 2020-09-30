#we're gonna do a random name request from the website http://pseudorandom.name/ and then hopefully things will work
from pprint import pprint
import requests 

def request_name():
    url = "http://pseudorandom.name/"
    response = requests.get(url)

    print (response.text)
    
    print(response.status_code)

    headers = dict(response.headers)

    pprint(headers)

request_name()