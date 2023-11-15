import random
import MySQLdb
from routers.detail import FoodDetail
# choice는 메인 화면의 랜덤 추첨과 식단 추천에만 씀


class FoodChoice:
    def __init__(self, db):
        self.food_detail = FoodDetail(db)

    def ran_side(self):
        try:
            _ran_side = self.food_detail.side_name()
            if _ran_side is None:
                return "No food_type_id = 1"
            if len(_ran_side) < 3:
                return "Not enough side dishes."
            __ran_side = random.sample(_ran_side, 3)
            ___ran_side = [side["name"] for side in __ran_side]
            result = " / ".join(___ran_side)

            return result
        except MySQLdb.Error as e:
            return f"Error food_type_id = 1: {e}"

    def ran_soup(self):
        try:
            _ran_soup = random.choice(self.food_detail.soup_name())
            if _ran_soup is None:
                return "No food_type_id = 2"
            return _ran_soup["name"]
        except MySQLdb.Error as e:
            return f"Error food_type_id = 2: {e}"

    def diet_side(self):
        try:
            _diet_side = self.food_detail.side_diet()
            if len(_diet_side) < 3:
                return "Not enough side dishes."
            __diet_side = random.sample(_diet_side, 3)
            return __diet_side
        except MySQLdb.Error as e:
            return f"Error food_type_id = 1: {e}"

    def diet_soup(self):
        try:
            _diet_soup = random.choice(self.food_detail.soup_diet())
            return _diet_soup
        except MySQLdb.Error as e:
            return f"Error food_type_id = 2: {e}"
