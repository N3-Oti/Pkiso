import random

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
touhyousya = []
yukensya = []
classmate = ["jon","kanae","satosi","hanako","taro","oda"]

for add in favorite_languages.keys():
    touhyousya.append(add) 
    classmate.append(add)
#print(f"{touhyousya}")

while len(yukensya) < 5:
    add = random.choice(classmate)
    if add not in yukensya:
        yukensya.append(add)

print(f"有権者リスト：{yukensya}")

for i in yukensya:
    if i in touhyousya:
        print(f"{i}さん、投票有難うございました。")
    else:
        print(f"{i}さん、ぜひ投票してください！")