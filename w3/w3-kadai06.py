tiwawa = {
    "name":"tiwawa",
    "date":{"ani":"dog","owner":"taro"}
    }
mikecat = {
    "name":"mikecat",
    "date":{"ani":"cat","owner":"mio"}
    }
sibadog = {
    "name":"sibadog",
    "date":{"ani":"dog","owner":"hanako"}
    }
pets = [tiwawa,mikecat,sibadog]

for i in pets:
    name = i.get("name","no_name")
    ani = i.get("date","no_date").get("ani","no_ani")
    owner = i.get("date","no_date").get("owner","no_owner")
    print (f"{name}は{ani}の一種です。飼い主は{owner}です。")