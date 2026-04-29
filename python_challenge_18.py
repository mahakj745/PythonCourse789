#VALIDATE THE QUALITY AND CORRECTNESS OF EMAIL VALUES

# email = "baraa@gmail.com"   
# #cleaning the string
# email = email.strip()
# if email == "":
#     print ("Email cannot be empty.")
# elif not "." in email and "@" in email:
#     print("Email must contain . and @")
# elif email.count('@') != 1:
#     print ("Email must contain exactly one @")
# elif not email.endswith(('.org','.com','.net')):
#     print ("Email must ends with .com, .org or .net")
# elif not len(email)<= 254:
#     print("email must no longer than 254 characters")
# elif not (email[0].isalnum() and email[-1].isalnum()):
#     print ("Email must start and end with a letter or digit")
# else:
#     print("Email is valid")    


#validate the quality and correctness of passwords
email = input ("Write your email: ")
password = input ("Write your password: ")

e = False

if password == "":
    e = True
    print ("Password cannot be empty")
if not len(password) >= 8:
    e = True
    print ("password must be atleast 8 characters")
if not password.upper():
    e = True
    print ("must include atlease one uppercase")
if not password.lower():
    e = True
    print ("must include atleast one lowercase")
if password == email:
    e = True
    print ("must not be same as email")
if " " in password:
    e = True
    print ("must not contain any spaces")
if not (password[0].isalnum and password[-1].isalnum):
    e = True
    print("must start and end with a letter or digit")

if e == False:
    print("password is valid")