while 1:
    kazu = input("整数を入力してください:")
    try:
        kazu = int(kazu)
        break
    except ValueError:
        print("無効な入力です。整数を入力してください。")

if kazu == 0:
    print(f"{kazu}は0なので、10の倍数ではありません。")
elif kazu%10 == 0:
    print(f"{kazu}は10の倍数です。")
else:
    print(f"{kazu}は10の倍数ではありません。")