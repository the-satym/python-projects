#date: 15 jan 2025

from cryptography.fernet import Fernet

# Step 1: Generate a secret key (this should ideally be stored securely if reused)
key = Fernet.generate_key()
cipher = Fernet(key)


# Step 2: Function to encrypt a message
def encrypt_message(message):
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message


# Step 3: Function to decrypt a message
def decrypt_message(encrypted_message):
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message


# Example usage
perform=bool(input("enter 1: for encryption and enter 0 for decryption:-   "))
if perform==1:
    if __name__ == "__main__":
        user_message = input("Enter the message to encrypt: ")
        encrypted = encrypt_message(user_message)
        print("Encrypted message:", encrypted)

    # Decrypting for demonstration
    #decrypted = decrypt_message(encrypted)
    #print("Decrypted message:", decrypted)
elif perform==0:
    encrypt_message=input("enter the code you want to decrypt:-   ")
    decrypted=decrypt_message(encrypted_message)
    print("decrypted message: ", decrypted)