known_users = ["alice", "bob", "claire", "dan", "emma", "fred", "georgie", "harry"]

while True:
    print("Hi!!My name is Travis")
    name = input("what is your name: ").strip().lower()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("would you like to be removed from the system(y/n)?: ").lower()

        if remove == "y":
            known_users.remove(name)
            print("Sorry to see you go from the system {}".format(name))
        elif remove == "n":
            print("Great, I didn't want you to leave {}".format(name))
            
            
    else:
        print("sorry but you are not valid user {}".format(name))
        add = input("would you like to join the system(y/n):").strip().lower()

        if add == "y":
            known_users.append(name)
            print("Happy to see you join the system {}".format(name))
        elif add == "n":
            print("Okay, no worries see you in future {}".format(name))
