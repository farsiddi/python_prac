alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
message = input("Type your message:\n").lower()
shift_num = int(input("Type the shift number:\n"))


def my_decrypt(text, shift):
    changed = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        changed += alphabet[new_position]
    print(f"Cipher text is\n{changed}")


my_decrypt(message, shift_num)
