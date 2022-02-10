from doctest import Example
import requests 
from pprint import pprint

URL = "http://127.0.0.1:5000/users"

EXAMPLE_JSON = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Playing video games"
}

def display_user(pk):
    current_user = requests.get("%s/%s" % (URL, pk))
    if current_user.status_code == 200:
        pprint(current_user.json())
    else:
        print("something went wrong while trying to display the user.")

def update_user(pk, first_name, last_name, hobbies):
    user_json = EXAMPLE_JSON
    user_json["first_name"]= first_name
    user_json["last_name"]= last_name
    user_json["hobbies"]= hobbies
    
    out = requests.put("%s/%s" % (URL, pk), json=user_json)
    if out.status_code == 204:
        print("Change successful.")
    else:
        print("Something went wrong while trying to update user.")


if __name__ == "__main__":
    pk = int(input("Type in the desired user id: "))
    print("Current user: ")
    display_user(pk)
    first_name = input("Type the desired first name: ")
    last_name = input("Type the desired last name: ")
    hobbies = input("Type in the desired hobbies: ")
    update_user(pk, first_name, last_name, hobbies)
    option = input ("Would you like to display changes? y/N")
    if option == "y"or option == "Y":
        display_user(pk)