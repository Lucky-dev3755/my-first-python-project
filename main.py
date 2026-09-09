import random

# Load saved best score
try:
    with open("highscore.txt", "r") as file:
        best_score = int(file.read())
except (FileNotFoundError, PermissionError, ValueError):
    best_score = 0


while True:
    print("\nNumber Guessing Game")
    print("Current Best Score:", best_score)
    print("Difficulty choose karo:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    print("4. Quit Game")

    choice = input("Choice (1/2/3/4): ")

    if choice == "1":
        max_number = 50
    elif choice == "2":
        max_number = 100
    elif choice == "3":
        max_number = 200
    elif choice == "4":
        print("Game band ho gaya. Thank you!")
        break
    else:
        print("Invalid choice!")
        continue

    number = random.randint(1, max_number)
    max_attempts = 7
hint_used = false
    print("1 se", max_number, "ke beech number guess karo!")
    print("Aapko 7 chances milenge.")

    for attempt in range(1, max_attempts + 1):
        try:
            print("Attempts remaining:", max_attempts - attempt + 1)
            if not hint_used:
    print("Hint: H likho aur hint pao, ya number guess karo.")
            guess = input("Apna guess dalo: ")
            guess_input = input("Apna guess dalo: ")

if guess_input.lower() == "h" and not hint_used:
    if number % 2 == 0:
        print("💡 Hint: Number EVEN hai.")
    else:
        print("💡 Hint: Number ODD hai.")
    hint_used = True
    continue


    print("Sirf number ya H dalo!")
    continue
        except ValueError:
            print("Sirf number dalo!")
            continue

        if guess < 1 or guess > max_number:
            print("Please 1 se", max_number, "ke beech number dalo!")
            continue

        if guess < number:
            print("Thoda bada number try karo!")

        elif guess > number:
            print("Thoda chhota number try karo!")

        else:
            score = max_attempts - attempt + 1

            print("Sahi jawab!")
            print("Aapne", attempt, "attempts mein jeet gaye!")
            if attempt == 1:
    print("Amazing! First try mein guess kiya! 🔥")
elif attempt <= 3:
    print("Excellent guessing! 👏")
elif attempt <= 5:
    print("Good guessing! 👍")
else:
    print("Nice! You made it! 💪")
            print("Aapka score:", score)
if score >= 6:
    print("Excellent! 🔥")
elif score >= 4:
    print("Very Good! 👏")

elif score >= 2:
    print("Good Job! 👍")
else:
    print("Keep Practicing! 💪")
            if score > best_score:
                best_score = score

                # Save best score
                try:
                    with open("highscore.txt", "w") as file:
                        file.write(str(best_score))
                except PermissionError:
                    pass

            break

    else:
        print("Game Over!")
        print("Sahi number tha:", number)

    print("Best score:", best_score)

    again = input("Dobara khelna hai? (y/n): ")

    if again.lower() != "y":
        print("Game band ho gaya. Thank you!")
        break
