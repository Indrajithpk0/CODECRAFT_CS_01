"""
Caesar Cipher Encryption and Decryption Program

This program demonstrates how the Caesar Cipher works.
Users must choose a shift value between 0 and 25.
Any invalid input will result in an error message and re-prompt.
"""


def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


def get_valid_shift():
    while True:
        user_input = input("Enter the shift value (0 to 25): ")

        if not user_input.isdigit():
            print("Invalid input. Please enter a number between 0 and 25.")
            continue

        shift = int(user_input)

        if 0 <= shift <= 25:
            return shift
        else:
            print("Invalid shift value. Please choose a value between 0 and 25.")


def main():
    print("Caesar Cipher Encryption and Decryption Program")
    print("------------------------------------------------")
    print("Note: Shift value 0 or 26 results in no encryption\n")

    message = input("Enter the message: ")
    shift = get_valid_shift()

    print("\nSelect the operation")
    print("1. Encrypt the message")
    print("2. Decrypt the message")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        encrypted_text = caesar_cipher(message, shift, "encrypt")
        print("\nEncrypted message:", encrypted_text)

        print("\nTo decrypt this message:")
        print("Use the encrypted text and the same shift value")
        print("Then choose the decrypt option")

    elif choice == "2":
        decrypted_text = caesar_cipher(message, shift, "decrypt")
        print("\nDecrypted message:", decrypted_text)

    else:
        print("\nInvalid choice. Please restart the program.")


if __name__ == "__main__":
    main()
