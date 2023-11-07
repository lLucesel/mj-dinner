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
_food_choice = FoodChoice(db_name, user, password, host, port)
_food_detail = FoodDetail(db_name, user, password, host, port)
_food_diet = FoodDiet(db_name, user, password, host, port)

_delete = """
    DELETE food
    FROM food
    INNER JOIN food_type ON food.food_type_id = food_type.id
    WHERE name = %s and food_type_id = 1
    """

print("!")
db.execute(_delete, ('테스트메뉴1',))
print("!")
db.commit()
print("!")