import random


print("-------------------------------")
print("     M& M Guessing game ")
print("-------------------------------")

print("Guess the number of M&M and you get lunch on the hous!")
print()

mm_count = random.randint(1, 100)
attempt_limit = 5
attempts = 0
 
while attempts < attempt_limit:
    guess_text = input ("How many M&M arre in the jar?")
    guess = int(guess_text)
    print(guess)
 
    attempts += 1

print("Bye")