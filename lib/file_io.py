def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as write_file:
        write_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as append_file:
        append_file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as read_file:
        return read_file.read()
