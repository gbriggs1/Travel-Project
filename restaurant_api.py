from __future__ import print_function

import argparse
import json
import pprint
import requests
import sys
import urllib

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

API_KEY= "s-475sGL9tb6SmL205hy4utmCsgz6oj7cCVdM_lcN6ATrWmpuYGe694QZpiE86u07GEAGSZMmd69n6D6MoVQNH1Xg8x1xNK8KC3qQsRH1Ad4pPeuWjlKMZwJCSSPYXYx"


# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'Philadelphia, PA'
SEARCH_LIMIT = 50

class EventInfo:
    def __init__(self,title, date_time, address, category, link, price, isRestaurant,weather):
        self.title= title
        self.date_time=date_time
        self.address= address
        self.category= category
        self.link=link
        self.price=price
        self.isRestaurant=True
        self.weather=weather
    def __str__(self):
        eventString="Venue Info \n------------------------------------------\n"
        eventString+= "Venue title: " + self.title + "\n"
        eventString+= "Venue date_time: " + self.date_time+ "\n"
        eventString+= "Venue address: " + self.address+ "\n"
        eventString+= "Venue category: " + self.category+ "\n"
        eventString+= "Venue link: " + self.link+ "\n"
        eventString+= "Venue price: " + self.price+ "\n"
        eventString+= "Venue is restaurant: " + self.isRestaurant+ "\n"
        eventString+= "Venue weather: " + self.weather+ "\n"
        eventString+= "------------------------------------------ "
        return eventString
    def serialize(self):
        ret = {
            "title": self.title,
            "date-time": self.date_time,
            "address": self.address,
            "category": self.category,
            "link": self.link,
            "price": self.price,
            "isRestaurant": self.isRestaurant,
            "weather": self.weather
        }
        return ret


def search(api_key, term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }

    api_feedback= create_data(request(API_HOST, SEARCH_PATH, api_key, url_params=url_params))#formats api response and returns a restaurant
    return api_feedback



def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    response = requests.request('GET', url, headers=headers, params=url_params)
    #print(response.json())
    return response.json()

def fill_restaurant(response, index):
    title = response['businesses'][index]['name']                           #stores title of event
    date_time=response['businesses'][index]['is_closed']                    #stores whether event is closed
    address= response['businesses'][index]['location']['display_address']   #stores address of event
    category= response['businesses'][index]['categories'][0]['alias']       #stores category of event
    link=response['businesses'][index]['url']                               #stores url of event
    price= None                                                             #stores price of event_set
    isRestaurant= True
    weather="weather"                                                       #weather is set later with API call
    return EventInfo(title,date_time,address,category,link,price,isRestaurant,weather)


def create_data(restaurants):
    restaurant_count= len(restaurants['businesses'])
    selected_restaurant= None
    event_list=[]                                            #restaurant to be returned
    for i in range(restaurant_count):
        restaurant = fill_restaurant(restaurants,i)
        event_list.append(restaurant)

    return event_list.pop().serialize()


#search(API_KEY,"dinner", "Lake Forest, IL")) example search request call
