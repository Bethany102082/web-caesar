from helpers import alphabet_position, rotate_character
def encrypt(text, key):
    key_position = 0
    new_text = ""
    for letter in text:
        rot = alphabet_position(key[key_position])
        new_rot_char = rotate_character(letter, rot)
        new_text = new_text + new_rot_char
        if letter.isalpha():
            key_position += 1
        if len(key) == key_position:
            key_position = 0
    return new_text






