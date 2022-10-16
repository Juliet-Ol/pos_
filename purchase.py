
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


def purchase_menu():
    print('''Welcome to bb shop.''')                         

    while True:
        print("""Use this short codes:
        press 1 - Make a purchase
        press 2 - to go back to the product menu
        press 3 to go back to the main menu""")

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
            
       
# search product availability

            lines_of_products = 0
            
            with open('product.txt') as fp:
                for line in fp:
                    if line.strip():
                        lines_of_products += 1
            
            def search_product_id():
            
                search_by = input("Search product by id:....").lower()
                with open("product.txt","r") as fp:
                    count = 0
                    for line in fp:
                        product_item = line.lower()
                        line_list = product_item.split( )                                              
                                                    
                        if line_list[0] == search_by + ".":
                            print(line_list[0], line_list[1], line_list[2])                         
                            
                                                     
                            item = line_list[2]                      

                        else:
                            count += 1                            
                            if count == lines_of_products:
                                if confirm('''Product not found. press 'y' to go to purchase menu or 'n' 
                                to search customer for purchase'''):                                                               
                                    make_a_purchase() 
                                else:                                     
                                    search_customer_to_purchase()                      

                return [item, search_by]  

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
                                else:                                     
                                    search_customer_to_purchase()                      

                return (stock) 
                                                         
                             

# Make a purchase
            customer
            
            
            def make_a_purchase():                          
                                      
                sale = input('''what would you like to buy today? Press enter to proceed:..''').lower()

                product_name = None
                print()

                product_price, product_id = (search_product_id()) 
                # print(product_price, product_id) 
                product_price = float(product_price)

                global inventory
                print('enter quantity....')
                # stock_balance = stock_balance() - purchase_quantity
                purchase_quantity = int(input())
                # inventory = (int(stock_balance())) - purchase_quantity
                
                # for line in stock_balance():
                    # if(int(stock_balance())>= purchase_quantity):                   

                    #     inventory = int(stock_balance()) -purchase_quantity
                    # else:
                    #     print("Less Stock")

                       

                # for i in range(1,product_quantity-1):
                #     while True:
                #         print() 
                # product_quantity = product_quantity - purchase_quantity          
                
                

                        
                count = 0
                with open('purchase.txt') as fp:
                    for line in fp:
                        if line.strip():
                            count += 1
                    print('number of non-blank lines', count)   

                    
                    text_file = open("purchase.txt","a+")
                    text_file.readline()
                    update_count = count +1
                    # print (p1)            
                    
                    total_price =  product_price * purchase_quantity 
                    global net_price
                    net_price = net_price + total_price
                     

                    uza = [f"""{update_count}. {customer} 
                                {product_name} 
                                {product_price} 
                                {purchase_quantity}""",  
                                product_name, total_price, net_price]                    
                    
                    purchase_list.append(uza)
                    print(uza)
                      

                    print("those are the items purchased") 

                    if confirm("would you like to add more items...."):                       
                        make_a_purchase() 


                    else:
                        print("here are the items purchased", uza)                                                              
                        
                    text_file.write(f"{uza}\n")         
                            
                    text_file.close()                          
          
                    # print("here are the items purchased", sale)               
                                 
            make_a_purchase() 

            
            # def receipt():
            #     count = 0
            #     with open('receipt.txt') as f:
            #         for line in f:
            #             if line.strip():
            #                 count += 1
            #         print('number of non-blank lines', count)   

                    
            #         text_file = open("purchase.txt","a+")
            #         text_file.readline()
            #         update_count = count +1

            # receipt()
            # print(receipt)
            import datetime
            purchase_list
            item 
            shop_name = "bright shop"
            shop_street = "Tom Mboya Sreet"
            cashier_name = "John Doe"
            now = datetime.datetime.now()
            date_time = now.strftime(("%Y-%m-%d %H:%M:%S"))
            purchase_quantity = "purchase quantity"
            product_price = "product price"
            receipt_message = "Thank you for doing business with us!!"

                            
            
            def receipt():
                


                print()
                print('*' *55 )
                print(f'\t\tReceipt')
                print(f'\t\t{shop_name.title()}')
                print(f'\t\t{shop_street}')
                print()
                print('*' *55 )
                print()             
                print(f'Customer:\t{customer}')
                print('*' *55 )
                print() 
                print(f'Cashier: {cashier_name}')
                print(f'{date_time[0:10]}\t\t\t\t\t{date_time[10:]}')
                print()
                print('*' *55 )
                print('PURCHASE')
                # print(f'{product_price} {total_price}')
                print(purchase_list)
                print(product_price)
                print('=' *55 )    
                print(f'Net Total\t\t\t Kes{net_price:.2f}')
                print()
                print(f'\t{receipt_message}')
                print('=' *55 )               
                
            receipt() 
            print(receipt)   

        elif short_code == '3':
            from pos import main_menu        
            main_menu()


if __name__ == "__main__":
    purchase_menu()