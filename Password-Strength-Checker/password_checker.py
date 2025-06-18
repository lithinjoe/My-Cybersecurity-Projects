import string
import random

def check_password_strength(password: str) -> int:
    score = 0
    categories = 0

    if any(c.isupper() for c in password):
        score += 1
        categories += 1
    if any(c.islower() for c in password):
        score += 1
        categories += 1
    if any(c.isdigit() for c in password):
        score += 1
        categories += 1
    if any(c in string.punctuation for c in password):
        score += 1
        categories += 1

    if categories < 4:
        return score

    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if length >= 20:
        score += 1

    return score

def suggest_password(base: str) -> str:
    special_chars = string.ascii_letters + string.digits + string.punctuation
    addon = ''.join(random.choices(special_chars, k=6))
    if random.choice([True, False]):
        return addon + base
    else:
        return base + addon

def check_password(password: str) -> None:
    try:
        with open("common.txt", "r") as file:
            common_passwords = set(file.read().splitlines())
    except FileNotFoundError:
        common_passwords = set()

    if password in common_passwords:
        print("\n  Your password is too common. Strength: 0")
        print(" Try something like:", suggest_password(password))
        return

    strength = check_password_strength(password)

    if strength <= 1:
        print("\n Very Weak Password.")
    elif strength == 2:
        print("\n  Weak Password.")
    elif strength == 3:
        print("\n  Average Password.")
    elif strength == 4:
        print("\n Decent Password.")
    else:
        print("\n Strong Password!")

    if strength < 5:
        print(" Suggested Stronger Version:", suggest_password(password))

def main():
    print("==== Password Strength Checker ====\n")
    print("Type 'exit' anytime to quit.\n")

    while True:
        user_input = input("Enter a password to check: ").strip()
        if user_input.lower() == "exit":
            print("Exiting... Goodbye!")
            break
        if user_input == "":
            print("Please enter something.")
            continue
        check_password(user_input)
        print("-" * 40)

if __name__ == "__main__":
    main()
