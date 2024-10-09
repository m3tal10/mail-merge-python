with open('./Input/Letters/starting_letter.txt') as template_file:
    template = template_file.read()
with open('./Input/Names/invited_names.txt') as name_file:
    names_string = name_file.read()

names = names_string.split('\n')

for name in names:
    new_file = template.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt',
              mode='w') as write_file:

        write_file.write(new_file)
