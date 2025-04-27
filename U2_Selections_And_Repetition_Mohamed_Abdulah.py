name = input("What is your name? ")
print("Hello", name + "! Let's play a quiz.")

score = 0
max_score = 0

while True:
    print("Pick a category: sports, math, science, history")
    category = input("Category: ").lower()

    print("Pick a difficulty: easy, medium, hard")
    difficulty = input("Difficulty: ").lower()

    question = ""
    options = []
    answer = ""

    if category == "sports":
        if difficulty == "easy":
            question = "How many players on a soccer team?"
            options = ["9", "10", "11", "12"]
            answer = "11"
        elif difficulty == "medium":
            question = "What country won the 2018 World Cup?"
            options = ["Germany", "France", "Brazil", "Spain"]
            answer = "France"
        elif difficulty == "hard":
            question = "What year did the first Olympics happen?"
            options = ["1896", "1900", "1924", "1880"]
            answer = "1896"
        else:
            print("Invalid difficulty. Try again.")
            continue

    elif category == "math":
        if difficulty == "easy":
            question = "What is 4 + 4?"
            options = ["6", "7", "8", "9"]
            answer = "8"
        elif difficulty == "medium":
            question = "What is 12 x 3?"
            options = ["36", "30", "33", "32"]
            answer = "36"
        elif difficulty == "hard":
            question = "What is the square root of 169?"
            options = ["11", "12", "13", "14"]
            answer = "13"
        else:
            print("Invalid difficulty. Try again.")
            continue

    elif category == "science":
        if difficulty == "easy":
            question = "What planet do we live on?"
            options = ["Mars", "Earth", "Venus", "Jupiter"]
            answer = "Earth"
        elif difficulty == "medium":
            question = "What gas do plants breathe in?"
            options = ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"]
            answer = "Carbon Dioxide"
        elif difficulty == "hard":
            question = "What’s the center of an atom called?"
            options = ["Electron", "Proton", "Nucleus", "Neutron"]
            answer = "Nucleus"
        else:
            print("Invalid difficulty. Try again.")
            continue

    elif category == "history":
        if difficulty == "easy":
            question = "Who was the first US president?"
            options = ["Lincoln", "Adams", "Washington", "Obama"]
            answer = "Washington"
        elif difficulty == "medium":
            question = "In what year did World War 2 end?"
            options = ["1942", "1945", "1947", "1950"]
            answer = "1945"
        elif difficulty == "hard":
            question = "Who was the Egyptian queen famous for her beauty?"
            options = ["Nefertiti", "Hatshepsut", "Cleopatra", "Isis"]
            answer = "Cleopatra"
        else:
            print("Invalid difficulty. Try again.")
            continue

    else:
        print("Invalid category. Try again.")
        continue


    print( question)

    for i in range(len(options)):
        print(str(i + 1) + ". " + options[i])

    user_answer = input("Your answer: ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 10
    else:
        print("Wrong! The correct answer was:", answer)

    max_score += 10

    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        break

print("Thanks for playing,", name + "!")
print("Your final score is", score, "out of", max_score)