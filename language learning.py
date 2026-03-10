words = {
    "hello": "vanakkam",
    "thank you": "nandri",
    "water": "thanni",
    "food": "saapadu",
    "friend": "nanban"
}

def learn_words():
    print("\nLearn Words\n")
    for eng, tam in words.items():
        print(f"{eng} = {tam}")

def quiz():
    score = 0
    print("\nQuiz Time\n")

    for eng, tam in words.items():
        ans = input(f"What is the meaning of '{eng}' in Tamil? ")

        if ans.lower() == tam.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer: {tam}\n")

    print("Your Score:", score, "/", len(words))

def add_word():
    eng = input("Enter English word: ")
    tam = input("Enter Tamil meaning: ")
    words[eng] = tam
    print("Word added successfully!")

while True:
    print("\n===== Language Learning App =====")
    print("1. Learn Words")
    print("2. Quiz")
    print("3. Add New Word")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        learn_words()
    elif choice == "2":
        quiz()
    elif choice == "3":
        add_word()
    elif choice == "4":
        print("Thank you for learning!")
        break
    else:
        print("Invalid choice")
