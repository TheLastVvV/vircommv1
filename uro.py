def generate_keys(word):
    length = len(word)
    key1 = length * 25
    key2 = 1223 - key1
    return key1, key2

def encrypt(word):
    key1, key2 = generate_keys(word)
    encrypted_word = ""
    
    for char in word.upper():
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            new_index = index + 1
            encrypted_index = (new_index + key2) % 26
            encrypted_char = chr((encrypted_index % 26) + ord('A') - 1)
            encrypted_word += encrypted_char
        else:
            encrypted_word += char  # Non-alphabet characters remain unchanged

    return encrypted_word

def decrypt(word):
    key1, key2 = generate_keys(word)
    decrypted_word = ""
    
    for char in word.upper():
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            new_index = index + 1
            decrypted_index = (new_index - key2) % 26
            decrypted_char = chr((decrypted_index % 26) + ord('A') - 1)
            decrypted_word += decrypted_char
        else:
            decrypted_word += char  # Non-alphabet characters remain unchanged

    return decrypted_word

def main():
    while True:
        print("\nUroboros Lightweight Encryption by Thelastvvv.com")
        print("\nChoose an option:")
        print("1. Encrypt a word")
        print("2. Decrypt a word")
        print("3. Exit")
        
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            word = input("Enter the word to encrypt: ")
            if word.isalpha():
                encrypted_word = encrypt(word)
                print(f"Encrypted word: {encrypted_word}")
            else:
                print("Error: Invalid input. Please enter alphabetic characters only.")
        elif choice == '2':
            word = input("Enter the word to decrypt: ")
            if word.isalpha():
                decrypted_word = decrypt(word)
                print(f"Decrypted word: {decrypted_word}")
            else:
                print("Error: Invalid input. Please enter alphabetic characters only.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
