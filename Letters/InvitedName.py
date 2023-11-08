PLACE_HOLDER = "[name]"

with open("InvitedNames.txt") as inv:
    names = inv.readlines()
    # print(names)

with open("Msg.txt") as letter_files:
    content = letter_files.read()
    # print(content)
    for name in names:
        stripped_name = name.strip()
        new_letter = content.replace(PLACE_HOLDER, stripped_name)
        print(new_letter)
        with open(f"./ReadyToSend/LetterTo{stripped_name}.text",mode="w") as complete_letter:
            complete_letter.write(new_letter)
    # print(letter_files.read())
