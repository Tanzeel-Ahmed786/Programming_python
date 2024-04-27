num_lines=0
num_words=0
num_chars=0
f = open("file.txt",mode = "r")
for line in f:
    num_lines += 1
    num_words += len(line.split())
    num_chars += len(line.strip("\n"))

print("Number of lines in file is :",num_lines)
print("Number of words in file is :",num_words)
print("Number of characters in file is :",num_chars)
