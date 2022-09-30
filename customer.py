class Customer:    
    
    def __init__(self,  first_name, last_name, mobile_number):

        # self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number    

    def __str__(self):
        return f" {self.first_name} {self.last_name} {self.mobile_number}\n"        
    

def customer_menu():
    print("Welcome to the customer menu")
    
    while True:
        print("""use this short codes: 
        press 1 - Create a new customer.
        press 2 - Search a customer.
        press 3 - Delete a customer. 
        press 4 - Update customer details.
        press 5 - go back to main menu""") 

        short_code = input()

    #Create a customer
        if short_code == '1':
            print("create a new customer")

            print("first name.....")  
            first_name = input()

            print("last name....")
            last_name = input()

            print("mobile_number")
            mobile_number = input()
                       
            count = 0
            with open('customer.txt') as fp:
                for line in fp:
                    if line.strip():
                        count += 1

            print('number of non-blank lines', count)
                        
            p1 = Customer(first_name, last_name, mobile_number)
            text_file = open("customer.txt","a+")
            text_file.readline()
            update_count = count +1
            print (p1)            
            
            customer_list = []
            person = (f"{update_count}. {p1.first_name} {p1.last_name} {p1.mobile_number}")
            
            customer_list.append(person)
            print(customer_list)
            for person in customer_list:
                
                try:
                    text_file.write(person + "\n").txt
                except:
                    print("there is an error")  
                      
                
            text_file.close()
            
            print('\n')
            print(f"new customer  {first_name} {last_name} {mobile_number} has been created")
            print('\n')

    #Search for a customer     

        elif short_code == '2':
            print("search for a customer")  
            print("""use this short codes: 
                press 1 - Search by first name.
                press 2 - Search by second name.
                press 3 - Phone number. 
                press 4 - Search by customer id.
                press 5 - go back to main menu""") 

            short_code = input()

            search_by = input("Search:....").upper()
            with open("customer.txt","r") as fp:
                for line in fp:
                    name = line.upper()
                    line_list = name.split( )
                    if line_list[1] == search_by:
                        print(line)

                    elif line_list[2] == search_by:
                        print(line) 

                    elif line_list[3] == search_by: 
                        print(line)

                    elif line_list[0] == search_by + ".":
                        print(line) 

    #Delete a customer 
               
                 


        elif short_code == '5':
            from pos import main_menu
        
            main_menu()

           


if __name__ == "__main__":

    customer_menu()        