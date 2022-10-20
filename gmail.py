import datetime
from email.message import EmailMessage
import smtplib, ssl
from struct import pack



# purchase_list
# item 
shop_name = "bright shop"
shop_street = "Tom Mboya Sreet"
cashier_name = "John Doe"
now = datetime.datetime.now()
date_time = now.strftime(("%Y-%m-%d %H:%M:%S"))  
receipt_messaage = "Thank you for shopping with us"                     



def send_receipt(full_name, email, purchase_list):
    EMAIL_ADDRESS = ' '
    EMAIL_PASSWORD = ' '
    email_receipient = " "
    subject = 'The receipt is attached. Thank you for shopping with us!!'
    
    body = '================================<br>'    
    body += f'\t\tReceipt<br>'
    body += f'\t\t{shop_name.title()}<br>'
    body += f'\t\t{shop_street}<br>'                
    body += '==============================<br>'                
    body += f'Customer: {full_name}<br>'
    body += '===============================<br>'               
    body += f'Cashier: {cashier_name}<br>'
    body += f'Date: {date_time}<br>'
    
    body += '************************************<br>'
    body += 'PURCHASE ITEMS<br>'
    body += "product_name | product_quantity | total_price<br>"
    for p in purchase_list:
        print(p)
        body += f"{p['product']} | {p['quantity']} | {p['price']}<br>"
             
        
    body += '*************************************<br>'   
    body += f"Net Total (paid)\t\t\t\t Kes {purchase_list[-1]['to pay']:.2f}<br>"
    
    body += f"{receipt_messaage}<br>"
    body += '==================================' 


    msg = EmailMessage()                
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg['Subject'] = subject
    msg.set_content(body)
    headers = ["From: " + EMAIL_ADDRESS,
    "To: " + email, 
    "Subject: " + subject,
    "Content-Type: text/html"]

    context = ssl.create_default_context()               

    print(f'Sending email to {email}')
    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:   
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)   
        smtp.sendmail(EMAIL_ADDRESS, email, "\r\n".join(headers) + "\r\n\r\n" + body )
        
            #     letter() 
            # print(letter)    