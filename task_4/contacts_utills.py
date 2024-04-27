def add_contact(args: list[str], contacts: dict):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return f"not enough values to unpack (expected 2, got: {len(args)})"
    
def change_contact(args: list[str], contacts: dict):
    try:
        name, phone = args
        contacts[name] = phone    
        return "Contact changed."
    except ValueError:
        return f"not enough values to unpack (expected 2, got: {len(args)})"


def show_phone(args: list[str], contacts: dict):
    try:
        name,  = args
        return f"phone number: {contacts[name]}"
    except KeyError:
        return f"Contact doesn't exist: {name})"


def all_contacts(contacts: dict):
    str_s = 'All contacts: \n'
    for name, phone in contacts.items():
        str_s += f"{name} {phone} \n"
            
    return str_s[:len(str_s)-1]
    