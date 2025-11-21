from  decorators import input_error

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name]=phone
        return f"Contact updated." 
    return f"⚠️ Контакт '{name}' не знайдено."
    
@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{contacts[name]}" if contacts.get(name) else f"⚠️ Контакт '{name}' не знайдено."
    
@input_error
def show_all(contacts):
    if not contacts:
        return "📭 No contacts saved yet."
    return "усі збережені контакти з номерами телефонів:\n" + \
           "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def main(): # print/input тут
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
            elif command=="change":
                 print(change_contact(args, contacts))
            elif command=="phone":
                 print(show_phone(args, contacts))
            elif command=="all":
                 print(show_all(contacts))
            else:
                 print("Invalid command.")
                 
if __name__ == "__main__":
    main()