import random
alien_color_list = ["green","yellow","red"]
colornum = random.randrange(len(alien_color_list))
alien_color = alien_color_list[colornum]
print(f"エイリアンの色は{alien_color}です。")
if alien_color == "green" :
    print("あなたは5点獲得しました！")