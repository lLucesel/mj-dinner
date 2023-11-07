import MySQLdb
from database import MySQLClientConnector
from pymysql import OperationalError
from pydantic import BaseModel


class FoodDetail:
    def __init__(self, db_name, user, password, host, port):
        self.connector = MySQLClientConnector(db_name, user, password, host, port)

    def food_name(self):
        try:
            food_name = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            """
            food_names = self.connector.fetchall(food_name)
            return food_names
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def side_name(self):
        try:
            self.connector.commit()
            side_name = """
                SELECT name
                FROM food JOIN food_type ON food.food_type_id = food_type.id
                WHERE food_type = '반찬' 
            """
            side_names = self.connector.fetchall(side_name)
            return side_names
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def soup_name(self):
        try:
            soup_name = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' 
            """
            soup_names = self.connector.fetchall(soup_name)
            return soup_names
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def side_detail(self, side_name: str):
        try:
            side_detail = """
            SELECT name, ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' and name = %s
            """
            side_details = self.connector.fetchall(side_detail, (side_name,))
            return side_details
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def soup_detail(self, soup_name: str):
        try:
            soup_detail = """
            SELECT name, ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' and name = %s
            """
            soup_details = self.connector.fetchall(soup_detail, (soup_name,))
            return soup_details
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def side_nutrient(self, side_name: str):
        try:
            side_nutrient = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' and name = %s
            """
            side_nutrients = self.connector.fetchall(side_nutrient, (side_name,))
            return side_nutrients
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def soup_nutrient(self, soup_name: str):
        try:
            soup_nutrient = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' and name = %s
            """
            soup_nutrients = self.connector.fetchall(soup_nutrient, (soup_name,))
            return soup_nutrients
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def side_diet(self):
        try:
            side_diet = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬'
            """
            _side_diet = self.connector.fetchall(side_diet)
            return _side_diet
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def soup_diet(self):
        try:
            soup_diet = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국'
            """
            _soup_diet = self.connector.fetchall(soup_diet)
            return _soup_diet
        except OperationalError:
            return "No data"
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def close_connection(self):
        self.connector.close()
