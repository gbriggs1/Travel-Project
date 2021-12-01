import requests
import json



def print_keys(keys, dictionary):
    for i in range(len(keys)):
        print(i,".  ", keys[i], ": ", type(dictionary.get(keys[i])))

def all_items_are_the_same_kind(the_list):


    type_of_item_0 = type(the_list[0])
    type_of_item_1 = type(the_list[0])

    for item in the_list:
        type_of_item_1 = type(item)
        if type_of_item_0 != type_of_item_1:
            return False
    return True

def verify_input(message, minimum, maximum, special_values, history_length):

    user_input = input(message)


    done = False

    if minimum == -1 and maximum == -1:
        while not done:
            if user_input.replace(" ", "").lower() == "y":
                return "y"
            elif user_input.replace(" ","").lower() == "n":
                return "n"
            else:
                user_input = input("\n\n Please enter either y or n:  ")



    else:
        while not done:
            

            special_letter = user_input.replace(" ", "").lower()

            if special_letter == "o" or special_letter == "q" or special_letter == "a":
              return special_letter


            elif special_letter != "":
                firs_letter = user_input.strip()[0]
                if  firs_letter == "h":
                    user_input = user_input.strip()[1:]
                if user_input.isdigit():
                    user_input = int(user_input)
                    if firs_letter == "h":
                      if user_input >= 0 and user_input < history_length:
                        return "h %d" % (user_input)
                      else:
                        print("\n\n you must enter a valid history id number \n\n".upper())
                        user_input = input(message)
                    elif user_input <= maximum and user_input >= minimum:
                        return user_input

            user_input = input(message)
                    

def track_history(item, label, history_list):
    if len(history_list) == 0:
        history_list.append([0, label, item])
        return
    
    id_num = len(history_list) 
    history_list.append([id_num, label, item])

def print_history(history_list, n_items):

    history_string = ""

    if n_items == "a":
        for item in history_list:
            history_string += ">> (%d) %s  " % (item[0], item [1])
    
    print()
    print(history_string + " ||  (a) for all \n")


def explore_json_res(json_response):
    
    original_item = json_response
    current_item = original_item
    label_of_current_item = "ORIGINAL ITEM"
    minimum = 0
    maximum = 0 
    level =  "main item "
    done = False 
    history_list = []
    track_history(current_item, label_of_current_item, history_list)

    while not done:
        print("\n\n", "="*150)
        print_history(history_list, "a")

        if type(current_item) == dict: 
            keys = list(current_item.keys())
            print_keys(keys, current_item)
            minimum = 0 
            maximum = len(keys) - 1 
            user_input = verify_input("\n\n Enter (%d - %d), (o) for original or (q) to quit or (h #) or (a): " % (minimum, maximum), minimum, maximum, ["o,", "q","a"], len(history_list))

            if type(user_input) == str:
                if user_input == "o":
                     current_item = original_item
                     label_of_current_item = "ORIGINAL ITEM"
                     track_history(current_item, label_of_current_item, history_list)

                elif user_input == "a":
                    print_history(history_list, "a")

                elif user_input == "q":
                    print("\n\n","*" *50, "\n\n", "DONE","\n\n", "*" *50, "\n\n" )
                    done = True

                elif user_input.strip()[0] == "h":   
                    index = int(user_input.strip()[1:])
                    current_item = history_list[index][2]
                    label_of_current_item = history_list[index][1]
                    track_history(current_item, label_of_current_item, history_list)

            else:
                key = keys[user_input]
                current_item = current_item.get(key)
                label_of_current_item = "dic key: %s" % key
                track_history(current_item, label_of_current_item, history_list)


                    

        elif type(current_item) == list:

            length = len(current_item)
            list_pointer = current_item

            if all_items_are_the_same_kind(current_item):

                print("\n"+"All items in this list are identical in type: they are %s \n" % type(current_item[0]))

                user_input = verify_input("Do you want to display an item from the list? (y/n): ", -1, -1, [], "")

                if user_input == "y":
                    list_pointer = current_item
                    current_item = current_item[0]
                    label_of_current_item = history_list[len(history_list)-1][1] + " - list - item 0 "
                    track_history(current_item, label_of_current_item, history_list)

                else:
                    minimum = 0
                    maximum = len(current_item)-1
                    user_input = verify_input("\n\n Enter (%d - %d), (o) for original or (q) to quit or (h #) or (a): " % (minimum, maximum), minimum, maximum, ["o", "q", "a"], len(history_list))

                    if user_input == "o":
                        current_item = original_item
                        label_of_current_item = "ORIGINAL item"
                        track_history(current_item, label_of_current_item, history_list)

                    elif user_input == "q":
                        print("\n\n","*" *50, "\n\n", "DONE","\n\n", "*" *50, "\n\n" )
                        done = True
                        return  

                    elif user_input == "a":
                        print_history(history_list, "a")

                    elif type(user_input) == int:
                        list_pointer = current_item
                        current_item = current_item[user_input]
                        label_of_current_item = history_list[len(history_list)-1][1] + " - list - item %d " % (user_input)
                        track_history(current_item, label_of_current_item, history_list) 
                        

                    elif user_input.strip()[0] == "h":
                        index = int(user_input.strip()[1:])
                        current_item = history_list[index][2]
                        label_of_current_item = history_list[index][1]
                        track_history(current_item, label_of_current_item, history_list)

            else:
                print("\n\n NOT ALL items in this list are identicle \n\n")
        else:
            print("\n\n", current_item, "\n\n")
            
            if input("wanna browse more in this list? (y/n): ").replace(" ", "").lower() == "y":
                current_item = history_list[len(history_list)-2][2]
                label_of_current_item = history_list[len(history_list)-1][1] + " - list of %d items " % (len(current_item))
                track_history(current_item, label_of_current_item, history_list)
            else:
                print("\n\n You will now be returned to the original element of this chain. \n\n")
                current_item = original_item
                label_of_current_item = "ORIGINAL item"
                track_history(current_item, label_of_current_item, history_list)



def main(): 
    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/SFO-sky/ORD-sky/2021-10-27"

    querystring = {"inboundpartialdate":"2021-10-27"}

    headers = {
        'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "10fbe44849msh06d96ec84656b34p17f832jsn645223ab0c92"
        }

    lat = 37.7749
    lon = 122.4194
    response = requests.get("https://api.seatgeek.com/2/events?lat="+str(lat)+"&lon=-"+str(lon)+"&range=12mi&client_id=MjM0MDA1Njh8MTYzMTg5MTMyNi4wNjQ5OTc3")
    res = response
    info_in_json = res.json()
    explore_json_res(info_in_json)

main()




