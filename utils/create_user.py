import requests 

URL = "http://127.0.0.1:5000/users"

EXAMPLE_JSON = {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Playing video games"
}

def create_user(first_name, last_name, hobbies):
    user_json = EXAMPLE_JSON
    user_json ["first_name"] = first_name
    user_json ["last_name"] = last_name
    user_json ["hobbies"] = hobbies

    out = requests.post(URL, json=user_json)
    if out.status_code == 201:
        print("User created.")
    else:
        print("something went wrong while trying to create a new user")


if __name__ == "__main__":
    first_name = input("Type in the desired first name: ")
    last_name = input("Typer the desired last name: ")
    hobbies = input("Type the desired hobbies: ")
    create_user(first_name, last_name, hobbies)