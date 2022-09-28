


first_name= input("enter name: ")
second_name= input("enter name: ")
name = f"my name is {first_name} {second_name} \n"
myfile= open("customer.txt", "a") 

# print(name)
# myfile.write(name)
# myfile.close()

#   p1 = Customer(first_name, last_name, mobile_number)
#         text_file = open("customer.txt","a+")
#         # add_customer = f"{Customer.first_name} {Customer.last_name} {Customer.mobile_number}\n"

#         print (p1)
#         text_file.write(f"{p1.first_name} {p1.last_name} {p1.mobile_number}\n")
#         text_file.close 






# assign list
l = ['Geeks','for','Geeks!']
 
# open file
with open('gfg.txt', 'w+') as f:
     
    # write elements of list
    for items in l:
        f.write('%s\n' %items)
     
    print("File written successfully")
 
 
# close the file
f.close()



# your_list = [1,2,3,'test']

# with open('your_text_file.txt', 'w') as f:
#     for item in your_list:
#         f.write(f"{line}\n")