class Customer:    
    
    def __init__(self, first_name, last_name, mobile_number):

        # self.customer_id = customer_Id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number    

    
    def create_customer(first_name, last_name, mobile_number):
        new_customer = Customer(first_name, last_name, mobile_number)    
        return new_customer

    customer_list = []
    
    def save_customer(new_customer):        
        Customer.customer_list.append(new_customer)
        return(Customer.customer_list)    

        

 

# def search_name():
#     letter = input("enter letter: ").upper()
#     IniFile = open ("customer.txt","r")
#     for s in IniFile:
#         if s[0] == letter:
                    
#             print(s)

# search_name()


# calling function

def customer_menu():
    print("Thank you for doing business with us.")
    customer_name =input()

    print(f"Hello{customer_name}")
    print('\n')

    while True:
        print("""use this short codes: press 1 - to create a new customer, 
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
            
            new_customer = Customer.create_customer(first_name, last_name, mobile_number)
            saved_customer = Customer.save_customer(new_customer)
            print(saved_customer)
            print('\n')
            print(f"new customer {first_name} {last_name} {mobile_number} has been created")
            print('\n')

        # elif short_code == '2':


        else:
            from pos import main_menu
            short_code == '5'
            main_menu()

           


if __name__ == "__main__":

    customer_menu()             



