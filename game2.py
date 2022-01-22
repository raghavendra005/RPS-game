# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------

questions = {
 "What year was the Indian constituion adopted?: ": "B",
 "When was the first congress session held?: ": "D",
 "What is ISRO's commercial wing called? : ": "A",
 "Which the highest motorable road in India: ": "B"
}

options =  [["A. 1948", "B. 1949", "C. 1950", "D. 1947"],
          ["A. 1985", "B. 1891", "C. 2000", "D. 1885"],
          ["A. NSIL", "B. SSC", "C. JPIG", "D. SSTC"],
          ["A. Jelep la","B. Umling la pass", "C. Nathu la", "D. Rohtang"]]


new_game()

while play_again():
    new_game()

print("Game over!")

