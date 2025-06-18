class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26  # Keep shift within alphabet range

    def encrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base + self.shift) % 26 + base)
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)

    def decrypt(self, text):
        result = []
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                new_char = chr((ord(char) - base - self.shift) % 26 + base)
                result.append(new_char)
            else:
                result.append(char)
        return ''.join(result)


def main():
    print("=== Caesar Cipher Tool ===")
    while True:
        try:
            shift = int(input("Enter shift key (number): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    cipher = CaesarCipher(shift)

    while True:
        action = input("\nChoose an action - Encrypt (E), Decrypt (D), or Quit (Q): ").strip().lower()
        if action == 'e':
            plain_text = input("Enter text to encrypt: ")
            encrypted = cipher.encrypt(plain_text)
            print("Encrypted Text:", encrypted)
        elif action == 'd':
            encrypted_text = input("Enter text to decrypt: ")
            decrypted = cipher.decrypt(encrypted_text)
            print("Decrypted Text:", decrypted)
        elif action == 'q':
            print("Exiting Caesar Cipher. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
