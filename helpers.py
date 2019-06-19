def alphabet_position(letter):
 
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if letter in lower:
        return lower.index(letter)
    else:
        return upper.index(letter)
            
def rotate_character(char, rot):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char.isalpha() == False:
        return char

    position = alphabet_position(char)
    position += rot
    post_rot = position % 26

    if char in lower:
        new_character = lower[post_rot]
    else:
        new_character = upper[post_rot]
    return new_character
