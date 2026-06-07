# Python Quiz Game

questions = ("How many legs do spiders have?: ",
             "Which animal lays the largest egg?: ",
             "What is the hardest natural material on earth?: ",
             "What planet is furthest from the sun?: ",
             "Which team has the most NFL superbowl wins?:",
             "How many bones are in the human body?: ",
             "What is the most bought car make in the U.S.?: ",
             "How many elements are on the periodic table?: ",
             "Who palyer has the most total rebounds in NBA history?: ",
             "What is the strongest animal relative to its size?: ")

options = (("A. 6", "B. 10", "C. 12", "D. 8"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Obsidian", "B. Gold", "C. Diamond", "D. Corundum"),
           ("A. Earth", "B. Neptune", "C. Jupiter", "D. Venus"),
           ("A. Steelers", "B. 49ers", "C. Chiefs", "D. Patriots"),
           ("A. 206", "B. 205", "C. 207", "D. 210"),
           ("A. Toyota", "B. Honda", "C. Ford", "D. Tesla"),
           ("A. 97", "B. 118", "C. 14", "D. 117"),
           ("A. Kareem Abdul-Jabbar", "B. Shaquille O'Neal", "C. Moses Malone", "D. Wilt Chamberlain"),
           ("A. Leafcutter Ant", "B. Dung Beetle", "C. Gorilla", "D. Praying Mantis"),)

answers = ("D", "D", "C", "B", "D", "A", "A", "B", "D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("--------------------------")
print("         RESULTS          ")
print("--------------------------")

print ("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print ("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")