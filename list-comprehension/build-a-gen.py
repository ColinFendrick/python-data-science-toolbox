lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']


def get_lengths(input_list):
    for person in input_list:
        yield len(person)

for value in get_lengths(lannister):
    print(value)
