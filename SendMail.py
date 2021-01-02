import smtplib as s
ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()

ob.login("Your Email","Password")

subject="Check Program"
body=" Write Message Here"
message="Subject:{}\n\n{}".format(subject,body)

ob.sendmail("Your Email","Reciever Email",message)
print('Send Successfully')
ob.quit()