import random
import string

def generate_password(length):
    # Define characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user input for the desired password length
length = int(input("Enter the desired password length: "))

# Generate and print the random password
password = generate_password(length)
print("Generated password:", password)
