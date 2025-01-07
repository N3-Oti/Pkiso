print("inu")
try:
    with open("./w4/dogs.txt", encoding='utf-8') as file_obj:
        txt = file_obj.read()
    print(txt)
    print()
except FileNotFoundError:
    pass

print("neko")
try:
    with open("./w4/cats.txt", encoding='utf-8') as file_obj:
        txt = file_obj.read()
    print(txt)
    print()
except FileNotFoundError:
    pass
