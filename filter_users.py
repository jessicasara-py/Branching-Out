import json


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)

    return users


def filter_users_by_name(users, name):
    filtered_users = [
        user for user in users
        if user["name"].lower() == name.lower()
    ]

    return filtered_users


def filter_users_by_age(users, age):
    filtered_users = [
        user for user in users
        if user["age"] == age
    ]

    return filtered_users


def filter_users_by_email(users, email):
    filtered_users = [
        user for user in users
        if user["email"].lower() == email.lower()
    ]

    return filtered_users


def main():
    users = load_users()

    filter_option = input(
        "What would you like to filter by? "
        "(name, age, or email): "
    ).strip().lower()

    if filter_option == "name":
        name = input("Enter a name: ").strip()
        filtered_users = filter_users_by_name(users, name)

    elif filter_option == "age":
        age = int(input("Enter an age: "))
        filtered_users = filter_users_by_age(users, age)

    elif filter_option == "email":
        email = input("Enter an email: ").strip()
        filtered_users = filter_users_by_email(users, email)

    else:
        print("Filtering by that option is not supported.")
        return

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    main()