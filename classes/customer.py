import csv
import os
class Customer:

    def __init__(self):
        self.customer_list = []
        self.generate_customer_list()
    
    def generate_customer_list(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as customers_csv:
            reader = csv.DictReader(customers_csv)
            for row in reader:
                self.customer_list.append(row)

    
    def new_customer(self, first, last):
        self.first = first
        self.last = last
        self.generate_id()
        print(f'Customer ID: {self.id}')
        self.save_new_user()

    
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
    

    def save_new_user(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'a') as customer_csv:
            writer = csv.DictWriter(customer_csv, fieldnames=['id','first_name','last_name','current_video_rentals'])
            writer.writerow({'id':self.id, 'first_name':self.first, 'last_name':self.last})
    
    def add_movie(self, movie_name, customer_id):
        if self.get_rentals(customer_id).count('/') == 2:
            raise 'Customer at rental limit'
        elif self.get_rentals(customer_id).count('/') == 1:
            for customer in self.customer_list:
                if customer['id'] == customer_id:
                    customer['current_video_rentals'] = customer['current_video_rentals']+f'/{movie_name}'
        elif self.get_rentals(customer_id) == '':
            for customer in self.customer_list:
                if customer['id'] == customer_id:
                    customer['current_video_rentals'] = movie_name
        else:
            for customer in self.customer_list:
                if customer['id'] == customer_id:
                    customer['current_video_rentals'] = customer['current_video_rentals']+f'/{movie_name}'
        self.update_customers()

                        
    def get_rentals(self, customer_id):
        for customer in self.customer_list:
            if customer['id'] == customer_id:
                return customer['current_video_rentals']
    
    def update_customers(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'w') as customer_csv:
            writer = csv.DictWriter(customer_csv, fieldnames=['id','first_name','last_name','current_video_rentals'])
            writer.writeheader()
            for customer in self.customer_list:
                writer.writerow({'id':customer['id'],'first_name':customer['first_name'],'last_name':customer['last_name'],'current_video_rentals':customer['current_video_rentals']})

    def return_movie(self, id, movie):
        if '/' in self.get_rentals(id):
            rental_list = self.get_rentals(id).split('/')
            rental_list.remove(movie)
            if len(rental_list) == 2:
                for customer in self.customer_list:
                    if customer['id'] == id:
                        customer['current_video_rentals'] = '/'.join(rental_list)
            else:
                for customer in self.customer_list:
                    if customer['id'] == id:
                        customer['current_video_rentals'] = rental_list[0]
        else:
            for customer in self.customer_list:
                    if customer['id'] == id:
                        customer['current_video_rentals'] = ''
        self.update_customers()


        




