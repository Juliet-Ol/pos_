

class customer:

    customer_list = []

    def __init__(self, first_name, last_name, mobile_number):

        # self.customer_id = customer_Id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number

    customer_list = []

    def save_customer(self):

        customer.customer_list.append(self)  

def create_customer(first_name, last_name, mobile_number):
    # customer = create_customer
    new_customer = customer(first_name, last_name, mobile_number)    
    customer.save_customer
    return new_customer

 

# def search_name():
#     letter = input("enter letter: ").upper()
#     IniFile = open ("customer.txt","r")
#     for s in IniFile:
#         if s[0] == letter:
                    
#             print(s)

# search_name()


# calling function

def main():
    print("Thank you for doing business with us.")
    customer_name =input()

    print(f"Hello{customer_name}")
    print('\n')

    while True:
        print("use this short codes: press 1 - to create a new customer, press 2 - search a customer, press 3 -display customer") 

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
            customer.save_customer(create_customer(first_name, last_name, mobile_number))
            print('\n')
            print(f"new customer {first_name} {last_name} {mobile_number} has been created")
            print('\n')

           


if __name__ == "__main__":

    main()             



