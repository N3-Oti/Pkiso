import random
raihin = ["Sun","Sumitani","Iwamoto"]
ninzu = len(raihin)
for i in range(ninzu):
    print(f"{raihin[i]}先生、晩餐会を開催致しますので是非参加して下さい。")

kesseki = random.randrange(ninzu)
print(f"出席不可:{raihin[kesseki]}")

raihin[kesseki] = "Miyasaka"
for i in range(ninzu):
    print(f"{raihin[i]}先生、晩餐会を開催致しますので是非参加して下さい。")