def make_album(name,title,tracks=""):#アーティスト名とタイトルでアルバム作成
    album = {"artist":name,"title":title} #単体辞書
    if tracks:
        album["tracks"] = tracks
    return album


def get_album_info(num): #単体アルバム情報入力関数
    while 1:
        artist = input(f"アルバム{num}のアーティスト名を入力してください（終了するにはqを入力してください）: ")
        artist = artist.strip()
        if artist == "q":
            print("プログラムを終了します。")
            exit()
        elif artist:
            break
        else:
            print("アーティスト名入力は必須です。")

    while 1:
        title = input(f"アルバム{num}のタイトルを入力してください（終了するにはqを入力してください）: ")
        title = title.strip()
        if title == "q":
            print("プログラムを終了します。")
            exit()

        elif title:
            break
        else:
            print("タイトル入力は必須です。")

    while 1:
        tracks = input(f"アルバム{num}の曲数を入力してください（省略可）]（終了するにはqを入力してください）: ")
        if tracks == "q":
            print("プログラムを終了します。")
            exit()
        elif tracks:
            try:
                tracks = int(tracks)
                break
            except ValueError:
                print("無効な入力です。整数で入力してください。")
        else:
            tracks = ""
            break

    return make_album(artist, title, tracks) #単体辞書作成

albums = {} #全体辞書

while 1: #全体辞書に単体を入れるループ
    num_x = input("アルバム番号を入力してください（終了するにはqを入力してください）: ")
    if num_x == 'q':
        break

    try:
        num = int(num_x)
    except ValueError:
        print("無効な入力です。整数で入力してください。")
        continue

    albums[num] = get_album_info(num) #番号付けして全体に入れる

print("\n作成したアルバム一覧:")
for num, album in albums.items():
    print(f"アルバム{num}: {album}")
