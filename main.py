import json
import re
import random
import string

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Password strength checker function (optional)
def is_strong_password(password):
    # Implement password strength check logic here
    # For example, you can check for minimum length, presence of uppercase, lowercase, digits, and special characters
    # Return True if the password is strong, False otherwise
    return (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in string.punctuation for char in password)
    )

# Password generator function (optional)
def generate_password(length):
   # Implement password generation logic here
    # You can use random.choice() to select characters from a pool of characters
    # Make sure to include a mix of uppercase, lowercase, digits, and special characters
    # Return the generated password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Initialize empty lists to store encrypted passwords, websites, and usernames
encrypted_passwords = []
websites = []
usernames = []

# Function to add a new password 
def add_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    try_generate_password = input("Do you want to generate a random strong password? (yes/no): ").lower()
    
    if try_generate_password == "yes":
        password_length = int(input("Enter the desired password length: "))
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
    
    else:
        while True:
            password = input("Enter the password: ")
            if is_strong_password(password):
                break
            else:
                print("Weak password. Please make it stronger.")
   

    # Encrypt the password before storing
    encrypted_password = caesar_encrypt(password, shift=3)
    
    # Add the data to the lists
    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted_password)
    print("Password added successfully!")

# Function to retrieve a password 
def get_password():
    website = input("Enter the website: ")

    if website in websites:
        index = websites.index(website)
        username = usernames[index]
        encrypted_password = encrypted_passwords[index]
        decrypted_password = caesar_decrypt(encrypted_password, shift=3)
        print(f"Username: {username}\nPassword: {decrypted_password}")
    else:
        print("Website not found in the password vault.")
 
# Function to save passwords to a JSON file 
def save_passwords():
    data = {
        "websites": websites,
        "usernames": usernames,
        "encrypted_passwords": encrypted_passwords
    }

    with open("vault.txt", "w") as file:
        json.dump(data, file)
    print("Passwords saved successfully!")

# Function to load passwords from a JSON file 
def load_passwords():
    try:
        with open("vault.txt", "r") as file:
            data = json.load(file)
            websites.extend(data["websites"])
            usernames.extend(data["usernames"])
            encrypted_passwords.extend(data["encrypted_passwords"])
            print("Passwords loaded successfully!")
    except FileNotFoundError:
        print("File not found. No passwords loaded.")
    except json.JSONDecodeError:
        print("Error decoding JSON. No passwords loaded.")

  # Main method
def main():
# implement user interface 

  while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Save Passwords")
    print("4. Load Passwords")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        save_passwords()
    elif choice == "4":
        load_passwords()
        print("Passwords loaded successfully!")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
