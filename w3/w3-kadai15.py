with open('./w3/learning_python.txt', encoding='utf-8') as file_obj:
    for line in file_obj:
        line = line.replace("python","バイトの人")
        print(line)
print()