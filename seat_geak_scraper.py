import requests



class EventInfo:

    def __init__(self,title, date_time, address, category, link, price, isRestaurant,weather):
        self.title= title
        self.date_time=date_time
        self.address= address
        self.category= category
        self.link=link
        self.price=price
        self.isRestaurant=False
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


def fillEvent(response, index):
    title= response.json()['events'][index]['short_title']
    date_time = response.json()['events'][index]['datetime_local']
    address = response.json()['events'][index]['venue']['address'] + ", " + response.json()['events'][index]['venue']['city'] + ", " + response.json()['events'][index]['venue']['postal_code']
    category= response.json()['events'][index]['type']
    link= response.json()['events'][index]['venue']['url']
    price= "$"+str(response.json()['events'][index]['stats']['lowest_price'])
    isRestaurant = False
    weather="NOT_YET"
    curEvent= EventInfo(title,date_time,address,category,link,price,isRestaurant,weather)
    return curEvent


def build_url(lat, lon,date,budget,interests):#specefies request URL based on interests, budget, date, lat & lon
        url = "https://api.seatgeek.com/2/events?lat="+str(lat)+"&lon="+str(lon)+"&range=10mi&per_page=10&highest_price.lte="+str(budget)+"&datetime_local.gte="+date
        #date must come in formate of 2021-11-19 --> then this will return only events on that day.
        url2= "&client_id=MjM0MDA1Njh8MTYzMTg5MTMyNi4wNjQ5OTc3"
        interest_size= len(interests)
        for i in range(interest_size):
            if interests[i] == 'Music':
                interests[i] = 'concert'
            if interests[i] == 'Plays' or interests[i] == 'Movies':
                interests[i] = 'theater'
            url+= "&taxonomies.name=" +interests[i]
        url= url+url2
        return url


def createData(lat, lon,date,budget,interests):
    get_request_url= build_url(lat, lon,date,budget,interests)
    response = requests.get(get_request_url) #request for events
    event_list=[]
    event_amnt= len(response.json()['events'])
    for i in range(event_amnt):
        curEvent= fillEvent(response,i)
        event_list.append(curEvent.serialize())

    return event_list
