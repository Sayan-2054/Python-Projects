import random
import string

def generate_password(
    length=12, 
    uppercase_count=2, 
    lowercase_count=2, 
    digit_count=2, 
    special_count=2, 
    avoid_ambiguous=True
):
    """
    Generates a secure password with customizable parameters.

    Parameters:
    - length: Total length of the password.
    - uppercase_count: Number of uppercase letters.
    - lowercase_count: Number of lowercase letters.
    - digit_count: Number of digits.
    - special_count: Number of special characters.
    - avoid_ambiguous: If True, avoids ambiguous characters for better readability.

    Returns:
    A randomly generated password.
    """
    if length < 8 or (length < uppercase_count + lowercase_count + digit_count + special_count):
        raise ValueError("Invalid password configuration")

    characters = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'special': string.punctuation
    }

    if avoid_ambiguous:
        ambiguous_chars = 'lI10O'
        for category, chars in characters.items():
            characters[category] = ''.join(c for c in chars if c not in ambiguous_chars)

    password = [random.choice(characters[category]) for category in characters]

    remaining_length = length - len(password)

    for _ in range(remaining_length):
        category = random.choice(list(characters.values()))
        password.append(random.choice(category))

    random.shuffle(password)

    return ''.join(password)

try:
    password = generate_password(length=16, uppercase_count=3, lowercase_count=3, digit_count=3, special_count=3, avoid_ambiguous=True)
    print("Generated Password:", password)
except ValueError as e:
    print("Error:", e)
