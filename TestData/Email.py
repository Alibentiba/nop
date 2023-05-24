import random
import string

def generate_email(length=10):
    # Generate a random string of lowercase letters and digits
    letters_digits = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters_digits) for _ in range(length))
    
    # Generate a random domain from a predefined list
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'example.com']
    domain = random.choice(domains)
    
    # Concatenate the username and domain to form the email address
    email = f"{username}@{domain}"
    
    return email

# Generate and print a random email address






