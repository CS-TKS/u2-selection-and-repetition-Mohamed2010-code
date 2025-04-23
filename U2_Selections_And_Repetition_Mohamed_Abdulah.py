name = input("What is your name? ")
print("Hello", name + "! Let's play a quiz.")

score = 0
max_score = 0

question = ""
options = []
answer = ""

print("Pick a category: sports, math, science, history")
category = input("Category: ")

print("Pick a difficulty: easy, medium, hard")
difficulty = input("Difficulty: ")

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
    print("Invalid category or difficulty. Try again.")


    print("" + question)





