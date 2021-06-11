from customer import Customer
from inventory import Inventory
class Interface:

    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.customer = Customer()

    def run(self):
        while True:
            mode = input(self.menu())
            if mode == '1':
                first = input('Please enter customer first name. : ')
                last = input('Please enter customer last name. : ')
                self.customer.new_customer(first, last)
            elif mode == '2':
                print(f'\nWe currently Have:')
                self.inventory.list_inventory()
                print(f'\n')
            elif mode == '3':
                customer_id = input('Please enter customer ID to view current rentals. : ')
                print(f'\nItems currently being rented: ')
                print(self.customer.get_rentals(customer_id))
                print(f'\n')
            elif mode == '4':
                customer_id = input('Please enter customer ID : ')
                self.inventory.list_inventory()
                selection = input('Please enter movie ID that is being rented. : ')
                returned_title = self.inventory.rent_movie(selection)
                self.customer.add_movie(returned_title, customer_id)

            elif mode == '5':
                id = input('Please enter customer id')
                movie = input('Please enter movie name')
                self.customer.return_movie(id, movie)
                
            elif mode == '6':
                print('Goodbye!')
                break

    def menu(self):
        return f"Welcome to RIP Blockbuster!\nWhat would you like to do?\nOptions:\n1. Create New Customer Account\n2. View Inventory\n3. View Customer Rentals\n4. Rent out Movie\n5. Movie Return\n6. Quit\n"
    
