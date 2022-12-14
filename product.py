


class Product:    
    
    def __init__(self, product_name, product_price, product_quantity):

        # self.product_id = product_id
        self.product_name = product_name
        self.product_price = float(product_price)
        self.product_quantity = int(product_quantity)    

    def __str__(self):
        return f"{self.product_name} {self.product_price} {self.product_quantity} \n"         

 

def product_menu():
    print('*' *49)
    print(f"\t\t Welcome to the product menu")
    print('*' *49)
    
    while True:
        print("""use this short codes: 
        press 1 - Create a product, 
        press 2 - search a product, 
        press 3 - list all products,       
        press 4 - delete a product, 
        press 5 - update product
        press 6 - go back to main menu""") 

        short_code = input()
        print('*' *49)

#Create a product
        text_file = open("product.txt","a+")
        if short_code == '1':
            def create_product():
                print("create a new product") 

                print("product name.....")  
                product_name = input()

                print("product price....")
                product_price = float(input())               

                print("product quantity....")
                product_quantity = int(input())

                count = 0
                with open('product.txt') as fp:
                    for line in fp:
                        if line.strip():
                            count += 1

                # print('number of non-blank lines', count)
                            
                p1 = Product(product_name, product_price, product_quantity)
                text_file = open("product.txt","a+")
                text_file.readline()
                update_count = count +1
                # print (p1)            
                
                product_list = []
                product = (f"{update_count}. {p1.product_name} {p1.product_price} {p1.product_quantity}")
                
                product_list.append(product)
                print(product_list)
                for product in product_list:
                    
                    try:
                        text_file.write(product + "\n").txt
                    except:
                        print(" ")                      
                    
                text_file.close()    
                
                print('\n')
                print(f"New product:... {update_count}. {product_name} price {product_price} and quantity {product_quantity} has been created.")
                print('\n')

                
                return(product_price)
                
            create_product()  

        

#Search for a product    

        elif short_code == '2':
            print("search for a product")  
            print("""use this short codes: 
                press 1 - Search product by name.
                press 2 - price.
                press 3 - product id. 
                """) 

            short_code = input()            
            search_by = input("Search product:....").lower()
            print('*' *49) 

            with open("product.txt","r") as fp:
                for line in fp:
                    item = line.upper()
                    line_list = item.split( )
                    if line_list[1] == search_by:
                        print('This is the searched product')
                        print()
                        print(line)
                        print('*' *49)

                    elif line_list[2] == search_by:
                        print('This is the searched product')
                        print()
                        print(line)
                        print('*' *49)

                    elif line_list[0] == search_by + ".":
                        print('This is the searched product')
                        print()
                        print(line) 
                        print('*' *49)   

# Print all products

        elif short_code == '3':            
            with open("product.txt", "r") as stock:
                with open("temp.txt", "w") as temp:
                    print('These are the products available:')
                    print()
                    print (stock.read())
                    print('*' *49)            
                                                        
# Update Product details                         
        elif short_code == '5':

            import os    
            

            def update_line():
                product_to_update = input("Search product id: ")     
                print('*' *49)               
                with open("product.txt", "r") as fp:
                    with open ('temp.txt', 'w') as temp:
                        for line in fp:
                            line_list = line.split( )                        
                                       
                            
                            if line_list[0] == product_to_update +".":
                                print(line)

                                pn = input('Enter product name:....')
                                pp = input('Enter product price:...') 
                                pq = input('Enter product quantity....')  

                                line=line.replace(line_list[1],pn)
                                line=line.replace(line_list[2],pp)
                                line=line.replace(line_list[3],pq)                                   
                                    
                                print('*' *49)  
                                print('Entry has been updated to' ) 
                                print()                            
                                print(line )
                                print('*' *49)
                            temp.write(line)
                import os              

                os.replace('temp.txt', 'product.txt')
            update_line()  

                        


#Delete product

        elif short_code == '4':
            def deleting_line():
                product_to_delete = input("Search product id: ")
                print('Product has been deleted')
                print('*'*49)
                print('These are the remaining products')
                print()
                
                with open("product.txt", "r") as fp:
                    with open ('temp.txt', 'w') as temp:

                        for line in fp:
                            line_list = line.split( )
                            # print(line_list[3])
                            if line_list[0] != product_to_delete+".":                                
                                print(line)
                                
                                # print('The product has been deleted')
                                temp.write(line)
                                
                import os              

                os.replace('temp.txt', 'product.txt')
                print('*' *49)
            deleting_line()                             
                         

        elif short_code == '6':
            from pos import main_menu
        
            main_menu()

if __name__ == "__main__":

    product_menu()        
        
             

           

            
            
            

          
