my_friends = ["Google","Amazon","OpenAI","Microsoft","NTT"]
your_friends = my_friends[:]
my_friends.append("KIC")
your_friends.append("NHK")

for i in range(len(my_friends)):
    print(f"私の友達は：{my_friends[i]}")

for i in range(len(your_friends)):
    print(f"あなたの友達は：{your_friends[i]}")