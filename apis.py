from pprint import pprint
import requests 

from private import LAT, LNG, OPENUV_KEY


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

#request_location()


#curl "https://fourtonfish.com/hellosalut/?lang=de"
#we're about to call for this to output a greeting in german
def request_hello():
  url = "https://fourtonfish.com/hellosalut/?lang=de"
  response = requests.get(url, params={'lang': 'de'})
  data = response.json()
  print(data['hello'])

request_hello()
#below requests activities
def request_boredapi():
  url = "https://www.boredapi.com/api/activity"
  response = requests.get(url, params={'participants' : '2'})
  data = response.json()
  print(data['activity'])
request_boredapi()

def request_insult():
  url = "https://evilinsult.com/generate_insult.php"
  response = requests.get(url, params={'lang': 'en' , 'type' : 'json'})
  data = response.json()
  print(data['insult'])
request_insult()

def request_agify():
  url = "https://api.agify.io"
  response = requests.get(url, params={'name': 'Dan'})
  data = response.json()
  print(data['age'])
request_agify()


def request_uv():
    #here's hoping this prints UV and OZone info for today
    response = requests.get(
        "https://api.openuv.io/api/v1/uv",
        params = {'lat': LAT, 'lng': LNG},
        headers= {'x-access-token':OPENUV_KEY}
    )
    data = response.json()
    print("UV Index:", data['result']['uv'])
    print("Ozone:", data['result']['ozone'])
request_uv()

def request_shakespeare():
    url = "https://shakespeare1.p.rapidapi.com/shakespeare/generate/insult"
    response = requests.get(url, params={"limit": "1"}, 
    headers= {'rapidAPI_KEY':"7c40183e4cmsh905dcd68bafea67p1b8572jsndedc57c1e54f"})
    data = response.json()
    if not response.ok:
      print("There was a problem with your request!")
      print(response.status_code, response.reason)
      pprint(response.headers)
      return
    print(data['quote'])
request_shakespeare()
