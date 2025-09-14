import csv
import os
class product_manager:
    
    def add_product(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

        file_path = "products.csv"
        field_names = ["id", "name", "price", "stock"]

        product_id = 1001

        # Check if file exists
        if os.path.exists(file_path):
            with open(file_path, "r", newline='') as file:
                reader = list(csv.DictReader(file))
                if reader:  # File not empty
                    last_id = int(reader[-1]["id"])
                    product_id = last_id + 1  # Increment id

                for row in reader:
                    if row["name"] == self.name:
                        print(f"\n{self.name} already exists!")
                        print("Select the Update option to update it.")
                        return
    
        new_row = {"id": product_id, "name": self.name, "price": self.price, "stock": self.stock}

        # Write to file
        if not os.path.exists(file_path):  # Create file with header
            with open(file_path, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
                writer.writerow(new_row)
        else:  # Append row
            with open(file_path, "a", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writerow(new_row)

        print("\nProduct added successfully.")

                
            
        
    
    def update_product(self, name, real_val, update_val):
        file_path = "products.csv"
        try:
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
                        field_names = ["id","name", "price", "stock"] 
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(new_rows)
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            print("Add Products")
            

            
    def delete_product(self, name):
        
        file_path = "products.csv"
        try:
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
                        field_names = ["id","name", "price", "stock"] 
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(new_rows)
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            print("Add Products")
            
            
    
    def search_product(self, name):
        
        file_path = "products.csv"
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    if name in row.values():
                        return True
                else:
                    False 
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            print("Add Products")
            
            
    def show_products(self):
        
        file_path = "products.csv"
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                print()
                flag=0
                id_width=10
                name_width = 19
                price_width = stock_width = 17
                print(f"\n{'ID'.ljust(id_width)}{'Name'.ljust(name_width)}{'Stock'.ljust(price_width)}{'Price'.ljust(stock_width)}\n")
                for row in reader:
                    flag=1
                    print(
                        f"{row['id'].ljust(id_width)}"
                        f"{row['name'].capitalize().ljust(name_width)}"
                        f"{row['stock'].ljust(stock_width)}"
                        f"Rs.{row['price']}".ljust(price_width)
                        )
                print()
                if flag==0:
                    print("\n\nStorage is Empty...!")
                    print("Add Products")
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            print("Add Products")
            
        
            
    def check_is_list_empty(self):    
            file_path = "products.csv" 
            list=[]
            try:
                with open(file_path, "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        list.append(row)
                    if len(list)==0:
                        with open(file_path, "a", newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(["name", "price", "stock"])
            except FileNotFoundError:
                print("\n\nStorage is Empty...!")
                print("Add Products")
                
                
    def total_sales(self):
        total_sales_filepath="total_sales.csv"
        try:
            with open(total_sales_filepath, "r") as file:
                reader = csv.DictReader(file)
                total_items_saled=0
                total_sales=0
                id_width=10
                name_width = 19
                price_width = stock_width = 17
                print(f"\n{'ID'.ljust(id_width)}{'Name'.ljust(name_width)}{'Saled'.ljust(stock_width)}{'Price(per item)'.ljust(price_width)}\n")
                for row in reader:
                    print(
                            f"{row['id'].ljust(id_width)}"
                            f"{row['name'].capitalize().ljust(name_width)}"
                            f"{row['stock'].ljust(stock_width)}"
                            f"{row['price'].ljust(price_width)}"
                    )
                    total_items_saled+=int(row['stock'])
                    total_sales+=int(row['price'])
                else:
                    print(f"\n\nTotal items sold : {total_items_saled}")                   
                    print(f"Total Sales : {total_sales}")
        except FileNotFoundError:
            print("\nNo Sales found yet!")
        
    def low_stocks(self):
        file_path = "products.csv" 
        try:
            with open(file_path, "r") as file:
                reader = csv.DictReader(file)
                print("\nProducts having stock less than 10")
                id_width=10
                name_width = 19
                price_width = stock_width = 17
                print(f"\n{'ID'.ljust(id_width)}{'Name'.ljust(name_width)}{'Stock'.ljust(stock_width)}\n")
                for row in reader:
                    if int(row['stock'])<=10:
                        print(
                            f"{row['id'].ljust(id_width)}"
                            f"{row['name'].capitalize().ljust(name_width)}"
                            f"{row['stock'].ljust(stock_width)}"
                        )
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            print("Add Products")