result = [' '.join(list_as_string.split()) for list_as_string in input().split('|')[::-1]]
strip_result = [el for el in result if el != ""]
print(' '.join(strip_result))
