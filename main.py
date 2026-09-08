import random

while True:
    print("\nNumber Guessing Game")
    print("Difficulty choose karo:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    choice = input("Choice (1/2/3): ")

    if choice == "1":
        max_number = 50
    elif choice == "2":
        max_number = 100
    elif choice == "3":
        max_number = 200
    else:
        print("Invalid choice!")
        continue

    number = random.randint(1, max_number)
    max_attempts = 7

    print("1 se", max_number, "ke beech number guess karo!")
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

    again = input("Dobara khelna hai? (y/n): ")

    if again.lower() != "y":
        print("Game band ho gaya. Thank you!")
        break
