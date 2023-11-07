from choice import FoodChoice
from database import MySQLClientConnector
from diet import FoodDiet
from detail import FoodDetail
from models import Food, FoodType

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

db = MySQLClientConnector(db_name, user, password, host, port)

print(db.execute("select 1"))
db.close()
