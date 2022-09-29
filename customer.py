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
        press 1 - to create a new customer, 
        press 2 - delete a customer,
        press 3 - search a customer, 
        press 4 - update customer details
        press 5 - go back to main menu""") 

        short_code = input()

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

            

        elif short_code == '2':
            print("search customer to delete")   
            
            def search_name():
                letter = input("enter letter: ").upper()
                IniFile = open ("customer.txt","r")
                for s in IniFile:
                    if s[0] == letter:
                    
                        print(s)
            search_name() 
                         
            # search_customer = input()
            if Customer(first_name, mobile_number):
                    
                    # search_customer = p1(search_customer)
                    search_customer = Customer(first_name, last_name, mobile_number) 
                    print(f"{search_customer.first_name} {search_customer.last_name}")
                    print('-' * 20)

                    print(f"Mobile number.......{search_customer.mobile_number}")
                    print(f"First name.......{search_customer.first_name}")
            else:
                    print("That customer does not exist")

            with open("customer.txt", "r") as file_input:
                with open("newfile.txt", "w") as output: 
                    for line in file_input:
                        if line.strip("\n") != "nickname_to_delete":
                            output.write(line)           


        elif short_code == '5':
            from pos import main_menu
        
            main_menu()

           


if __name__ == "__main__":

    customer_menu()        