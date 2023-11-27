import MySQLdb
from MySQLdb.cursors import DictCursor


class FoodDetail:
    def __init__(self, db: DictCursor):
        self.connector = db

    def search_food(self, query):
        try:
            _search = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE name LIKE %s
            """
            food_query = f'%{query}%'
            self.connector.execute(_search, (food_query,))
            search_names = self.connector.fetchall()
            return search_names
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def food_name(self):
        try:
            _food_name = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type='반찬' or food_type='국'
            """
            self.connector.execute(_food_name)
            food_names = self.connector.fetchall()
            return food_names
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def side_name(self):
        try:
            _side_name = """
                SELECT name
                FROM food JOIN food_type ON food.food_type_id = food_type.id
                WHERE food_type = '반찬' 
            """
            self.connector.execute(_side_name)
            side_names = self.connector.fetchall()
            return side_names
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def soup_name(self):
        try:
            soup_name = """
            SELECT name
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' 
            """
            self.connector.execute(soup_name)
            soup_names = self.connector.fetchall()
            return soup_names
        except MySQLdb.Error as e:
            return f"Error name: {e}"

    def side_detail(self, side_name: str):
        try:
            side_detail = """
            SELECT name, ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' and name = %s
            """
            self.connector.execute(side_detail, (side_name,))
            side_details = self.connector.fetchall()
            return side_details
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def soup_detail(self, soup_name: str):
        try:
            soup_detail = """
            SELECT name, ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' and name = %s
            """
            self.connector.execute(soup_detail, (soup_name,))
            soup_details = self.connector.fetchall()
            return soup_details
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def food_detail(self, food_name: str):
        try:
            food_detail = """
            SELECT name, ingredient, spice, recipe
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE name = %s
            """
            self.connector.execute(food_detail, (food_name,))
            soup_details = self.connector.fetchall()
            return soup_details
        except MySQLdb.Error as e:
            return f"Error detail: {e}"

    def side_nutrient(self, side_name: str):
        try:
            side_nutrient = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬' and name = %s
            """
            self.connector.execute(side_nutrient, (side_name,))
            side_nutrients = self.connector.fetchall()
            return side_nutrients
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def soup_nutrient(self, soup_name: str):
        try:
            soup_nutrient = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국' and name = %s
            """
            self.connector.execute(soup_nutrient, (soup_name,))
            soup_nutrients = self.connector.fetchall()
            return soup_nutrients
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def food_nutrient(self, food_name: str):
        try:
            food_nutrient = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE name = %s
            """
            self.connector.execute(food_nutrient, (food_name,))
            soup_nutrients = self.connector.fetchall()
            return soup_nutrients
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def side_diet(self):
        try:
            side_diet = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '반찬'
            """
            self.connector.execute(side_diet)
            _side_diet = self.connector.fetchall()
            return _side_diet
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def soup_diet(self):
        try:
            soup_diet = """
            SELECT name, calorie, carbohydrate, protein, vitamin
            FROM food JOIN food_type ON food.food_type_id = food_type.id
            WHERE food_type = '국'
            """
            self.connector.execute(soup_diet)
            _soup_diet = self.connector.fetchall()
            return _soup_diet
        except MySQLdb.Error as e:
            return f"Error nutrient: {e}"

    def todo(self):
        try:
            _todo = """
            SELECT id, content, complete
            FROM todo
            """
            self.connector.execute(_todo)
            __todo = self.connector.fetchall()
            return __todo
        except MySQLdb.Error as e:
            return f"Error todo: {e}"

    def add_todo(self, content: str):
        try:
            _add_todo = """
            INSERT INTO todo (content, complete)
            VALUES (%s, false)
            """
            self.connector.execute(_add_todo, (content,))
            __add_todo = self.connector.fetchall()
            return f"Todo '{content}' added successfully"
        except MySQLdb.Error as e:
            return f"Error add_todo: {e}"

    def delete_todo(self, id: int):
        try:
            _delete_todo = """
            DELETE FROM todo
            WHERE id = %s
            """
            self.connector.execute(_delete_todo, (id,))
            __delete_todo = self.connector.fetchall()
            return f"Todo {id} deleted successfully"
        except MySQLdb.Error as e:
            return f"Error delete todo: {e}"

    def close_connection(self):
        self.connector.close()
