
# from itertools import product
import os

import email
# from multiprocessing import context
from datetime import datetime
from click import confirm
# from nbformat import write
from customer import customer_menu
from product import product_menu
from gmail import send_receipt
from email.message import EmailMessage


# import sys
# import fileinput
# import smtplib




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
net_price = 0
item = None
receipt1 =[]



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
                    for customer_line in fp:
                        customer_line_list = customer_line.split()
                        if customer_line_list[0] == search_customer_by_id + ".":
                            print(f'Selected {customer_line_list[1]}')
                            print('*' *49)
                            full_name = customer_line_list[1] +" "+ customer_line_list[2]
                            email = customer_line_list[4]
                        else:                            
                            count += 1
                            
                            if count == number_of_records:
                                if confirm('''Customer not found. press 'y' to go to purchase menu or 'n' 
                                to create a customer'''):                                                               
                                    purchase_menu() 
                                else:                                     
                                    customer_menu() 
                return [full_name, email]            

            full_name, email = search_customer_to_purchase()  
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
            
# Make a purchase
            
            
            inventory = []

            def provide_quantity(product_quantity):
                print(f'Enter quantity: [1-{product_quantity}]')
                print(full_name)
                purchase_quantity = int(input("Enter quantity:.."))
                if (purchase_quantity > product_quantity):
                    print(f'Not enough Stock. Available stock is {product_quantity}')
                    provide_quantity(product_quantity)
                
                return purchase_quantity
            
            def make_a_purchase(): 

                print('*' *49)
                print()                   
                sale = input('''what would you like to buy today? Press enter to proceed:..''').lower()
                print()                
                                
                product_name, raw_product_price, raw_product_quantity, product_id, = (search_product_id()) 
                # print(product_price, product_id) 
                product_name = product_name
                product_price = float(raw_product_price)
                product_quantity = int(raw_product_quantity)
                # print('enter quantity....')
                purchase_quantity = provide_quantity(product_quantity)
                
                        
                count = 0
                with open('purchase.txt') as fp:
                    for line in fp:
                        if line.strip():
                            count += 1                   

                    
                    text_file = open("purchase.txt","a+")
                    text_file.readline()
                    update_count = count +1
                             
                    
                    total_price =  product_price * purchase_quantity 
                    global net_price
                    net_price = net_price + total_price                              
                   
                    
                    remaining_stock = int(raw_product_quantity) - purchase_quantity
                    x = f'{product_name} {raw_product_price} {raw_product_quantity}'
                    y = f'{product_name} {raw_product_price} {remaining_stock}'

                    from pathlib import Path
                    file = Path('product.txt')
                    file.write_text(file.read_text().replace(x, y))

                    print(full_name)
                    print(email)
                                        
                    uza = {"purchase_id": update_count,
                        "customer": full_name,
                        "product": product_name, 
                        "quantity": purchase_quantity,  
                        "price": total_price,
                        "to pay": net_price} 

                   

                    text_file.write(f"{uza}\n")        
                    text_file.close()

                    print('*'*49)
                    purchase_list.append(uza)
                    print(f"""{update_count}. {full_name} {product_name}  price {product_price} quantity {purchase_quantity} total price {total_price} To Pay {net_price}""")

                    receipts = [product_name, purchase_quantity, total_price] 
                
                        

                    for receipts in receipts:
                        receipt1.append(receipts)
                        print(receipts)
                      

                    print("those are the items purchased") 
                    print('*'*49)
                    if confirm("would you like to add more items...."):                       
                        make_a_purchase() 


                    else:
                        print("here are the items purchased", uza)                                                              
                        
                                          
          
                             
                                 
            make_a_purchase()
            send_receipt(full_name, email, purchase_list)

            
        
            import datetime
            
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
                print(f'Customer: {full_name}')
                print('=' *55 )
                print() 
                print(f'Cashier: {cashier_name}')
                print(f'{date_time[0:10]}\t\t\t\t\t{date_time[10:]}')
                print()
                print('*' *55 )
                print('PURCHASE')
                print("product_name || product_quantity|| total_price")
                # print(f'{receipt1[0]}\t\t {receipt1[1]}\t\t {receipt1[2]}')
                for receipt in receipt1:
                    print(receipt)
                print(f'{receipt1[0]}  {receipt1[1]} {receipt1[2]}')
                print('*' *55 )    
                print(f'Net Total (amount paid)\t\t\t\t Kes {net_price:.2f}')
                print()
                print(f'\t{receipt_message}')
                print('=' *55 )               
                
            receipt() 
            print(receipt)
            
            # import ssl
            # from pathlib import Path             
  
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