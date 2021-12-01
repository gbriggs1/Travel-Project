import requests

def openTripMap():
    response = requests.get("https://api.opentripmap.com/0.1/en/places/radius?radius=200&lon=-75.1652&lat=39.9526&rate=3&apikey=5ae2e3f221c38a28845f05b6671c0266f303774d03391de1ba8a83b3")
    d = {}
    for i in range(len(response.json()['features'])):
        d[response.json()['features'][i]['properties']['name']] = response.json()['features'][i]['properties']['kinds']

    return d

def tripTypes(kinds):
    response = requests.get("http://api.opentripmap.com/0.1/en/places/bbox?lon_min=-125&lat_min=30&lon_max=-71&lat_max=42&kinds="+kinds+"&format=geojson&apikey=5ae2e3f221c38a28845f05b6671c0266f303774d03391de1ba8a83b3")
    for i in range(len(response.json()['features'])):
        print(response.json()['features'][i]['properties']['name'])
    return
def main():
    d = openTripMap()
    total = 0
    for key in d:
        print(key)
    print(d)
    #plan: turn the info to dictionary of events and tags. So key is event name and value is the descripters included under 'kinds'.
main()
