
# from itertools import product
from datetime import datetime
import os
from click import confirm
# from nbformat import write
from customer import customer_menu
from product import product_menu


class Purchase:
    all = []

    def __init__(self, product_name, product_price, purchase_quantity ):        

        # assert product_price >= 0
        assert purchase_quantity >= 0
        # assert inventory >= 0

#Assign self     
        self.product_name = product_name
        self.product_price = (product_price)
        self.purchase_quantity = int(purchase_quantity)
                   
    def __repr__(self):
        return f"Purchase('{self.product_name}', {self.product_price}, {self.purchase_quantity})"    

purchase_list = []
inventory = 0
# uza = []
net_price = 0
item = None
receipts =[]



def purchase_menu():
    print('*' *49)
    print(f'\t\t Welcome to Bright shop!!'.title())  
    print('*' *49)                       

    while True:
        print("""Use this short codes:
        press 1 - Make a purchase
        press 2 - list all purchases
        press 3 - to go back to the main menu""")

        short_code = input()

        count = 0
        number_of_records = 0
        
        with open('customer.txt') as fp:
            for line in fp:
                if line.strip():
                    number_of_records += 1

# Search customer who wants to purchase using id                
        if short_code == '1': 
            def search_customer_to_purchase():            
                search_customer_by_id = input("Enter customer Id:....")
                with open('customer.txt', 'r') as fp:
                    count = 0
                    for line in fp:
                        name = line.upper()
                        line_list = name.split( )
                        if line_list[0] == search_customer_by_id + ".":
                            print()
                            print('*' *49)
                            print(line)
                            customer = line
                        else:                            
                            count += 1
                            
                            if count == number_of_records:
                                if confirm('''Customer not found. press 'y' to go to purchase menu or 'n' 
                                to create a customer'''):                                                               
                                    purchase_menu() 
                                else:                                     
                                    customer_menu() 
                return(customer)               

            customer = search_customer_to_purchase()  
            # print(customer)                
         
# Search product by id on availability  
            lines_of_products = 0
            
            with open('product.txt') as fp:
                for line in fp:
                    if line.strip():
                        lines_of_products += 1
            
            def search_product_id():
                print()
                search_by = input("Search product by id:....").lower()
                with open("product.txt","r") as fp:
                    count = 0
                    for line in fp:
                        product_item = line.lower()
                        line_list = product_item.split( )                                              
                                                    
                        if line_list[0] == search_by + ".":
                            print()
                            print(line_list[0], line_list[1], line_list[2], line_list[3] )                         
                            
                                                     
                            item_name = line_list[1]  
                            item = line_list[2] 
                            rem_stock = line_list[3]                   

                        else:
                            count += 1                            
                            if count == lines_of_products:
                                if confirm('''Product not found. press 'y' to go to purchase menu or 'n' 
                                to search customer for purchase'''):                                                               
                                    make_a_purchase() 
                                else:                                     
                                    search_customer_to_purchase()                      

                return [item_name, item, rem_stock, search_by]                

#Check on quatity of stock availability
            
            lines_of_products = 0
            
            with open('product.txt') as fp:
                for line in fp:
                    if line.strip():
                        lines_of_products += 1
            
            def stock_balance():
            
                search_by = input("Search product by id:....").lower()
                with open("product.txt","r") as fp:
                    count = 0
                    for line in fp:
                        product_item = line.lower()
                        line_list = product_item.split( )                                              
                                                    
                        if line_list[0] == search_by + ".":
                            print(line_list[3])                   
                                                                                
                            stock = line_list[3]                      

                        else:
                            count += 1                            
                            if count == lines_of_products:
                                if confirm('''Quantity not enough. press 'y' to go to purchase menu or 'n' 
                                to search customer for purchase'''):                                                               
                                    make_a_purchase() 
                                    break
                                else:                                     
                                    search_customer_to_purchase()                      

                return (stock) 
                                                         
                             

# Make a purchase
            customer
            
            
            def make_a_purchase(): 
                print('*' *49)
                print()                   
                sale = input('''what would you like to buy today? Press enter to proceed:..''').lower()
                print()
                
                                
                product_name, product_price, product_quantity, product_id, = (search_product_id()) 
                # print(product_price, product_id) 
                product_name = product_name
                product_price = float(product_price)
                product_quantity = int(product_quantity)
                print('enter quantity....')
                purchase_quantity = int(input())
                product_quantity = product_quantity - purchase_quantity
                

                # global inventory
                # print('enter quantity....')
                # # stock_balance = stock_balance() - purchase_quantity
                
                # inventory = (int(stock_balance())) - purchase_quantity
                
                # for line in stock_balance():
                    
                #     if(int(stock_balance())>= purchase_quantity):
                #         inventory = int(stock_balance()) -purchase_quantity                       
                #         break                                       
                       
                #     else:
                #         print("Less Stock")
                      

                # for i in range(1,product_quantity-1):
                #     while True:
                #         print() 
                # product_quantity = product_quantity - purchase_quantity          
                
                

                        
                count = 0
                with open('purchase.txt') as fp:
                    for line in fp:
                        if line.strip():
                            count += 1
                    # print('number of non-blank lines', count)   

                    
                    text_file = open("purchase.txt","a+")
                    text_file.readline()
                    update_count = count +1
                    # print (p1)            
                    
                    total_price =  product_price * purchase_quantity 
                    global net_price
                    net_price = net_price + total_price                                  

                    # uza = [f"""{update_count}. {customer} {product_name}  price {product_price} quantity {purchase_quantity} total price {total_price} To Pay {net_price}"""]                    
                    uza = {"p_id": update_count,
                        "customer": customer,
                        "product": product_name, 
                        "quantity": purchase_quantity,  
                        "price": total_price,
                        "to pay": net_price}   


                    print('*'*49)
                    purchase_list.append(uza)
                    print(uza)
                    receipt ={
                        product_name,
                        purchase_quantity,
                        total_price
                    }
                    receipts.append(receipt)
                    print(receipts,"this is a receipt")
                      

                    print("those are the items purchased") 
                    print('*'*49)
                    if confirm("would you like to add more items...."):                       
                        make_a_purchase() 


                    else:
                        print("here are the items purchased", uza)                                                              
                        
                    text_file.write(f"{uza}\n")        
                    text_file.close()                      
          
                                  
                                 
            make_a_purchase() 

            
        
            import datetime
            # purchase_list
            # item 
            shop_name = "bright shop"
            shop_street = "Tom Mboya Sreet"
            cashier_name = "John Doe"
            now = datetime.datetime.now()
            date_time = now.strftime(("%Y-%m-%d %H:%M:%S"))                       
            receipt_message = "Thank you for doing business with us!!"                            
            
            def receipt():           

                print()
                print('=' *55 )
                print(f'\t\tReceipt')
                print(f'\t\t{shop_name.title()}')
                print(f'\t\t{shop_street}')
                print()
                print('=' *55 )
                print()             
                print(f'Customer:..{customer}')
                print('=' *55 )
                print() 
                print(f'Cashier: {cashier_name}')
                print(f'{date_time[0:10]}\t\t\t\t\t{date_time[10:]}')
                print()
                print('*' *55 )
                print('PURCHASE')
                print("product_name || product_quantity|| total_price")
                print(receipts)
                print('*' *55 )    
                print(f'Net Total (to pay)\t\t\t\t Kes{net_price:.2f}')
                print()
                print(f'\t{receipt_message}')
                print('=' *55 )               
                
            receipt() 
            print(receipt)   

        elif short_code == '2':
            with open("purchase.txt", "r") as stock:
                with open("temp.txt", "w") as temp:
                    print('These are the products available:')
                    print()
                    print (stock.read())
                    print('*' *49)      

        elif short_code == '3':
            from pos import main_menu        
            main_menu()


if __name__ == "__main__":
    purchase_menu()