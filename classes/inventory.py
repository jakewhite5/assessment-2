import csv
import os

class Inventory:
    


    def __init__(self):
        # creates and calls for inventory list to be made from csv
        self.inventory = []
        self.init_inventory()
    

    def init_inventory(self):
        # sets the path too and opens the inventory csv in order to populate init list
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path) as inventory_csv:
            reader = csv.DictReader(inventory_csv)
            for row in reader:
                self.inventory.append(row)

    def list_inventory(self):
        # displays each item id, title, and rating based off the the init list
        for item in self.inventory:
            if int(item['copies_available']) > 0:
                print(item['id'], item['title'], item['rating']) 
        
    def rent_movie(self, id):
        #checks for amount of movies in stock and decrements amount if in stock
        for movie in self.inventory:
            if movie['id'] == id:
                if movie['copies_available'] == '0':
                    print('Sorry we are out of copies of that Title')
                else:
                    movie['copies_available'] = str(int(movie['copies_available']) - 1)
                    self.update_inventory()
                    return movie['title']
                
    def return_movie(self, movie):
        #finds movie that is being returned and increment amount
        for item in self.inventory:
            if item['title'] == movie:
                item['copies_available'] = str(int(item['copies_available'] + 1))
        self.update_inventory()
        
    
    def update_inventory(self):
        # re writes inital csv with currently held data in initial list
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'w') as inventory_csv:
            writer = csv.DictWriter(inventory_csv, fieldnames=['id','title','rating','copies_available'])
            writer.writeheader()
            for movie in self.inventory:
                writer.writerow({'id':movie['id'],'title':movie['title'],'rating':movie['rating'],'copies_available':movie['copies_available']})
