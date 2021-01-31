import re

def write_result(result):
    with open("output.txt", "w") as file:
        for res in result:
            file.write(res+"\n")

def get_file_content(path_to_file):
    with open(path_to_file, "r") as file:
        text = "".join(file.readlines())
        return re.findall(r"[A-Za-z']+", text.lower())

path_to_words = "words.txt"
path_to_text = "text.txt"

first_file_words = get_file_content(path_to_words)
second_file_words = get_file_content(path_to_text)

analyse = {}

for word in first_file_words:
    if word in second_file_words:
        analyse[word] = second_file_words.count(word)

result = [f"{el[0]} - {el[1]}"for el in sorted(analyse.items(), key=lambda x: -x[1])]

write_result(result)