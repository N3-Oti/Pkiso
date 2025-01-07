seito = {"ハリーポッター":"グリフィンドール寮、11歳","ハーマイオニー・グレンジャー": "グリフィンドール寮、11歳","ロン・ウィーズリー":"グリフィンドール寮、11歳","ドラコ・マルフォイ": "スリザリン寮、11歳"}
print(seito.keys())
print(seito.values())

for name, info in seito.items():  # items()メソッドでキーと値のペアを取得
    print(f"{name}: {info}")  # 生徒の名前と寮・年齢を表示