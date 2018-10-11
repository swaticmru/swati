# Python code to illustrate Sending mail from  
# importing smtp library
import smtplib 
  
# creating smtp session
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
#  providing the Authentication 
s.login("maniswati1999@gmail.com", "#iostream.h") 
  
# message to be sent 
message = "Hey there! this email is sent using smtp."
  
# sending the mail 
s.sendmail("maniswati1999@gmail.com", "tinaalex07@gmail.com", message) 
  
# terminating the session 
s.quit() 
