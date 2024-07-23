def extract_name_from_email(email):
    name_part = email.split('@')[0]
    return name_part.title()


def get_user_data():
    user_data = {}

    while True:
        email = input("Email: ").strip()

        if email == "":
            break

        proposed_name = extract_name_from_email(email)

        while True:
            response = input(f"Is your name {proposed_name}? (Y/n) ").strip().lower()

            if response == "" or response == "y":
                user_data[email] = proposed_name
                break
            elif response == "n":
                correct_name = input("Name: ").strip()
                user_data[email] = correct_name
                break
            else:
                print("Invalid input. Please enter Y, n, or leave it blank for default (Y).")

    return user_data


def run():
    user_data = get_user_data()

    print("\nStored emails and names:")
    for email, name in user_data.items():
        print(f"{name} ({email})")

run()
