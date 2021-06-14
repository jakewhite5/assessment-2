import csv
import os
class Customer:

    #initially creates list from csv data

    def __init__(self):
        self.customer_list = []
        self.generate_customer_list()
    
    # creates initial list based off csv starting data
    def generate_customer_list(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as customers_csv:
            reader = csv.DictReader(customers_csv)
            for row in reader:
                self.customer_list.append(row)

    # creates instance of new customer by taking in first name and last name. Calls for self id
    def new_customer(self, first, last):
        self.first = first
        self.last = last
        self.generate_id()
        print(f'Customer ID: {self.id}')
        self.save_new_user()

    # creates new id by adding 1 to highest current ID
    def generate_id(self):
        return_id = 0
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as customers_csv:
            reader = csv.DictReader(customers_csv)
            for row in reader:
                if int(row['id']) > return_id:
                    return_id = int(row['id'])
        self.id = str(return_id + 1)
    
    #makes append case for new users
    def save_new_user(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'a') as customer_csv:
            writer = csv.DictWriter(customer_csv, fieldnames=['id','first_name','last_name','current_video_rentals'])
            writer.writerow({'id':self.id, 'first_name':self.first, 'last_name':self.last})

    # add movie by applying details of movie to customer object str. identifies quantity and format by locating /
    def add_movie(self, movie_name, customer_id):
        customer = self.get_customer_by_id(customer_id)
        if self.get_rentals(customer_id).count('/') == 2:
            raise 'Customer at rental limit'
        elif self.get_rentals(customer_id).count('/') == 1:
            customer['current_video_rentals'] = customer['current_video_rentals']+f'/{movie_name}'
        elif self.get_rentals(customer_id) == '':
            customer['current_video_rentals'] = movie_name
        else:
            customer['current_video_rentals'] = customer['current_video_rentals']+f'/{movie_name}'
        self.update_customers()

    # return rental from customer based on id                    
    def get_rentals(self, customer_id):
        for customer in self.customer_list:
            if customer['id'] == customer_id:
                return customer['current_video_rentals']

    # returns customer object based on id
    def get_customer_by_id(self, customer_id):
        for customer in self.customer_list:
            if customer['id'] == customer_id:
                return customer

    #total save to make data persistent after any transaction
    def update_customers(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'w') as customer_csv:
            writer = csv.DictWriter(customer_csv, fieldnames=['id','first_name','last_name','current_video_rentals'])
            writer.writeheader()
            for customer in self.customer_list:
                writer.writerow({'id':customer['id'],'first_name':customer['first_name'],'last_name':customer['last_name'],'current_video_rentals':customer['current_video_rentals']})

    # remove movie str from customer object with formatting in mind
    def return_movie(self, id, movie):
        customer = self.get_customer_by_id(id)
        if '/' in self.get_rentals(id):
            rental_list = self.get_rentals(id).split('/')
            rental_list.remove(movie)
            if len(rental_list) == 2:
                customer['current_video_rentals'] = '/'.join(rental_list)
            else:
                customer['current_video_rentals'] = rental_list[0]
        else:
            customer['current_video_rentals'] = ''
        self.update_customers()


        




