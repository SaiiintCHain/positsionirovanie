def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings, start=1):
        byte_start_position = f.tell()
        f.write(string + '\n')
        strings_positions[(index, byte_start_position)] = string
    f.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)