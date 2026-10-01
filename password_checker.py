# Ask user to enter a password 
password = input("Enter a password :")

# This variable will store the password score 
score = 0
feedback = []

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

# small list for common passwords
common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "monkey", "dragon", "111111", "baseball", "iloveyou"]

if password.lower() in common_passwords:
    score = 0
    feedback.append("Password is very common, try something else.")

if score <= 2:
    strength = "weak"
elif score <= 4:
    strength = "medium"
elif score == 5:
    strength = "strong"
else:
    strength = "very strong"

print("\nPassword strength:", strength)
print("Score:", score, "/ 6")

if feedback:
    print("\nRecommendations:")
    for item in feedback:
        print("-", item)