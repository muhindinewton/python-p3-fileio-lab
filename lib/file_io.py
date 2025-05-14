# lib/file_io.py

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file:
        file.write(file_content)


def append_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as file:
        file.write(file_content)


def read_file(file_name):
    with open(f"{file_name}.txt", mode='r', encoding='utf-8') as file:
        return file.read()
