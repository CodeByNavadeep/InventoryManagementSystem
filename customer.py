import csv
import datetime
import copy

class customer:
    
    bill_details=[]
    total=0
    
    def search_products_inStorage(self, name):
        file_path = "products.csv"
        
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if name in row.values():
                    return True
            else:
                False 
    
    def search_products_inCart(self, name):
        file_path = "customercart.csv"
        
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if name in row.values():
                    return True
            else:
                False 
                
    def add_to_cart(self, name):
        product_filepath = "products.csv"
        
        cart_filepath = "customercart.csv"
        
        item_in_cart = "unfound"
                      
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
                    field_names = ["name", "price", "stock"] 
                    writer = csv.DictWriter(file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerows(new_rows)
                    name=name.capitalize()
                    print("\n"+f"{name} stock incremented to {count} in cart successfully.")       
            else:           
                with open(product_filepath, 'r') as product_file:
                    reader=csv.DictReader(product_file)
                    for row in reader:
                        if name in row.values():
                            row["stock"]=1
                            with open(cart_filepath, 'a', newline='') as customer_file:
                                fieldnames=["name", "price", "stock"]
                                writer=csv.DictWriter(customer_file, fieldnames=fieldnames)
                                writer.writerow(row)
                                name=name.capitalize()
                                print("\n"+f"{name} added to cart successfully.")
                        
    
    
    
    def show_cartProducts(self):
        cart_filepath="customercart.csv"
        
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
        
            
                
            
    def buy_cartProducts(self):
        cart_filepath="customercart.csv"
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
                        field_names = ["name", "price", "stock"] 
                        writer = csv.DictWriter(file, fieldnames=field_names)
                        writer.writeheader()
                        writer.writerows(new_rows)                 
        #UPDATE CART
        cart_filepath = "customercart.csv"
        with open(cart_filepath, "w", newline='') as file:
            field_names = ["name", "price", "stock"]
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
                
    
    def print_bill(self):
        print("\n\n---------------------------BILL DETAILS---------------------------")
        print("\n"+" "*38,end="")
        print(datetime.datetime.now())
        max_name_len=max([len(row["name"]) for row in self.bill_details])
        for row in self.bill_details:
            name=row["name"].capitalize()
            print("\n"+f"{self.bill_details.index(row)+1}. {name}({row["stock"]})"+ (max_name_len-len(row["name"])+10)*" " + f"Rs.{int(row["stock"])*int(row["price"])}")     
        print("-"*(max_name_len+10)+"---------------------")
        print("Grand Total"+" "*11+f"Rs.{self.total}")
        print("\nThankyou.")
        print("-"*67)
        
        customer_bill_text_file="customerbill.txt"
        #PRINTING BILL IN .TXT FILE
        with open(customer_bill_text_file, 'w') as file:
            file.write("---------------------------BILL DETAILS---------------------------\n")
            now=datetime.datetime.now()
            current_time=now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(" "*46)
            file.write(current_time)
            max_name_len=max([len(row["name"]) for row in self.bill_details])
            for row in self.bill_details:
                name=row["name"].capitalize()
                file.write("\n"+f"{self.bill_details.index(row)+1}. {name}({row["stock"]})"+ (max_name_len-len(row["name"])+10)*" " + f"Rs.{int(row["stock"])*int(row["price"])}")     
            file.write("\n"+"-"*(max_name_len+10)+"---------------------")
            file.write("\n"+"Grand Total"+" "*11+f"Rs.{self.total}")
            file.write("\nThankyou.")
            file.write("\n"+"-"*67)
                       
    
    def delete_product(self, name):
        
        file_path = "customercart.csv"
        
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