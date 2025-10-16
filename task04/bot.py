
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    if contacts.get(name):
        return "Contact already exists, try to change it."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if not contacts.get(name):
        return "Contact does not exist, try to add it."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name, = args
    if not contacts.get(name):
        return "Contact does not exist, try to add it."
    return contacts[name]

def show_all(contacts):
    return "\n".join([f"{name}: {contacts[name]}" for name in contacts.keys()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
