import os

def extract_files(dir):
    return [el for el in dir_content if os.path.isfile(el)]

def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        file_name, extension = file.split(".")
        if file_name not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report

dir_content = os.listdir()

files = extract_files(dir_content)
report = get_report_for_files_extensions(files)

result_string = ""

for extension, file_names in sorted(report.items(), key=lambda x: x[0]):
    result_string += f".{extension}\n"
    result_string += f"- - - {''.join(file_names)}.{extension}\n"

with open("C:\\Users\\User\\Desktop\\result.txt", "w") as file:
    file.write(result_string)
