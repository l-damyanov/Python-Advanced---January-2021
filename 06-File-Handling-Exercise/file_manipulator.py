import os

def create_file(file_path):
    with open(file_path, "w") as file:
        file.write("")

def add(file_path, content):
    with open(file_path, "a") as file:
        file.write(content+"\n")

def replace_content(file_path, content, replace_with):
    try:
        with open(file_path, "r+") as file:
            text = ''.join(file.readlines())
            replaced_content = text.replace(content, replace_with)
            file.seek(0)
            file.write(replaced_content)
    except FileNotFoundError:
        print("An error occurred")

def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")

mapper = {"Create": create_file, "Add": add, "Replace": replace_content, "Delete": delete_file}

def start_engine():
    command_data = input().split("-")
    while not command_data[0] == "End":
        command, command_args = command_data[0], command_data[1:]
        mapper[command](*command_args)
        command_data = input().split("-")

start_engine()
