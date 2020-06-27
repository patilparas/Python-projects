<<<<<<< HEAD
from random import choice

questions = ["Why is the sky blue? : ",
             "Where are the dinosaurs? : ",
             "What are you doing? : "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why? : ").strip().lower()
 
print("Ohh... Ok")
=======
from random import choice

questions = ["Why is the sky blue? : ",
             "Where are the dinosaurs? : ",
             "What are you doing? : "]

question = choice(questions)
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why? : ").strip().lower()
 
print("Ohh... Ok")
>>>>>>> 24f9b43... second commit
