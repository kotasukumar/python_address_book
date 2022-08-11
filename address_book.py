import sys


class Contact:
    def __init__(self, first_name, last_name, address, city, state, pin_code, email_id, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.pin_code = pin_code
        self.email_id = email_id
        self.mobile_number = mobile_number
        self.details = [self.first_name, self.last_name, self.address, self.city, self.state, self.pin_code,
                        self.email_id, self.mobile_number]


def add(name):
    local = []
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    address = input("Enter the address: ")
    city = input("Enter the city: ")
    state = input("Enter the state: ")
    pincode = input("Enter the pin code: ")
    email = input("Enter email id: ")
    mobile_number = input("Enter mobile number: ")
    result = Contact(f_name, l_name, address, city, state, pincode, email, mobile_number)
    contact_list.append(result.details)
    local.append(result.details)
    addressbook[name] = local


def edit(name):
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    for i in contact_list:
        if f_name == i[0] and l_name == i[1]:
            print("Contact found, please enter details to update")
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            address = input("Enter the address: ")
            city = input("Enter the city: ")
            state = input("Enter the state: ")
            pincode = input("Enter the pin code: ")
            email = input("Enter email id: ")
            mobile_number = input("Enter mobile number: ")
            index = contact_list.index(i)
            contact_list[index] = [f_name, l_name, address, city, state, pincode, email, mobile_number]
            addressbook[name] = contact_list


def book_entry(name):
    print(name)
    while True:
        user_input = int(
            input("Enter your choice\n1:Add the contact\n2:Edit the contact\n3:Delete the contact\n4:Display"
                  "\n5:Return to main menu: "))
        if user_input == 1:
            add(name)
            print("Contact added successfully")
        elif user_input == 2:
            edit(name)
            print("Contact edited successfully")
        elif user_input == 3:
            f_name = input("Enter first name: ")
            l_name = input("Enter last name: ")
            for i in addressbook.get(name):
                if f_name == i[0] and l_name == i[1]:
                    contact_list.remove(i)
            print("Contact deleted successfully")
        elif user_input == 4:
            print(addressbook.get(name))
        elif user_input == 5:
            main_menu()


def main_menu():
    while True:
        menu = int(input("Enter your choice\n1:Create book\n2:Access the existing address book\n"
                         "3:Display all books\n4:Exit: "))
        if menu == 1:
            book_name = input("Enter name of the book: ")
            if addressbook:
                for i in addressbook:
                    if i == book_name:
                        print("Name already exist please enter another name")
                        main_menu()
                    else:
                        book_entry(book_name)
            else:
                book_entry(book_name)
        elif menu == 3:
            print(addressbook)
        elif menu == 4:
            sys.exit()


if __name__ == "__main__":
    print("Welcome to address book")
    addressbook = {}
    contact_list = []
    main_menu()

