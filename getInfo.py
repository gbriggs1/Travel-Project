#Script will call backend with info from front end then return the desired info to the front end
import getLon_Lat
import getWeather
# sys.path.insert(1, '/home/gbriggs1/cs71/cs71_project/API_algorithms')
# when html ready -> this will take input parameter 'city'
    # will also have more info functions such as displaying events.
# def getEventSuggestions():
#     print("here")
#
#     return
def cityCoords(cityName, cityState): #return coords
    city_list = getLon_Lat.getLon_Lat(cityName, cityState)
    cit_lat = city_list[3].lstrip()
    cit_lon = city_list[4].lstrip()
    state_abr = city_list[1].lstrip()
    return [cit_lat, cit_lon, state_abr]
def getWeather(coords): #returns weather description
    import getWeather
    weather_list = getWeather.getWeather(coords[0], coords[1])
    return weather_list[1]
def getTemp(coords):#returns temperature in Fº
    import getWeather
    weather_list = getWeather.getWeather(coords[0], coords[1])
    return weather_list[0]
# def getInfo():
#     getEventSuggestions() #will also take a set of user preferences to make its decisions
# getInfo()
