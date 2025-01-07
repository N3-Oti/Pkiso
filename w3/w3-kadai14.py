print("全部")
with open("./w3/learning_python.txt", encoding='utf-8') as file_obj:
    txt = file_obj.read()
print(txt)
print()

print("1行づつ")
with open('./w3/learning_python.txt', encoding='utf-8') as file_obj2:
    for line in file_obj2:
        print(line)
print()

print("リスト")
with open('./w3/learning_python.txt', encoding='utf-8') as file_obj3:
    lines = file_obj3.readlines()

for line in lines:
    print(line.rstrip())