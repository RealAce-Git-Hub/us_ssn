#encoder : Encrypts data. Converts data into a secure format.
#decoder : Deecrypts data. Converts secure format back to original data.


def encrypt(password, n):
    new_pass = ""
    for i in password:
        new_pass = new_pass + chr((ord(i)+n)%26)
    return new_pass

def decrypt(password, n):
    original_pass = ""
    for i in password:
        original_pass = original_pass + chr((ord(i)-n)%26)
    return original_pass

if __name__  == "__main__":
    password = input("Enter your password: ")
    n = int(input("Enter shift value (number): "))
    encrypted_password = encrypt(password, n)
    decrypted_password = decrypt(encrypted_password, n)
    print("Original Password: ", password)
    print("Encrypted Password: ", encrypted_password)
    print("Decrypted Password: ", encrypted_password)