class Product:    
    
    def __init__(self, product_name, product_price, product_quantity):

        # self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity    

    def __str__(self):
        return f"{self.product_name} {self.product_price} {self.product_quantity} \n"         

 

def product_menu():
    print("view different products available")
    
    while True:
        print("""use this short codes: 
        press 1 - add a product, 
        press 2 - search a product,
        press 3 - delete a product, 
        press 4 - update product
        press 5 - go back to main menu""") 

        short_code = input()

        text_file = open("product.txt","a+")
        if short_code == '1':
            print("create a new product") 

            print("product name.....")  
            product_name = input()

            print("product price....")
            product_price = input()

            print("product quantity....")
            product_quantity = input()
            
            p1 = Product(product_name, product_price, product_quantity)
            
            print (p1)
            text_file.write(f"{p1.product_name} {p1.product_price} {p1.product_quantity}\n")
            text_file.close()  

            print('\n')
            print(f"new product {product_name} {product_price} {product_quantity} has been created")
            print('\n')


    #Search for a product    

        elif short_code == '2':
            print("search for a product")  
            print("""use this short codes: 
                press 1 - Search product by name.
                press 2 - price.
                press 3 - product id. 
                press 5 - print all products""") 

            short_code = input()

            search_by = input("Search:....").upper()
            with open("product.txt","r") as fp:
                for line in fp:
                    item = line.upper()
                    line_list = item.split( )
                    if line_list[0] == search_by:
                        print(line)

                    elif line_list[1] == search_by:
                        print(line)

            # Print all the data on the database
            with open("product.txt", "r") as f:
                print (f.read())               
                         

        elif short_code == '5':
            from pos import main_menu
        
            main_menu()

if __name__ == "__main__":

    product_menu()        
        
             

           

            
            
            

          
