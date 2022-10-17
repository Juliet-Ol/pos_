class Customer:    
    
    def __init__(self,  first_name, last_name, mobile_number, email):
        

        # self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number 
        self.email = email 


    def __str__(self):
        return f" {self.first_name} {self.last_name} {self.mobile_number} {self.mobile_number}\n"        
    

def customer_menu():
    print('*' *49)
    print(f"\t\tWelcome to the customer menu")
    print('*' *49)
    
    while True:
        print("""use this short codes: 
        press 1 - Create a new customer.
        press 2 - Search a customer.         
        press 3 - Update customer details.
        press 4 - Delete a customer.
        press 5 - list all customers
        press 6 - go back to main menu""") 

        short_code = input()
        print('*' *49)
        

#Create a customer
        if short_code == '1':
            def create_a_customer():
                print("Create a new customer")
                print()

                print("Enter first name:.....")  
                first_name = input()
                print()

                print("Enter last name:....")
                last_name = input()
                print()

                print("Enter mobile_number:..")
                mobile_number = input()
                print()

                print("Enter email address:...")
                email = input()
                print()
                        
                count = 0
                with open('customer.txt') as fp:
                    for line in fp:
                        if line.strip():
                            count += 1

                # print('number of non-blank lines', count)
                            
                p1 = Customer(first_name, last_name, mobile_number, email)
                text_file = open("customer.txt","a+")
                text_file.readline()
                update_count = count +1
                # print (p1)            
                
                customer_list = []
                person = (f"{update_count}. {p1.first_name} {p1.last_name} {p1.mobile_number} {p1.email}")
                
                customer_list.append(person)
                print(customer_list)
                for person in customer_list:
                    
                    try:
                        text_file.write(person + "\n")
                    except:
                        print("there is an error")                        
                    
                text_file.close()
                
                print('\n')
                print(f"New customer:.. Name {first_name} {last_name} Mobile number {mobile_number} email {email} has been created!")
                print('\n')
                print('*' *49)
            create_a_customer()    

#Search for a customer     
        
        elif short_code == '2':
            print("Search for a customer")  
            print("""use this short codes: 
                press 1 - Search by first name.
                press 2 - Search by second name.
                press 3 - Phone number. 
                press 4 - Search by customer id.
                press 5 - Search by email
                """) 

            short_code = input()          

            search_by = input("Search customer:....").upper()
            print('*' *49)
            with open("customer.txt","r") as fp:
                for line in fp:
                    name = line.upper()
                    line_list = name.split( )
                    if line_list[1] == search_by:
                        print()
                        print(line)
                        print('*' *49)

                    elif line_list[2] == search_by:
                        print()
                        print(line)
                        print('*' *49) 

                    elif line_list[3] == search_by: 
                        print()
                        print(line)
                        print('*' *49)

                    # elif line_list[4] == search_by: 
                    #     print()
                    #     print(line)
                    #     print('*' *49)    

                    elif line_list[0] == search_by + ".":
                        print()
                        print(line) 
                        print('*' *49)                       

       
# Update customer details                         
        elif short_code == '3':

            import os               
            def update_line():
                customer_to_update = input("Search customer id to update: ")
                print('*' *49)          
                
                
                with open("customer.txt", "r") as fp:
                    with open ('temp.txt', 'w') as temp:
                        for line in fp:
                            line_list = line.split( )                        
                                                    
                            
                            if line_list[0] == customer_to_update +".":
                                print()
                                print(line)
                                print('*' *49)

                                fn = input('Enter firstname:....')
                                print()
                                ln = input('Enter last_name:...') 
                                print()
                                mn = input('Enter mobile_number:....')
                                print()
                                e = input('Enter email:....')
                                print()   

                                line=line.replace(line_list[1],fn)
                                line=line.replace(line_list[2],ln)
                                line=line.replace(line_list[3],mn)
                                line=line.replace(line_list[4],e)

                                # line = line.replace(line_list, (customer_to_update + ' ' + fn[1] +' ' + ln + ' ' + mn))
                                print('*' *49)
                                print('The entry', line, 'has been updated')
                                print('*' *49)
                            temp.write(line)
                import os              

                os.replace('temp.txt', 'customer.txt')
            update_line()   

        
#Delete a customer 
        elif short_code == '4':
            def deleting_line():
                customer_to_delete = input("Search customer id to delete:... ")
                print()
                print(f'Customer {customer_to_delete} has been deleted')
                print('*'*49)
                print('These are the remaining customers')
                print()                
                with open("customer.txt", "r") as fp:
                    with open ('temp.txt', 'w') as temp:

                        for line in fp:
                            line_list = line.split( )
                            # print(line_list[3])
                            if line_list[0] != customer_to_delete+".":
                                print(line)
                                temp.write(line)
                import os              

                os.replace('temp.txt', 'customer.txt')
                print('*' *49)
            deleting_line()

#to list everythin in the file
        elif short_code == '5':
            with open("customer.txt", "r") as f:
                print('These are the customers available:')
                print()
                print (f.read()) 
                print('*' *49)     


        elif short_code == '6':
            from pos import main_menu        
            main_menu()

           


if __name__ == "__main__":

    customer_menu()        