class Product:    
    
    def __init__(self, product_name, product_price):

        # self.product_id = product_Id
        self.product_name = product_name
        self.product_price = product_price
        # self.quantity = quantity    

    def __str__(self):
        return f"{self.product_name} {self.product_price} \n"         

 

def product_menu():
    print("view different products available")
    
    while True:
        print("""use this short codes: 
        press 1 - add a product, 
        press 2 - delete a product,
        press 3 - search a product, 
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
        
        p1 = Product(product_name, product_price)
        
        print (p1)
        text_file.write(f"{p1.product_name} {p1.product_price}\n")
        text_file.close()  

        print('\n')
        print(f"new product {product_name}  {product_price} has been created")
        print('\n')

if __name__ == "__main__":

    product_menu()        
        
             

           

            
            
            

          
