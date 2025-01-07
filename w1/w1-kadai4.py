import random
raihin = ["Sun","Sumitani","Iwamoto"]
def send(raihin):
    ninzu = len(raihin)
    for i in range(ninzu):
        print(f"{raihin[i]}先生、晩餐会を開催致しますので是非参加して下さい。")
send(raihin)

ninzu = len(raihin)
kesseki = random.randrange(ninzu)
print(f"出席不可:{raihin[kesseki]}")

raihin[kesseki] = "Miyasaka"
send(raihin)

print("大テーブルの予約が出来ました！")
raihin.insert(0,"Sento")
ninzu = len(raihin)
raihin.insert(ninzu//2,"Manaka")
raihin.append("saigou")
send(raihin)

gentei = 2
print(f"食材が足りない為、招待客が{gentei}人になります。")
ninzu = len(raihin)
for i in range(ninzu - gentei):
    sakujyo = raihin.pop()
    print(f"申し訳ありません、{sakujyo}先生、食材不足により招待を取りやめさせていただきます。誠に申し訳ございません。")
    ninzu -= 1
send(raihin)

for i in range(ninzu):
    del raihin[0]
print(raihin)