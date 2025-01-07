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