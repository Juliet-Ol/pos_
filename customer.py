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
        press 3 - Update customer details.
        press 4 - Delete a customer.
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
                press 5 - Print all items in the file""") 

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

                       

            #to bring everything in the database
            with open("customer.txt", "r") as f:
                print (f.read())  


# Update customer details             
        elif short_code == '3':

            import os

            original_file = "newfile.txt"
            temp_file = "temp.txt"

            string_to_update = [input("Enter what you want to update: ")]
            word_to_update = string_to_update[0]

            with open("newfile.txt", "r") as fp:
                for line in fp:
                    if line != None and word_to_update in line:
                        print(line)

            string_to_replace_with = input("Enter name you want to replace with: ")
            with open(original_file, "r") as my_input:
                with open(temp_file, "w") as output:
                    for line in my_input:
                        for word in string_to_update:
                            # line_list = line.split( )
                            # string_to_replace_with = input("Enter name you want to replace with: ")
                            # print(line_list[3])
                            if line != None and word in line:
                                print(line)
                 
                            line = line.replace(word, string_to_replace_with)
                        output.write(line)

            # replace file with original name
            os.replace('temp.txt', 'newfile.txt')            


#Delete a customer 
        elif short_code == '4':
            print("search for a customer")  
            print("""use this short codes: 
                press 1 - Search by first name.
                press 2 - Search by second name.
                press 3 - Phone number. 
                press 4 - Search by customer id.
                press 5 - Print all items in the file""") 

            short_code = input()

            search_by = input("Search:....").upper()
            with open("newfile.txt","r") as fp:
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

                    else:
                        with open("newfile.txt", "r") as file_input:
                            with open("tempfile.txt", "w") as output: 
                                for line in file_input:
                                    if line.strip("\n") != "nickname_to_delete":
                                        output.write(line) 
                                        print(line)  

                                        line = line.replace(search_by, "")
                                    output.write(line)  
   
            # replace file with original name
            os.replace('temp.txt', 'newfile.txt') 

        #Delete searched entry
        # elif short_code == '3':

        #     import os

        #     original_file = "newfile.txt"
        #     temp_file = "temp.txt"

        #     string_to_delete = [input("Enter name you want to delete: ")]
        #     word_to_delete =string_to_delete[0]

        #     with open("newfile.txt", "r") as fp:
        #         for line in fp:
        #             if line != None and word_to_delete in line:
        #                 print(line)

        #     string_to_replace_with = input("Enter name you want to replace with: ")
        #     with open(original_file, "r") as my_input:
        #         with open(temp_file, "w") as output:
        #             for line in my_input:
        #                 for word in string_to_delete:
        #                     # line_list = line.split( )
        #                     # string_to_replace_with = input("Enter name you want to replace with: ")
        #                     # print(line_list[3])
        #                     if line != None and word in line:
        #                         print(line)
                 
        #                     line = line.replace(word," ")
        #                 output.write(line)

        #     # replace file with original name
            # os.replace('temp.txt', 'newfile.txt')    


        elif short_code == '5':
            from pos import main_menu
        
            main_menu()

           


if __name__ == "__main__":

    customer_menu()        