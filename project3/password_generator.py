import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

characters = (
    string.ascii_letters
    + string.digits
    + "@#$%&!"
)

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a length greater than zero.")

    else:
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)
        print("Password length:", len(password))

except ValueError:
    print("Invalid input. Please enter a whole number.")
