#------------------------------------------------------------INVENTORY MANAGEMENT & BILLING SYSTEM------------------------------------------------

import product_management
import customer


print("\n\n----------WELCOME TO INVENTORY MANAGEMENT & BILLING SYSTEM----------")

while(True):
    print("\n1. Product Manager")
    print("2. Customer")
    print("3. Exit")
    client = input("\nSelect the option : ").lower()



    if client == "1" or client == "product manager":

        manager_name = input("\nTell me your name before further proceeding : ").capitalize()
        print("\n"+f"Hi {manager_name}!")
        print("\nWhat do you want to do?")
        
        while(True):
            
            print("\n1. Add product")
            print("2. Update product")
            print("3. Delete product")
            print("4. Search product")
            print("5. Show products")
            print("6. Exit")
            option = input("\nSelect any one of the above options : ").lower()
            
            if option == "1" or option == "add product":
                try:
                    name, price, stock = input("\nEnter Product Name, Price, Stock : ").split()
                    price, stock = map(int, (price, stock))
                    manager_obj = product_management.product_manager()
                    manager_obj.add_product(name, price, stock)
                except ValueError:
                    print("\nError : Enter three correct values separated by a space in between them!")
                    
                
            elif option == "2" or option == "update product":
                
                name = input("\nEnter the Name of the product to be updated : ").lower()
                
                manager_obj = product_management.product_manager()
                result = manager_obj.search_product(name)
                
                if result:
                    print("\n"+f"{name} Found")
                    print("\n1. Name\n2. Price\n3. Stock")
                    real_val = int(input("\nWhat do you want to change : "))
                    if real_val==1 or real_val==2 or real_val==3:
                        list=["name","price","stock"]
                        update_val = input("\nEnter the Update Value: ")
                        manager_obj.update_product(name, list[real_val-1], update_val)     
                    else:
                        print("Enter the integer value.")    
                else:
                    print("\n"+f"{name} not found")         
                    
        
            
            elif option == "3" or option == "delete product":
                
                name = input("\nEnter the Name of the product : ").lower()
                
                manager_obj = product_management.product_manager()
                result = manager_obj.search_product(name)
                
                if result:
                    manager_obj.delete_product(name)
                else:    
                    print("\n"+f"{name} not found") 
                
            
            elif option == "4" or option == "search product":
                
                name = input("\nEnter the Name of the product : ").lower()
                
                manager_obj = product_management.product_manager()
                result=manager_obj.search_product(name)
                name=name.capitalize()
                if result:
                    print("\n"+f"{name} Found")
                else:
                    print("\n"+f"{name} not found")    
                
                
                
            elif option == "5" or option == "show products":
                manager_obj = product_management.product_manager()
                manager_obj.show_products()
                
            
            elif option == "6" or option == "exit":
                break
            
            
            else:
                print("\nInvalid Option.")
            




    elif client == "2" or client == "customer":
        
        customer_name = input("\nTell me your name before further proceeding : ").capitalize()
        print("\n"+f"Hi {customer_name}!")
        print("\nWhat do you want to do?")
        
        while(True):
            print("\n1. Search products to add to cart : ")
            print("2. Show Cart Products")
            print("3. Buy Cart Products")
            print("4. Delete Cart Products")
            print("5. Exit")
            option = input("\nSelect any one of the above options : ").lower()
            
            if option == "1" or option == "search product":
                name = input("\nEnter the Name of the product : ").lower()
                    
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
                    
        
            elif option == "2" or option == "show cart products":
                customer_obj = customer.customer()
                customer_obj.show_cartProducts()   
            
                    
                    
            elif option == "3" or option == "buy cart products":
                customer_obj = customer.customer()
                cart=customer_obj.show_cartProducts() 
                
                if cart==0:
                    pass
                else:
                    customer_obj.buy_cartProducts()
                    #PRINT BILL
                    result=input("\nDo you want the bill details? (y/n)").strip()
                    if result=='y':
                            customer_obj.print_bill()
                    elif result=='n':
                        pass
                    else:
                        print("\nInvalid Option.") 
                    
            
            elif option == "4" or option == "delete cart products":
                
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
                        
            elif option == "5" or option == "exit":
                break 
            
            else:
                print("\nInvalid Option.")    
        
    elif client == "3" or client == "exit":
        break
           
    else:
        print("\nInvalid Option.")
print("\n\nEnd of Program.")