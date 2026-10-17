
# Project 4: General Knowledge Quiz

print("================================")
print("     GENERAL KNOWLEDGE QUIZ")
print("================================")

# Initialize the score
score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.")

# Question 3
answer = input("3. How many days are there in a week? ").strip().lower()

if answer == "7" or answer == "seven":
    print("Correct answer!")
    score += 1
else:
    print("Incorrect! The correct answer is Seven.")

# Display the final score
print("\n================================")
print(f"Your final score is: {score}/3")
print("Thank you for playing!")
print("================================")
