import csv
import datetime
import copy
import os
import shutil
class customer:
    
    bill_details=[]
    total=0
    
    def list_products(self):
        file_path = "products.csv"
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                print()
                flag=0
                name_width = 19
                price_width = 17
                print(f"\n{'Name'.ljust(name_width)}{'Price'.ljust(price_width)}\n")
                for row in reader:
                    flag=1
                    print(
                        f"{row['name'].capitalize().ljust(name_width)}"
                        f"Rs.{row['price']}".ljust(price_width)
                        )
                print()
                if flag==0:
                    print("\n\nStorage is Empty...!")
                    print("Add Products")
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            
            
    
    def search_products_inStorage(self, name):
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

                
    
    
    def search_products_inCart(self, name):
        file_path = "customercart.csv"
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
            
            
                
    def add_to_cart(self, name):
        product_filepath = "products.csv"
        
        cart_filepath = "customercart.csv"
        
        item_in_cart = "unfound"
        #Check Stock is Available or Not
        try:
            with open(product_filepath, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if name in row.values():
                        if int(row['stock'])<=1:
                            print("\nStock is unavailable.")
                            print("Please try after some time.")
                            return
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            return
        if os.path.exists(cart_filepath):
            #Incrementing Stock if the product exists already
            with open(cart_filepath, "r") as file:
                reader = csv.DictReader(file)
                new_rows=[]
                for row in reader:
                    if name in row.values():
                        count=int(row["stock"])+1
                        row["stock"]=count
                        item_in_cart = "found"
                        new_rows.append(row)
                    else:
                        new_rows.append(row)
                if item_in_cart == "found":     
                    with open(cart_filepath, "w", newline='') as file:  
                        field_names = ["id", "name", "price", "stock"] 
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(new_rows)
                        name=name.capitalize()
                        print("\n"+f"{name} stock incremented to {count} in cart successfully.")   
                        
                #Adding the product if it isn't in cart    
                else:           
                    with open(product_filepath, 'r') as product_file:
                        reader=csv.DictReader(product_file)
                        for row in reader:
                            if name in row.values():
                                row["stock"]=1
                                with open(cart_filepath, 'a', newline='') as customer_file:
                                    fieldnames=["id", "name", "price", "stock"]
                                    writer=csv.DictWriter(customer_file, fieldnames=fieldnames)
                                    writer.writerow(row)
                                    name=name.capitalize()
                                    print("\n"+f"{name} added to cart successfully.")
                        
    
    
    
    def show_cartProducts(self):
        cart_filepath="customercart.csv"
        try:
            with open(cart_filepath, 'r') as customer_file:
                reader=csv.DictReader(customer_file)
                flag=0
                for row in reader:
                    print()
                    flag=1
                    for key, value in row.items():
                        print(key.capitalize() + " : " + value.capitalize())
                if flag==0:
                    print("\n\nStorage is Empty...!")
                    print("Add Products to cart")
                    return 0
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")
            
                
            
    def buy_cartProducts(self):
        cart_filepath="customercart.csv"
        total_sales_filepath="total_sales.csv"
        shutil.copyfile(cart_filepath, total_sales_filepath)
        delete_rows = []
        with open(cart_filepath, 'r') as customer_file:
            reader=csv.DictReader(customer_file)
            for row in reader:
                self.bill_details.append(row)
                self.total += int(row["price"]) * int(row["stock"])
                delete_rows.append(row)
            print("\n"+f"The Total Cost of Products is Rs.{self.total}.")      
        #UPDATE STORAGE
        for cart_row in delete_rows:
            name=cart_row["name"]
            product_filepath = "products.csv"
            with open(product_filepath, "r") as file:
                reader = csv.DictReader(file)
                new_rows=[]
                for row in reader:
                    if name in row.values():
                        row["stock"]=int(row["stock"])-int(cart_row["stock"])
                        new_rows.append(row)
                    else:
                        new_rows.append(row)
                else:        
                    with open(product_filepath, "w", newline='') as file:  
                        field_names = ["id", "name", "price", "stock"] 
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(new_rows)                 
        #UPDATE CART
        cart_filepath = "customercart.csv"
        with open(cart_filepath, "w", newline='') as file:
            field_names = ["id", "name", "price", "stock"]
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
                
                
    
    def print_bill(self, customer_name):
        print("\n\n---------------------------BILL DETAILS---------------------------")
        print("\n"+" "*38,end="")
        print(datetime.datetime.now())
        max_name_len=max([len(row["name"]) for row in self.bill_details])
        # Define column widths
        name_width = max_name_len + 10
        stock_width = 25
        price_width = 17
        # Header
        print(f"\n{'Name'.ljust(name_width)}{'No.Of Items'.ljust(stock_width)}{'Price(per item)'.ljust(price_width)}\n")
        for row in self.bill_details:
            name=row["name"].capitalize()
            # Row
            print(
                    f"{self.bill_details.index(row)+1}. {name.ljust(name_width)}"
                    f"{str(row['stock']).ljust(stock_width)}"
                    f"Rs.{int(row['stock']) * int(row['price'])}".ljust(price_width)
                )
        print()
        print("-"*(max_name_len+10)+"---------------------")
        print("Grand Total"+" "*15+f"Rs.{self.total}")
        print(f"\nThankyou {customer_name.capitalize()}😊.")
        print("-"*67)
        customer_bill_text_file="customerbill.txt"
        #PRINTING BILL IN .TXT FILE
        with open(customer_bill_text_file, 'w', encoding='utf-8') as file:
            file.write("---------------------------BILL DETAILS---------------------------\n")
            now=datetime.datetime.now()
            current_time=now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(" "*46)
            file.write(current_time)
            max_name_len=max([len(row["name"]) for row in self.bill_details])
            # Header
            file.write("\n\n"+f"{'Name'.ljust(name_width)}{'No.Of Items'.ljust(stock_width)}{'Price(per item)'.ljust(price_width)}"+"\n\n")
            for row in self.bill_details:
                name=row["name"].capitalize()
                file.write(
                    f"{self.bill_details.index(row)+1}. {name.ljust(name_width)}"
                    f"{str(row['stock']).ljust(stock_width)}"
                    f"Rs.{int(row['stock']) * int(row['price'])}".ljust(price_width)+"\n"
                )   
            file.write("\n"+"-"*(max_name_len+10)+"---------------------")
            file.write("\n"+"Grand Total"+" "*15+f"Rs.{self.total}"+"\n")
            file.write("\n"+f"Thankyou {customer_name.capitalize()}😊.")
            file.write("\n"+"-"*67)
                       
    
    def delete_product(self, name):
        
        file_path = "customercart.csv"
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
                        field_names = ["id", "name", "price", "stock"] 
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(new_rows)
        except FileNotFoundError:
            print("\n\nStorage is Empty...!")