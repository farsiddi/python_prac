alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift_num = int(input("Type the shift number:\n"))


def caesar(text, shift, cipher_direction):
    changed = ""
    if cipher_direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        changed += alphabet[new_position]
    print(f"Your Cipher text is {changed}")


caesar(message,shift_num,direction)