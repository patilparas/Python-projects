#ask user for name
name = input("what is your name: ")

#ask user for age
age = input("what is your age: ")

#ask user for city
city = input("what is your city: ")

#ask user what they enjoy
enjoy = input("what you enjoy: ")

#create output text
string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, enjoy)

#print output on screen
print(output)
