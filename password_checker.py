# Ask user to enter a password 
password = input("Enter a password :")

# This variable will store the password score 
score = 0
feedback = []

# small list for common passwords
common_passwords = [
    "password", "123456", "123456789", "12345678", "12345",
    "111111", "1234567", "sunshine", "qwerty", "iloveyou",
    "princess", "admin", "welcome", "666666", "abc123",
    "password1", "123123", "000000", "monkey", "charlie"
]


if password.lower() in common_passwords:
    score = 0
    feedback.append("Password is in the top 20 common passwords, try something else.")


#Check lenghth of the password
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1
    feedback.append("Use at least 12 characters.")
else:
    feedback.append("Password is too short.")


# Check uppercase  
if any(char.isupper() for char in password):
    score += 1
else:
    feedback.append("Use at least one uppercase letter.")

# Check  lowrcase
if any(char.islower() for char in password):
    score += 1
else:
    feedback.append("Use at least one lowercase letter.")

# Check if the password has at least one digit
if any(char.isdigit() for char in password):
    score += 1
else:
    feedback.append("Use at least one digit.")


# Check if the password has at least one special character
# isalnum() means: letter or number
# "not" means we are looking for something that is NOT a letter or number
if any(not char.isalnum() and not char.isspace() for char in password):
    score += 1
else:
    feedback.append("Use at least one special character.")
#check for spaces
if any(char.isspace() for char in password):
    score = 0
    feedback.append("Password should not contain spaces.")




if score <= 2:
    strength = "weak"
elif score <= 4:
    strength = "medium"
elif score == 5:
    strength = "strong"
else:
    strength = "very strong"

print("\nPassword strength:", strength)
#print("Score:", score, "/ 6")

if not feedback:
    print("SUCCESS: Password is strong and meets all requirements!")
else:
    print("REJECTED: Password does not meet security requirements.")
    print("\nRecommendations:")
    for item in feedback:
        print("-", item)