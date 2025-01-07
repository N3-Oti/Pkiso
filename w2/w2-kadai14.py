import random
fruits_basket = ["apple","mango","strawberry","grape","peach","banana","pineapple","watermelon","orange","blueberry"]
soudemonai_fruits = fruits_basket[:]
favorite_fruits = []

for i in range(3):
    bannum = random.randrange(len(soudemonai_fruits))
    favorite_fruits.insert(0,soudemonai_fruits[bannum]) 
    del soudemonai_fruits[bannum]

print(f"好きなフルーツは{favorite_fruits}です。")

while len(fruits_basket) > 5:
    bannum = random.randrange(len(fruits_basket)) 
    del fruits_basket[bannum]
print(f"バスケットの中身は{fruits_basket}です。")
found_favorite = False

if fruits_basket[0] in favorite_fruits:
    print(f"あなたは本当に{fruits_basket[0]}が好きなのですね！")
    found_favorite = True
if fruits_basket[1] in favorite_fruits:
    print(f"あなたは本当に{fruits_basket[1]}が好きなのですね！")
    found_favorite = True
if fruits_basket[2] in favorite_fruits:
    print(f"あなたは本当に{fruits_basket[2]}が好きなのですね！")
    found_favorite = True
if fruits_basket[3] in favorite_fruits:
    print(f"あなたは本当に{fruits_basket[3]}が好きなのですね！")
    found_favorite = True
if fruits_basket[4] in favorite_fruits:
    print(f"あなたは本当に{fruits_basket[4]}が好きなのですね！")
    found_favorite = True
if not found_favorite:
    print("残念でした！好きなフルーツが一つも残っていませんでした🧺")