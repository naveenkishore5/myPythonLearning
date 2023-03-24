PLACEHOLDER = "[name]"


with open('./Input/Names/invited_names.txt') as f:
    names = f.readlines()
    print(names)

with open('./Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}', mode='w') as completed_letter:
            completed_letter.write(new_letter)
