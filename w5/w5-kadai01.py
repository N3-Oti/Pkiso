class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"レストラン名：{self.restaurant_name}")
        print(f"料理の種類：{self.cuisine_type}")

    def open_restaurant(self):
        print("レストランは営業中です！")

restaurant = Restaurant("浅野屋","うなぎ")


restaurant.describe_restaurant()
restaurant.open_restaurant()