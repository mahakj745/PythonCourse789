
#name = input("Enter your name: ")
#age = int(input("Enter your age: "))

#print(name != "" and age >= 18)


# password = input("Enter your password")
# # print(len(password)>=8 and != " ")

# condition1 = len(password) >= 8
# condition2 = " " not in password

# print(condition1 and condition2)


#name = input("Enter your name: ")
#print("s" in name)

#email = input("Enter your email: ")
#condition_1 = email is not ""
#condition_2 = "@" in email
#condition_3 = email.endswith(".com")

#print (condition_1 and condition_2 and condition_3)

#user_name = input("Enter your name: ")
#condition_1 = is_instance(user_name, str)
#condition_2 = user_name is not "None"
#condition_3 = len(user_name)<=5

#print (condition_1 and condition_2 and condition_3)


user_name = input("Enter your name: ")
is_banned = False
email_verified = True

access = (user_name in ["admin" or "moderator"]) and (not is_banned or email_verified)
print (access)
