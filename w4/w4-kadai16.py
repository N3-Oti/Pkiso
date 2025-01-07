def make_album(name,title,tracks=""):#アーティスト名とタイトルでアルバム作成
    album = {"artist":name,"title":title}
    if tracks:
        album["tracks"] = tracks
    return album

album1 = make_album("b'z","b'z best",12)
album2 = make_album("dareka","koreka")
album3 = make_album("test","best")

print(album1)
print(album2)
print(album3)