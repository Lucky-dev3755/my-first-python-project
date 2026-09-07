import random

number = random.randint(1, 100)

print("Number Guessing Game")
print("1 se 100 ke beech number guess karo!")
print("Aapko 7 chances milenge.")

for attempt in range(1, 8):
    guess = int(input("Apna guess dalo: "))

    if guess < number:
        print("Thoda bada number try karo!")
    elif guess > number:
        print("Thoda chhota number try karo!")
    else:
        print("Sahi jawab!")
        print("Aap", attempt, "attempts mein jeet gaye!")
        break
else:
    print("Game Over!")
    print("Sahi number tha:", number)
