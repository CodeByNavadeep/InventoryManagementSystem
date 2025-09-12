import csv

class product_manager:
    
    def add_product(self, name, price, stock):
        
        self.name = name
        self.price = price
        self.stock = stock
        
        new_row = {"name" : self.name, "price" : self.price, "stock" : self.stock}
        
        file_path = "products.csv"
        
        item="notExists"
        try:
            with open(file_path, "r") as file:
                self.check_is_list_empty()
                reader = csv.DictReader(file)
                for row in reader:
                    if self.name in row.values():
                        item="exists"
                        print("\n"+f"{self.name} already exits!")
                        print("Select the Update option to update it.")
            if item=="notExists":
                with open(file_path, "a", newline='') as file:
                    field_names = ["name", "price", "stock"]
                    writer = csv.DictWriter(file, fieldnames=field_names)
                    writer.writerow(new_row)
                    print("\nProduct added successfully.")
        except FileNotFoundError:
            with open(file_path, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "price", "stock"])
                field_names = ["name", "price", "stock"]
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writerow(new_row)
                print("\nProduct added successfully.")
                
            
        
    
    def update_product(self, name, real_val, update_val):
        file_path = "products.csv"
        
        with open(file_path, "r") as file:
            
            reader = csv.DictReader(file)
            new_rows=[]
            for row in reader:
                if name in row.values():
                    row[real_val]=update_val
                    new_rows.append(row)
                    name=name.capitalize()
                    print("\n\n"+f"'{name}' Product's {real_val} is updated to '{update_val}' successfully.")
                else:
                    new_rows.append(row)
            else:        
                with open(file_path, "w", newline='') as file:  
                    field_names = ["name", "price", "stock"] 
                    writer = csv.DictWriter(file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerows(new_rows)
            

            
    def delete_product(self, name):
        
        file_path = "products.csv"
        
        with open(file_path, "r") as file:
            
            reader = csv.DictReader(file)
            new_rows=[]
            for row in reader:
                if name in row.values():
                    print("\n"+f"{name} deleted successfully.")
                else:
                    new_rows.append(row)
            else:        
                with open(file_path, "w", newline='') as file:  
                    field_names = ["name", "price", "stock"] 
                    writer = csv.DictWriter(file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerows(new_rows)
                        
            
            
    
    def search_product(self, name):
        
        file_path = "products.csv"
        
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if name in row.values():
                    return True
            else:
                False 
            
            
    def show_products(self):
        
        file_path = "products.csv"
        
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            
            flag=0
            for row in reader:
                print()
                flag=1
                for key, value in row.items():
                    print(key.capitalize() + " : " + value.capitalize())
            if flag==0:
                print("\n\nStorage is Empty...!")
                print("Add Products")
        
            
    def check_is_list_empty(self):    
            file_path = "products.csv" 
            list=[]
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    list.append(row)
                if len(list)==0:
                    with open(file_path, "a", newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["name", "price", "stock"])