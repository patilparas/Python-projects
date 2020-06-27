movies = {
    "Finding Dory" : [3,5],
    "Avatar" : [18, 5],
    "Tarzan" : [15,5],
    "Ace Ventura" : [12,5],
    "Rocky" : [12,5]
    }

while True:
    choice = input("what film would you like to watch? : ").strip().title()

    if choice in movies:
        age = int(input("how old are you? : ").strip())
        
        if age >= movies[choice][0]:
            seats = movies [choice][1]
            
            if seats>0:
                print("Enjoy the movie :)")
                movies[choice][1] = movies[choice][1]-1
            else:
                print("Sorry! No tickets left :(")

        else:
            print("You are too young to watch the movies!!!")
    else:
        print("We dont have that film...")
