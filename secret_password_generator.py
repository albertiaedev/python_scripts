import re
import secrets
import string


def generate_secret(length=20, nums=3, special_chars=2, uppercase=4, lowercase=4):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols


    # Generate password
    while True:
        secret = ''
        
        for _ in range(length):
            secret += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, secret))
            for constraint, pattern in constraints
        ):
            break
    
    return secret


# Run this script as a main program, not an imported module
if __name__ == '__main__':
    new_secret = generate_secret()
    print('New Secret Password:', new_secret)