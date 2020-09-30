from pprint import pprint
import requests 

def request_demo():
    #Explore how web requests work
    url = "https://raw.githubusercontent.com/alissa-huskey/python-class/master/hello.txt"
    response = requests.get(url)

    #shows body of response
    print(response.text)

    print(response.status_code)

    headers = dict(response.headers)

    pprint(headers)


def request_weather():
    url = "http://wttr.in/Oakland?u"
    response = requests.get(url)

    print(response.text)

    print(response.status_code)

    headers = dict(response.headers)

    pprint(headers)

#request_weather()

#curl "http://api.open-notify.org/astros.json"

def request_astros():
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    #print(response.text)
    data = response.json()
    print(f"There are {data['number']} people in space today.")

    for astro in data['people']:
        print(f"- {astro['name']}")

#request_astros()

def request_location():
    url = "https://freegeoip.app/json/"
    response = requests.get(url)
    
    data = response.json()
    print(f"We are at {data['latitude']} , {data['longitude']} right now")

request_location()