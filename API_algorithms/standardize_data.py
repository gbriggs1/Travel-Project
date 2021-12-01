import requests

class VenueInfo:
    def __init__(self,state,name,timezone,url,score,address,country,city):
        self.state= state
        self.name= name
        self.timezone= timezone
        self.url= url
        self.score= score
        self.address= address
        self.country=country
        self.city=city

    def __str__(self):
        eventString= "Event name: " + self.name + "\n"
        eventString+= "Event country: " + self.country+ "\n"
        eventString+= "Event state: " + self.state+ "\n"
        eventString+= "Event city: " + self.city+ "\n"
        eventString+= "Event address: " + self.address+ "\n"
        eventString+= "Event timezone: " + self.timezone+ "\n"
        eventString+="Event url: " + self.url+ "\n"
        eventString+= "Event score: " + str(self.score)+ "\n"
        eventString+="------------------------------------------"
        return eventString


#    def __init__(type):


def fillVenue(response, index):
    address= response.json()['events'][index]['venue']['postal_code']
    state = response.json()['events'][index]['venue']['state']
    name = response.json()['events'][index]['venue']['name']
    timezone = response.json()['events'][index]['venue']['timezone']
    url = response.json()['events'][index]['venue']['url']
    score = response.json()['events'][index]['venue']['score']
    address = response.json()['events'][index]['venue']['address']
    country = response.json()['events'][index]['venue']['country']
    city = response.json()['events'][index]['venue']['city']
    curVenue= VenueInfo(state,name,timezone,url,score,address,country,city)
    return curVenue


def main():
    lat = 37.7749
    lon = 122.4194
    response = requests.get("https://api.seatgeek.com/2/events?lat="+str(lat)+"&lon=-"+str(lon)+"&range=12mi&client_id=MjM0MDA1Njh8MTYzMTg5MTMyNi4wNjQ5OTc3")
    for i in range(len(response.json()['events'])):
        print(response.json()['events'][i]['type'])

def createData(lat, lon):
    user_lat = lat #Philly latitude
    user_lon = lon #Philly longitude
    response = requests.get("https://api.seatgeek.com/2/events?lat="+str(lat)+"&lon=-"+str(lon)+"&range=12mi&client_id=MjM0MDA1Njh8MTYzMTg5MTMyNi4wNjQ5OTc3") #request for philly events
    event_set = set([])
    event_amnt= len(response.json()['events'])
    print(event_amnt)
    for i in range(event_amnt):
        event= response.json()['events'][i]['type']
        venue = response.json()['events'][i]['datetime_utc']
        performanceLength= len(response.json()['events'][i]['performers'])

        #for j in range(performanceLength):
            #print(response.json()['events'][i]['performers'][j]['type'])
            #print(response.json()['events'][i]['performers'][j]['type'])
        curVenue= fillVenue(response,i) #fills venue information and gets venueInfo object
        print(str(curVenue))
        #event_info= response.json()['events'][i][event]
        event_set.add(event)



    #print(event_amnt)

    #print("Which event type are you interested in?")
    #print(event_set)
    #response= str(input())
    #print("Here is an event for you!")
    #print(response.json()['events'][1][response])

createData(39.9526, 75.1652)
