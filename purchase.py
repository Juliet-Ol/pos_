
import os
from click import confirm
from customer import customer_menu
from product import product_menu


class Purchase:
    all = []

    def __init__(self, product_name, product_price, purchase_quantity ):        

        assert product_price >= 0
        assert purchase_quantity >= 0
        # assert stock >= 0

#Assign self     
        self.product_name = product_name
        self.product_price = float(product_price)
        self.purchase_quantity = int(purchase_quantity)
        # self.stock = int(stock)

           
    def __repr__(self):
        return f"Purchase('{self.product_name}', {self.product_price}, {self.purchase_quantity})"    


sale = []
total = []
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

# Open product file to check availability
            def make_a_purchase():
                customer
                with open("testproduct.txt", "r") as stock:
                    with open("temp.txt", "w") as temp:
                        print (stock.read())            #prints stock available
                        for line in stock:
                            if line == stock:
                                # stock.append(line)
                                print(line)            
# Enter what you are purchasing

                        purchase_list = input('''what would you like to buy today? Press enter to proceed:..''').lower()

                        print('enter product.....')
                        product_name =input ()

                        print('enter quantity....')
                        purchase_quantity = int(input())
                        
                        
                        print('enter price....')
                        product_price = float(input())  

                        
                count = 0
                with open('purchase.txt') as fp:
                    for line in fp:
                        if line.strip():
                            count += 1

                    print('number of non-blank lines', count)   

                    purchase_list = input('''this has been added to your sale''').lower()         
                                
                    p1 = Purchase(product_name, product_price, purchase_quantity)
                    text_file = open("purchase.txt","a+")
                    text_file.readline()
                    update_count = count +1
                    print (p1)            
                    
                    purchase_list = []                                                          #include customer name
                    uza = (f"{update_count}.{customer} {p1.product_name} {p1.product_price} {p1.purchase_quantity}", product_price * purchase_quantity) 
                    
                    purchase_list.append(uza)
                    print(purchase_list)
                    for uza in purchase_list:  

                        print("those are the items purchased") 

                    if confirm("would you like to add more items...."):
                        make_a_purchase()    
                    # if more_purchase == "y":

                    else:
                        print("here are the items purchased", uza)                                      
                        
                    text_file.write(f"{uza}\n")         
                            
                    text_file.close()                          
          

                    print("here are the items purchased", sale)           
                 
                

            make_a_purchase()         

if __name__ == "__main__":
    purchase_menu()