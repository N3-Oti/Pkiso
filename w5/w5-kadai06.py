class Restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"レストラン名：{self.restaurant_name}")
        print(f"料理の種類：{self.cuisine_type}")

    def open_restaurant(self):
        print("レストランは営業中です！")

    def served_restaurant(self):
        print(f"これまで{self.number_served}人が来店しました")

    def set_number_served(self,number_served):
        self.number_served = number_served
        print(f"{self.number_served}人に変更しました")

    def increment_number_served(self):
        self.number_served = self.number_served + 1
        print(f"現在{self.number_served}人が来店しました")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,flavors,number_served=0):
        super().__init__(restaurant_name, "アイスクリーム屋", number_served)
        if isinstance(flavors, list): #指定されたオブジェクトが指定されたデータ型かどうかを判定
            self.flavors = flavors
        else:
            raise TypeError("flavors属性にはリストを指定してください。")

    def ice_list(self):
        print(f"フレバーリスト：{self.flavors}")


restaurant = Restaurant("浅野屋","うなぎ",)
#test31 = IceCreamStand("サーティーワン","ばにら、ちょこ、ミント")
Ice31 = IceCreamStand("サーティーワン",["バニラ","チョコ","ミント"])

Ice31.ice_list()

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.served_restaurant()
restaurant.set_number_served(243)
restaurant.increment_number_served()
restaurant.increment_number_served()
restaurant.increment_number_served()