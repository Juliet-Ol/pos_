
import os
from click import confirm
from customer import customer_menu
import product


class Purchase:
    all = []

    def __init__(self, product_name, product_price, purchase_quantity ):        

        assert product_price >= 0
        assert purchase_quantity >= 0
        # assert stock >= 0

#Assign self     
        # self.customer_id = customer_id
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
                
        if short_code == '1': 
            def search_customer_to_purchase():            
                search_customer_by_id = input("Enter customer Id:....")
                with open('newfile.txt', 'r') as fp:
                    count = 0
                    for line in fp:
                        name = line.upper()
                        line_list = name.split( )
                        if line_list[0] == search_customer_by_id + ".":
                            print(line)
                            customer = line
                        else: 
                            # line_list != search_customer_by_id + "." 
                            count += 1
                            
                            if count == number_of_records:
                                if confirm('Customer not found. Return to main menu?'):                                                               
                                    purchase_menu() 
                                else:                                     
                                    customer_menu() 
                return(customer)                    


            customer = search_customer_to_purchase() 
            # print(customer,'customer found')
            


            def make_a_purchase():
                customer = search_customer_to_purchase()
                

            make_a_purchase()             







if __name__ == "__main__":
    purchase_menu()