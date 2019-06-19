from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_text = ""
    for letter in text:
        new_letter = rotate_character(letter, rot)
        new_text += new_letter
    return new_text   

def main():
    secret_message = input("What's your secret message?")
    rotation_request = int(input("How many spaces would you like to rotate?"))
    new_encrypted_message = encrypt(secret_message, rotation_request)
    print(new_encrypted_message)

if __name__ == "__main__":
    main()


