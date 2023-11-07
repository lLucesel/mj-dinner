from fastapi import APIRouter
from database import MySQLClientConnector
import random

router = APIRouter()

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

db = MySQLClientConnector(db_name, user, password, host, port)


@router.get("/")
async def get_random():
    result_side_data = db.side()
    result_soup_data = db.soup()
    db.close()

    if result_side_data:
        random_side = random.choice(result_side_data)
        random_side_name = random_side["name"]
        return random_side_name
    else:
        return {"error": "No items found with food_type_id = 1"}

    if result_soup_data:
        random_soup = random.choice(result_soup_data)
        random_soup_name = random_soup["name"]
        return random_soup_name
    else:
        return {"error": "No items found with food_type_id = 2"}
