from csv import reader

#NOTE: This function returns a list with elements [City, State abreve, State, Lat, Lon, TimeZone]
    #Ex: ['Boston', ' MA', ' Massachusetts', ' 42.3188', ' -71.0846', ' America/New_York']

def getLon_Lat(city, state):
    with open('uscities.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)
        l = list(csv_reader)

    for i in range(len(l)):
        if l[i][0] == city:
            if str(l[i][2]) == " " + str(state):
                return l[i] #city information
            # rl = []
            # rl.append(l[i][3])
            # rl.append(l[i][3])
            # print(rl) #only coordinates
            # break
    return

# //endpoints - lat lon, interests
