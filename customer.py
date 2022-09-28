class Customer:    
    
    def __init__(self, first_name, last_name, mobile_number):

        # self.customer_id = customer_Id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number    

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.mobile_number}\n"      

    # class methods
    # def create_customer(first_name, last_name, mobile_number):
    #     new_customer = Customer(first_name, last_name, mobile_number) 
        # f = open("customer.txt", "a")
        # f.write(new_customer)
        # f.close() 
        
        # text_file = open("customer.txt","a")
        # for element in Customer():
        #     text_file.write(element+"\n")
        #     text_file.close

        
        # return new_customer

    # customer_list = []
    
    # def save_customer(new_customer):              
    #     # Customer.customer_list.append(new_customer)

    #     # f = open("customer.txt", "a")
    #     # f.write(new_customer)
    #     # f.close() 

    #     # a_list = ["abc", "def", "ghi"]

    #     # customer_list = []
    #     text_file = open("customer.txt","a")
    #     for element in customer_list:
    #         # for i in element:
    #         print (element)
    #         text_file.write(element+"\n")
    #     text_file.close  


        # return(Customer.customer_list)






      

 

# def search_name():
#     letter = input("enter letter: ").upper()
#     IniFile = open ("customer.txt","r")
#     for s in IniFile:
#         if s[0] == letter:
                    
#             print(s)

# search_name()


# calling function

# customer_list = []
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

            # create and save the customer
            
                       
            # new_customer = Customer.create_customer(first_name, last_name, mobile_number)
            # saved_customer = Customer.save_customer(new_customer)
            # customer_list.append(new_customer)
           
            # customer_list.append(add_customer)
            
            
            p1 = Customer(first_name, last_name, mobile_number)
            text_file = open("customer.txt","a+")

            print (p1)
            
            
            text_file.write(f"{p1.first_name} {p1.last_name} {p1.mobile_number}\n").txt
            text_file.close  
            
            print('\n')
            print(f"new customer {first_name} {last_name} {mobile_number} has been created")
            print('\n')

            

        elif short_code == '2':
            print("search customer to delete")   

            p1 = Customer(first_name, last_name, mobile_number)               
            search_customer = input()
            if Customer(first_name, mobile_number):
                    search_customer = p1(search_customer)
                    print(f"{search_customer.first_name} {search_customer.last_name}")
                    print('-' * 20)

                    print(f"Mobile number.......{search_customer.mobile_number}")
                    print(f"First name.......{search_customer.first_name}")
            else:
                    print("That customer does not exist")

            # with open("customer.txt", "r") as file_input:
            #     with open("newfile.txt", "w") as output: 
            #         for line in file_input:
            #             if line.strip("\n") != "nickname_to_delete":
            #         output.write(line)           


        else:
            from pos import main_menu
            short_code == '5'
            main_menu()

           


if __name__ == "__main__":

    customer_menu()             



