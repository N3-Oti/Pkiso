kawas = {
    "四万十川":"日本",
    "長江":"中国",
    "ミシシッピ川":"アメリカ"
}
for name,kuni in kawas.items():
    print(f"{name}は{kuni}にあります。")
print()

for name in kawas.keys():
    print(f"河川名:{name}")
print()

for kuni in kawas.values():
    print(f"国名:{kuni}")