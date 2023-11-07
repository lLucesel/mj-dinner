import MySQLdb
from detail import FoodDetail
from database import MySQLClientConnector
from pymysql import OperationalError


class FoodBring:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)
        self.side_name = self.connector.side_name()
        self.soup_name = self.connector.soup_name()
        self.side_detail = self.connector.side_detail()
        self.soup_detail = self.connector.soup_detail()
        self.side_nutrient = self.connector.side_nutrient()
        self.soup_nutrient = self.connector.soup_nutrient()

    def side_bring(self, name):
        try:
            # 데이터베이스에서 해당 이름(name)에 해당하는 스프 세부 정보 가져오는 코드
            cursor = self.connector.cursor()
            query = """SELECT ingredient, spice, recipe, calorie, carbohydrate, protein, vitamin
                     FROM food JOIN food_type ON food.food_type_id = food_type.id
                     WHERE name = %s"""
            cursor.execute(query, (name,))
            side_detail = cursor.fetchone()

            if side_detail:
                return {
                    "ingredient": side_detail[0],
                    "spice": side_detail[1],
                    "recipe": side_detail[2],
                    "calorie": side_detail[3],
                    "carbohydrate": side_detail[4],
                    "protein": side_detail[5],
                    "vitamin": side_detail[6],
                }
            else:
                return "No data"

        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error: {e}"
