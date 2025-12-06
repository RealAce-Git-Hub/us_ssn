import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')

character_list = ""

while True:
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        character_list += string.digits
    elif choice == 2:
        character_list += string.ascii_letters
    elif choice == 3:
        character_list += string.punctuation
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please choose again.")

password = []
for i in range(length):
    randomchar = random.choice(character_list)
    password.append(randomchar)

print("The random password is " + "".join(password))