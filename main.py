import random

while True:
    number = random.randint(1, 100)
    max_attempts = 7

    print("Number Guessing Game")
    print("1 se 100 ke beech number guess karo!")
    print("Aapko 7 chances milenge.")

    
        for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input("Apna guess dalo: "))
    except ValueError:
        print("Sirf number dalo!")
        continue

   
        if guess < number:
            print("Thoda bada number try karo!")

        elif guess > number:
                   print("Thoda chhota number try karo!")

        else:
            score = max_attempts - attempt + 1
            print("Sahi jawab!")
            print("Aapne", attempt, "attempts mein jeet gaye!")
            print("Aapka score:", score)
            break

    else:
        print("Game Over!")
        print("Sahi number tha:", number)

   play again = input("Dobara khelna hai? (y/n): ")

    if play again.lower() != "y":
        print("Game band ho gaya. Thank you!")
        break
