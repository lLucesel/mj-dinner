import MySQLdb
from MySQLdb.cursors import DictCursor
from routers.choice import FoodChoice
from routers.detail import FoodDetail


# 식단짜기에서만 사용
class FoodDiet:
    def __init__(self, db: DictCursor):
        self.food_detail = FoodDetail(db)
        self.food_choice = FoodChoice(db)
        self.diet_plans = []

    def diet_plan(self):
        # 7 미만일 경우 반복
        while len(self.diet_plans) < 7:
            _diet_set = self.diet_set()
            # if self.valid_diet_set(_diet_set):
            self.diet_plans.append(_diet_set)
        return self.diet_plans

    def diet_set(self):
        try:
            # 반찬 3개, 국 1개의 칼로리들의 합이 500이상 800이하가 될 때까지 무한 반복
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
                if not 650 <= sum_cal <= 800:
                    _diet_set = list()
                    continue
                # 안 만족하면 _diet_set으로 돌아가기
                else:
                    return _diet_set
        except MySQLdb.Error as e:
            return f"Error detail: {e}"
