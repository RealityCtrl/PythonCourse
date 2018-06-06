words = "good code architecture helps legibility"

file_name = "my_text.txt"
with open(file_name, "wt") as fileObj:
    fileObj.write(words)