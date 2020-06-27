#get user mail id
email = input("What is your mail id: ").strip()

#slice out username
username = email[:email.index("@")]

#slice domain name
domain = email[email.index("@")+1 :]

#format message
output = "your username is {} and ur domain name is {}".format(username,domain)

#display output message
print(output)
