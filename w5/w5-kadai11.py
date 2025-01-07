from users2 import *
from users3 import *

taro = User("Taro","Yamada",32,"password")
sato = User("Tomoki","Sato",23,"p@Ssw0rd")
hanako = User("Hanako","Tanaka",25,"112233")
masaki = Admin("Masaki","Tanaka",24,"root","111")
tasaki = Admin("Maya","Tasaki",24,"ro0ot","011")

masaki.show_privileges()
tasaki.show_privileges()