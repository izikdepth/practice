import random
import string

def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

def main():
    length = int(input("Enter password length: "))
    allow_repeats = input("Allow repeated characters? (y/n) ").lower() == 'y'
    use_letters = input("Use letters? (y/n) ").lower() == 'y'
    use_numbers = input("Use numbers? (y/n) ").lower() == 'y'
    use_symbols = input("Use symbols? (y/n) ").lower() == 'y'

    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if not allow_repeats:
        chars = ''.join(set(chars))

    password = generate_password(length, chars)
    print("Generated password:", password)

    save_to_file = input("Save password to file? (y/n) ").lower() == 'y'
    if save_to_file:
        with open('passwords.txt', 'a') as file:
            file.write(password + '\n')

if __name__ == '__main__':
    main()
