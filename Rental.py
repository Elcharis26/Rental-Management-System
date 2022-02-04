from pprint import pprint
from time import strftime

class Rental:

    inventory = { 'bike': 2,
               'boat': 2,
               'car': 1,
               'cycle': 3 }

    rentals, customers = {}, {} 

    def addCustomer(name, phone, email):
        Rental.customers[name] = {}
        Rental.customers[name]["phone"] = phone
        Rental.customers[name]["email"] = email

    def viewCustomerList():
        print()
        pprint(Rental.customers)

    def addRental(customer, rental_date, return_date, vehicle_type):
        Rental.rentals[customer] = {}
        Rental.rentals[customer]["rental_date"] = rental_date
        Rental.rentals[customer]["return_date"] = return_date
        Rental.rentals[customer]["vehicle_type"] = vehicle_type

    def viewRentalBookings():
        print()
        pprint(Rental.rentals)

    def viewInventory():
        print()
        pprint(Rental.inventory)

class Operations(Rental):

    def __init__(self):
        msg = """\nChoose an option:
    1. Add customer
    2. Add rental booking
    3. See customer list
    4. See rental booking list
    5. See inventory of vehicles available

    (press "e" to end program)
"""

        def take_input():
            print(msg)
            user = input()

            if user == "1":
                name = input("\nEnter customer name: ")
                phone = int(input("Enter phone number: "))
                email = input("Enter email address: ")
                Operations.addCustomer(name, phone, email)
                print(f'\n"{name}" added as customer!')
                take_input()
                
            elif user == "2":
                if Operations.customers == {}:
                    print("\nNo customers have been registered currently.")
                else:
                    print("Choose customer from below: ")
                    customers = Operations.customers
                    lst = list(enumerate(customers, start = 1))
                    for i in lst:
                        print(*i, sep = ". ")
                    print()
                    customer = int(input())
                    customer = lst[customer-1][1]
                    if customer in Operations.rentals:
                        print("\nPlease return rented vehicle before renting another.")
                    else:
                        if customer in Operations.customers:
                            rental_date = input("Enter rental date: ") or strftime("%d-%m-%Y")
                            return_date = input("Enter return date: ") or "Null"
                            print("Choose vehicle from below: ")
                            vehicles = Operations.inventory
                            lst = list(enumerate(vehicles, start = 1))
                            for i in lst:
                                print(*i, sep = ". ")
                            print()
                            vehicle = int(input())
                            vehicle = lst[vehicle-1][1]

                            if Operations.inventory[vehicle] > 0:
                                Operations.addRental(customer, rental_date, return_date, vehicle)
                                print(f'\n"{vehicle}" booked for "{customer}" successfully!')
                                Operations.inventory[vehicle] -= 1
                            else:
                                print(f'\n"{vehicle_type}" cannot be rented as it is already booked.')
                        else:
                            print(f'\n"{customer}" is not a registered customer.\nPlease add "{customer}" as customer and try again.')

                take_input()

            elif user == "3":
                if Operations.customers == {}:
                    print("\nNo customers have registered currently.")
                else:
                    Operations.viewCustomerList()

                take_input()

            elif user == "4":
                [ print("\nNo vehicles have been rented currently.") if Operations.rentals == {} else Operations.viewRentalBookings() ]

                take_input()

            elif user == "5":
                Operations.viewInventory()
                take_input()

            elif user == "e":
                print("\nProgram ended successfully.")

            else:
                print("\nInvalid input\nTry again\n")
                take_input()

        take_input()

Operations()
