from flask import Flask, render_template, request, jsonify
import getInfo
from markupsafe import escape
import seat_geak_scraper
import restaurant_api
app = Flask(__name__)
coords = []
trips = []
API_KEY= "s-475sGL9tb6SmL205hy4utmCsgz6oj7cCVdM_lcN6ATrWmpuYGe694QZpiE86u07GEAGSZMmd69n6D6MoVQNH1Xg8x1xNK8KC3qQsRH1Ad4pPeuWjlKMZwJCSSPYXYx"

@app.route("/")
def get_main_page():
    return render_template('index.html')

# (3) This will return a text response
@app.route("/TripInformation", methods=['POST']) #search or path?
def getTripInformation():
    json_data = request.get_json()
    print(json_data)
    city = json_data["tripCity"]
    state = json_data["tripState"]
    # coords = getInfo.cityCoords(city, state)
    interests = json_data["interests"]
    date = json_data["startDate"]
    budget = json_data["dailyBudget"]
    coords = getInfo.cityCoords(city, state)
    data = seat_geak_scraper.createData(coords[0], coords[1], date, budget, interests)
    for i in range(len(data)):
        data[i]['weather'] = getInfo.getWeather(coords)
        data[i]['temp'] = getInfo.getTemp(coords)

    trip = []
    possible = 0
    for i in range(len(data)):
        time = data[i]['date-time'][11] + data[i]['date-time'][12]
        if possible <= int(time) and data[i]['date-time'][:10] == date:
            trip.append(data[i])
            possible = int(time) + 3
    if 'Meals' in interests:
        param = city + ', '+str(coords[2])
        meal = restaurant_api.search(API_KEY, 'dinner', param) #if it returns only 1 meal
        if len(str(possible)) == 1:
            ip = int(possible)+10
            meal['date-time'] = date+'T'+str(ip)+':00:00'
        else:
            meal['date-time'] = date+'T'+str(possible)+':00:00'
        meal['weather'] = getInfo.getWeather(coords)
        meal['temp'] = getInfo.getTemp(coords)
        trip.append(meal)
        #time will be date (2000-12-30)+'T'+possible (12)+ '00:00'
        # print(restaurant_api.search(API_KEY, 'dinner', param))
        #will add this to data
    trips.append(trip)
    print(trip)

    return str(len(trips)-1)



@app.route("/scheduleForm")
def loadScheduling():
    return render_template("integratedForm.html") #load 'scheduling form' with data that includes activities, weather, temp
@app.route("/schedule")
def schedule():
    return render_template("timelinePage.html")
@app.route("/schedule/data", methods=['GET'])
def sendTrip():
    id = int(request.args.get('scheduleid'))
    trip = trips[id]
    # return render_template("", trip)
    ls = []
    ls.append(trip)
    return jsonify(ls) #Need to determine name labeled in front end. This is a json with all trips and their information

if __name__ == '__main__':
    app.run()
