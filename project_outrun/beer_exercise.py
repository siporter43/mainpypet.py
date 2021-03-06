# Description of script
"""Trying to get info from the beer site and be able to determine the data types. Then we
attempt to pull the info from a terminal using the given fncn name"""

# Imports

from pprint import pprint

import requests

import textwrap

# Global Variables

WIDTH = 58

WRAP = 50


# Other variables

final = {}
data = response.json()

#the hw part
def main():
    response = requests.get("http://api.punkapi.com/v2/beers/random")
    
    data[0].keys()
    beer = data[0]
    beer['name']
    beer['description']

    final['name'] = beer['name']

    description = textwrap.wrap(beer['description'], WRAP)
    temp_desc = ""   
    for line in description:
        temp_desc += f"{line}\n"
    
    final['description'] = temp_desc
    # beer['ingredients'].keys()
    ing = beer['ingredients']
    # ing.keys()

    # ing['malt'][0]['name']

    final['ingredients'] = []

    for malt in ing['malt']:
        name = malt['name'] + " Malt"
        final['ingredients'].append(name)


    for hops in ing['hops']:
        name = hops['name'] + " Hops"
        final['ingredients'].append(name)


    final['ingredients'].append(ing['yeast'] + " Yeast")

    final['ingredients'] = list(set(final['ingredients']))
    
    temp_ing = ""

    for item in final["ingredients"]:
        temp_ing += f"{item}\n"

    final['ingredients'] = temp_ing

    print(final['name'])
    print(final['description'])
    print(final['ingredients'])

# def beer_ingredients():
#     print(final['name'])
#     print(final['ingredients'])
# main()

