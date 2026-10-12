import json


def load_users():
    """Load users from the JSON database file."""
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)

    return users


def display_users(users):
    """Print matching users or a message if no users were found."""
    if users:
        for user in users:
            print(user)
    else:
        print("No users found matching your criteria.")


def filter_users_by_name(users, name):
    """Filter users by name, ignoring uppercase and lowercase."""
    filtered_users = [
        user for user in users
        if user.get("name", "").lower() == name.lower()
    ]

    display_users(filtered_users)


def filter_users_by_age(users, age):
    """Filter users by their exact age."""
    filtered_users = [
        user for user in users
        if user.get("age") == age
    ]

    display_users(filtered_users)


def filter_users_by_email(users, email):
    """Filter users by email, ignoring uppercase and lowercase."""
    filtered_users = [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]

    display_users(filtered_users)


def main():
    """Ask for a filter option and display matching users."""
    filter_option = input(
        "What would you like to filter by? (name, age, email): "
    ).strip().lower()

    if filter_option not in ("name", "age", "email"):
        print("Invalid filter option. Please choose name, age, or email.")
        return

    users = load_users()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: "))
        except ValueError:
            print("Please enter a valid integer for the age.")
            return

        filter_users_by_age(users, age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(users, email_to_search)


if __name__ == "__main__":
    main()
