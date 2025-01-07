class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"レストラン名：{self.restaurant_name}")
        print(f"料理の種類：{self.cuisine_type}")

    def open_restaurant(self):
        print("レストランは営業中です！")

asanoya = Restaurant("浅野屋","うなぎ")
yosinoya = Restaurant("吉野家","牛丼")
matuya = Restaurant("松屋","牛丼")


asanoya.describe_restaurant()
yosinoya.describe_restaurant()
matuya.describe_restaurant()
