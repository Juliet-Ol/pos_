class Product:    
    
    def __init__(self, product_name, product_quantity):

        # self.customer_id = customer_Id
        self.product_name = product_name        
        self.product_quantity = product_quantity 

    def __str__(self):
        return f"{self.product_name} {self.product_quantity}\n"   


def product_menu():
    print("Welcome to the product menu")  

    while True:
        print("""use this short codes: 
        press 1 - to create a new product, 
        press 2 - delete a product,
        press 3 - search a product, 
        press 4 - update product details
        press 5 - go back to main menu""") 

        short_code = input()          


        text_file = open("product.txt","a+")
        if short_code == '1':
            print("create a new product") 

        product_name = input("enter product name:....")
        
        product_quantity = input("enter product quantity ....")


        p1 = Product(product_name, product_quantity)
        
        print (p1)
        text_file.write(f"{p1.product_name} {p1.product_quantity}\n").txt
        text_file.close  

product_menu()        