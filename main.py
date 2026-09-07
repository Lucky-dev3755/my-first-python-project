import random

number = random.randint(1, 100)
attempts = 4

print("Number Guessing Game")
print("1 se 100 ke beech number guess karo!")

while True:
    guess = int(input("Apna guess dalo: "))
    attempts += 1

    if guess < number:
        print("Thoda bada number try karo!")
    elif guess > number:
        print("Thoda chhota number try karo!")
    else:
        print("Sahi jawab!")
        print("Aapne", attempts, "attempts mein guess kiya.")
        break
