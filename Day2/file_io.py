words = "good code architecture helps legibility"

file_name = "my_text.txt"
with open(file_name, "wt") as fileObj:
    fileObj.write(words)

with open(file_name, "r") as fileObj:
    words_read = fileObj.readline()
    print(words_read)
    words_list = words_read.split()
    print(words_list)