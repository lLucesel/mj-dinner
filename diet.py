import random
import MySQLdb
from database import MySQLClientConnector
from detail import FoodDetail
from choice import FoodChoice
from pymysql import OperationalError


class FoodDiet:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.food_detail = FoodDetail(db_name, user, password, host, port)
        self.food_choice = FoodChoice(db_name, user, password, host, port)
        self.diet_plans = []

    def diet_plan(self):
        # 7 미만일 경우 반복
        while len(self.diet_plans) < 7:
            _diet_set = self.diet_set()
            #if self.valid_diet_set(_diet_set):
            self.diet_plans.append(_diet_set)
        return self.diet_plans, self.close_connection()

    def diet_set(self):
        try:
            # 반찬 3개, 국 1개의 칼로리들의 합이 2000이상 2300이하가 될 때까지 무한 반복
            while True:
                # 반찬 3개 중복 안되게 칼로리, 영양성분, 이름을 리스트 안의 딕셔너리로 소환
                _diet_side = self.food_choice.diet_side()
                # 국 1개 칼로리, 영양성분, 이름을 딕셔너리로 소환 후 리스트로 다시 바꾸기
                _diet_soup = self.food_choice.diet_soup()
                __diet_soup = [_diet_soup]
                # 딕셔너리로 이루어진 반찬 3개와 국 1개의 리스트 만들기
                _diet_set = _diet_side + __diet_soup
                # 만든 리스트에서 calorie에 해당하는 인덱스의 합 구하기
                sum_cal = sum(food["calorie"] for food in _diet_set)
                # 그 합이 다음 조건을 만족할 경우 초기화 하고 돌아가기
                if not 2000 <= sum_cal <= 2300:
                    _diet_set = list()
                    continue
                # 안 만족하면 _diet_set으로 돌아가기
                else:
                    return _diet_set
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    #def valid_diet_set(self, diet_set):
    #    #todo set 바꾸자
    #    diet_names = set(diet["name"] for diet in self.diet_plans)
    #    for food in diet_set:
    #        if food["name"] in diet_names:
    #            return False
    #    return True

    def close_connection(self):
        self.connector.close()
