PLACEHOLDER = "[name]"

names = []
with open("./Input/Names/invited_names.txt", mode="r") as file:
    for line in file:
        names.append(line.strip())

with open("./Input/Letters/starting_letter.txt", mode="r") as file2:
    text = file2.read()
    for name in names:
        new_text = text.replace(PLACEHOLDER, name)
        print(new_text)
        print("_________________")

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
            new_file.write(new_text)

