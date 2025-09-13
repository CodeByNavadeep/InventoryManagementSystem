#------------------------------------------------------------INVENTORY MANAGEMENT & BILLING SYSTEM------------------------------------------------

import product_management
import customer
import time

print("\n\n----------WELCOME TO INVENTORY MANAGEMENT & BILLING SYSTEM----------")

while(True):
    print("\n1. Product Manager")
    print("2. Customer")
    print("3. Exit")
    client = input("\nSelect the option : ").lower()

    if client == "1" or client == "product manager":

        manager_name = input("\nTell me your name before further proceeding : ").capitalize()
        print("\n"+f"Hi {manager_name}!")
        time.sleep(0.5)
        print("\nWhat do you want to do?")
        time.sleep(0.5)
        
        while(True):
            
            print("\n1. Show products")
            print("2. Add product")
            print("3. Update product")
            print("4. Delete product")
            print("5. Search product")
            print("6. View total sales")
            print("7. Check low Stocks")
            print("8. Exit")
            option = input("\nSelect any one of the above options : ").lower()
            
            if option == "1" or option == "show products":
                time.sleep(0.5)
                manager_obj = product_management.product_manager()
                manager_obj.show_products()
                time.sleep(0.5)
                
                
            elif option == "2" or option == "add product":
                time.sleep(0.5)
                try:
                    name, price, stock = input("\nEnter Product Name, Price, Stock : ").split()
                    price, stock = map(int, (price, stock))
                    manager_obj = product_management.product_manager()
                    manager_obj.add_product(name, price, stock)
                except ValueError:
                    print("\nError : Enter three correct values separated by a space in between them!")
                time.sleep(0.5)   
                
                
            
            elif option == "3" or option == "update product":
                
                name = input("\nEnter the Name of the product to be updated : ").lower()
                
                manager_obj = product_management.product_manager()
                result = manager_obj.search_product(name)
                time.sleep(0.5)
                if result:
                    print("\n"+f"{name} Found")
                    time.sleep(0.5)
                    print("\n1. Name\n2. Price\n3. Stock")
                    try:
                        real_val = int(input("\nWhat do you want to change : "))
                    except ValueError as e:
                        print("\nSelect the valid integer option")
                    else:
                        list=["name","price","stock"]
                        update_val = input("\nEnter the Update Value: ")
                        manager_obj.update_product(name, list[real_val-1], update_val)     
                else:
                    print("\n"+f"{name} not found")         
                time.sleep(0.5)    
        
            
            
            elif option == "4" or option == "delete product":
                
                name = input("\nEnter the Name of the product : ").lower()
                
                manager_obj = product_management.product_manager()
                result = manager_obj.search_product(name)
                time.sleep(0.5)
                if result:
                    manager_obj.delete_product(name)
                else:    
                    print("\n"+f"{name} not found") 
                time.sleep(0.5)
                
                
            elif option == "5" or option == "search product":
                name = input("\nEnter the Name of the product : ").lower()
                time.sleep(0.5)
                manager_obj = product_management.product_manager()
                result=manager_obj.search_product(name)
                name=name.capitalize()
                if result:
                    print("\n"+f"{name} Found")
                else:
                    print("\n"+f"{name} not found")    
                time.sleep(0.5)
                
                
            elif option == "6" or option == "total sales":
                time.sleep(0.5)
                manager_obj = product_management.product_manager()
                manager_obj.total_sales()
                time.sleep(0.5)    
            
            elif option == "7" or option == "low stock":
                time.sleep(0.5)
                manager_obj = product_management.product_manager()
                manager_obj.low_stocks()
                time.sleep(0.5)
            
            elif option == "8" or option == "exit":
                break
            
            
            else:
                print("\nInvalid Option.")

    elif client == "2" or client == "customer":
        
        customer_name = input("\nTell me your name before further proceeding : ").capitalize()
        print("\n"+f"Hi {customer_name}!")
        time.sleep(0.5)
        print("\nWhat do you want to do?")
        time.sleep(0.5)
        
        while(True):
            print("\n1. List all the products in the mall")
            print("2. Add products to cart")
            print("3. Show Cart Products")
            print("4. Buy Cart Products")
            print("5. Delete Cart Products")
            print("6. Exit")
            option = input("\nSelect any one of the above options : ").lower()
            
            if option == "1" or option == "list products":
                time.sleep(0.5)
                customer_obj=customer.customer()
                customer_obj.list_products()
                time.sleep(0.5)
            
            elif option == "2" or option == "search product":
                name = input("\nEnter the Name of the product : ").lower()
                time.sleep(0.5)
                customer_obj = customer.customer()
                result=customer_obj.search_products_inStorage(name)
                if result:
                    print("\n"+f"{name} Found")
                    result=input("\nAdd to cart? (y/n) : ").lower()
                    if result=='y':
                        customer_obj.add_to_cart(name)
                    elif result=='n':
                        pass
                    else:
                        print("\nInvalid Option.")    
                else:
                    print("\n"+f"{name} not found")    
                time.sleep(0.5) 
        
        
            elif option == "3" or option == "show cart products":
                time.sleep(0.5)
                customer_obj = customer.customer()
                customer_obj.show_cartProducts()   
                time.sleep(0.5)
            
                    
                    
            elif option == "4" or option == "buy cart products":
                time.sleep(0.5)
                customer_obj = customer.customer()
                cart=customer_obj.show_cartProducts() 
                
                if cart==0:
                    pass
                else:
                    customer_obj.buy_cartProducts()
                    #PRINT BILL
                    result=input("\nDo you want the bill details? (y/n)").strip()
                    if result=='y':
                            customer_obj.print_bill(customer_name)
                    elif result=='n':
                        pass
                    else:
                        print("\nInvalid Option.") 
                time.sleep(0.5)
                    
            
            elif option == "5" or option == "delete cart products":
                time.sleep(0.5)
                customer_obj = customer.customer()
                cart=customer_obj.show_cartProducts()
                
                if cart==0:
                    pass
                else:
                    name = input("\nEnter the Name of the product : ").lower()
                    
                    
                    result = customer_obj.search_products_inCart(name)
                    
                    if result:
                        customer_obj.delete_product(name)
                    else:    
                        print("\n"+f"{name} not found") 
                time.sleep(0.5)
                
            elif option == "6" or option == "exit":
                break 
            
            else:
                print("\nInvalid Option.")    
        
    elif client == "3" or client == "exit":
        break
           
    else:
        print("\nInvalid Option.")
print("\n\nEnd of Program.")