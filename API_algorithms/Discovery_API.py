
import requests
import json

# This program identifies lists in json responses by transforming them to strings first.
# It fails to deal with the cases were there are lists inside lists.
# It's not really a useful program, it was just a random attempt to create
# the more interesting api_json_res_analysis program.
#
#                                    - Nader 




def print_json_text(response_in_json):
    data = json.dumps(response_in_json)
    print(type(data))
    data = str(data)
    print("After transformation: %s" % (type(data)))
    f_bracket = 0 
    s_bracket = 0 
    items_list = []
    item = ""
    for character in data: 
        if character == "[":
            f_bracket = 1
        elif character == "]":
            s_bracket = 1
        else:
            if f_bracket and not s_bracket:
                item += character
            if s_bracket:
                items_list.append(item)
                item = ""
                f_bracket = 0
                s_bracket = 0
    for elemment in items_list:
        print(elemment)
        print()




res = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?countryCode=US&apikey=xKQauouObxyt0ZElqu68f6yg8A4OU3gj")
keys = res.json()["_embedded"]["events"][3].keys()
n_events = len(res.json()["_embedded"]["events"])
print("\n number of events is: ", n_events, '\n')
#print(keys)
res_in_json = res.json()
print_json_text(res_in_json)


