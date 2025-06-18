import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("🔐 Password Generator")
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
