import uvicorn
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from choice import FoodChoice
from detail import FoodDetail
from database import MySQLClientConnector
from diet import FoodDiet
from models import Food, FoodType

app = FastAPI()
templates = Jinja2Templates(directory="templates")

db_name = "dinner"
user = "admin_mj"
password = "77gundam77"
host = "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com"
port = 3306

db = MySQLClientConnector(db_name, user, password, host, port)
_food_choice = FoodChoice(db_name, user, password, host, port)
_food_detail = FoodDetail(db_name, user, password, host, port)
_food_diet = FoodDiet(db_name, user, password, host, port)


@app.get("/")
async def main(request: Request):
    ran_side_name = _food_choice.ran_side()
    ran_soup_name = _food_choice.ran_soup()

    return (templates.TemplateResponse
            ("main.html", {"request": request,
                           "side_name": ran_side_name,
                           "soup_name": ran_soup_name}))


@app.get("/side")
async def side(request: Request):
    _side_name = _food_detail.side_name()
    _side_name = sorted(_side_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("side.html", {"request": request, "side_name": _side_name}))


@app.get("/soup")
async def soup(request: Request):
    _soup_name = _food_detail.soup_name()
    _soup_name = sorted(_soup_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("soup.html", {"request": request, "soup_name": _soup_name}))


@app.get("/side/{side_name}")
async def side_recipe(request: Request, side_name: str):
    # 클릭해서 들어간 side_name에 해당하는 요소들을 갖고와야함

    _side_details = _food_detail.side_detail(side_name)
    _side_nutrients = _food_detail.side_nutrient(side_name)

    return (templates.TemplateResponse(
        "side-recipe.html",
        {"request": request,
         "side_name": side_name,
         "side_detail": _side_details,
         "side_nutrient": _side_nutrients}
    ))


@app.put("/side/{side_name}")
async def update_side(request: Request, side_name: str, _food: Food):
    _update = """
    UPDATE food A
    INNER JOIN food_type B ON A.food_type_id = B.id
    SET A.name = %s, A.ingredient = %s, A.spice = %s, A.recipe = %s,
    A.calorie = %s, A.carbohydrate = %s, A.protein = %s, A.vitamin = %s
    WHERE A.name = %s
    """
    values = (_food.name, _food.ingredient, _food.spice, _food.recipe,
              _food.calorie, _food.carbohydrate, _food.protein, _food.vitamin)
    db.execute(_update, values)
    db.commit()
    db.close()


@app.post("/side/{side_name}")
async def delete_side(request: Request, side_name: str, _method: str):
    if method_type == "delete":
        _delete = """
        DELETE food
        FROM food
        INNER JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s and food_type_id = 1
        """
        db.execute(_delete, (side_name,))
        db.commit()
        db.close()

    return RedirectResponse(url="/side")


@app.get("/soup/{soup_name}")
async def soup_recipe(request: Request, soup_name: str):
    # 클릭해서 들어간 soup_name에 해당하는 요소들을 갖고 와야함
    _soup_details = _food_detail.soup_detail(soup_name)
    _soup_nutrients = _food_detail.soup_nutrient(soup_name)

    return (templates.TemplateResponse(
        "soup-recipe.html",
        {"request": request,
         "soup_name": soup_name,
         "soup_detail": _soup_details,
         "soup_nutrient": _soup_nutrients}
    ))


@app.delete("/soup/{soup_name}")
async def delete_soup(request: Request, soup_name: str):
    _delete = """
    DELETE food
    FROM food
    INNER JOIN food_type ON food.food_type_id = food_type.id
    WHERE name = %s and food_type_id = 2
    """
    db.execute(_delete, (soup_name,))
    db.commit()
    db.close()

    return RedirectResponse(url="/soup")


@app.get("/diet")
async def diet(request: Request):
    _diet = _food_diet.diet_plan()

    print(type(_diet))
    print(_diet[0])

    sun_side_cal = _diet[0][0][0]["calorie"] + _diet[0][0][1]["calorie"] + _diet[0][0][2]["calorie"]
    mon_side_cal = _diet[0][1][0]["calorie"] + _diet[0][1][1]["calorie"] + _diet[0][1][2]["calorie"]
    tue_side_cal = _diet[0][2][0]["calorie"] + _diet[0][2][1]["calorie"] + _diet[0][2][2]["calorie"]
    wed_side_cal = _diet[0][3][0]["calorie"] + _diet[0][3][1]["calorie"] + _diet[0][3][2]["calorie"]
    thu_side_cal = _diet[0][4][0]["calorie"] + _diet[0][4][1]["calorie"] + _diet[0][4][2]["calorie"]
    fri_side_cal = _diet[0][5][0]["calorie"] + _diet[0][5][1]["calorie"] + _diet[0][5][2]["calorie"]
    sat_side_cal = _diet[0][6][0]["calorie"] + _diet[0][6][1]["calorie"] + _diet[0][6][2]["calorie"]

    sun_soup_cal = _diet[0][0][3]["calorie"]
    mon_soup_cal = _diet[0][1][3]["calorie"]
    tue_soup_cal = _diet[0][2][3]["calorie"]
    wed_soup_cal = _diet[0][3][3]["calorie"]
    thu_soup_cal = _diet[0][4][3]["calorie"]
    fri_soup_cal = _diet[0][5][3]["calorie"]
    sat_soup_cal = _diet[0][6][3]["calorie"]

    sun_cal = sun_side_cal + sun_soup_cal
    mon_cal = mon_side_cal + mon_soup_cal
    tue_cal = tue_side_cal + tue_soup_cal
    wed_cal = wed_side_cal + wed_soup_cal
    thu_cal = thu_side_cal + thu_soup_cal
    fri_cal = fri_side_cal + fri_soup_cal
    sat_cal = sat_side_cal + sat_soup_cal

    all_side = sun_side_cal + mon_side_cal + tue_side_cal + wed_side_cal + thu_side_cal + fri_side_cal + sat_side_cal
    all_soup = sun_soup_cal + mon_soup_cal + tue_soup_cal + wed_soup_cal + thu_soup_cal + fri_soup_cal + sat_soup_cal
    all_food = all_side + all_soup

    sun_car = (_diet[0][0][0]["carbohydrate"] + _diet[0][0][1]["carbohydrate"] +
               _diet[0][0][2]["carbohydrate"] + _diet[0][0][3]["carbohydrate"])
    mon_car = (_diet[0][1][0]["carbohydrate"] + _diet[0][1][1]["carbohydrate"] +
               _diet[0][1][2]["carbohydrate"] + _diet[0][1][3]["carbohydrate"])
    tue_car = (_diet[0][2][0]["carbohydrate"] + _diet[0][2][1]["carbohydrate"] +
               _diet[0][2][2]["carbohydrate"] + _diet[0][2][3]["carbohydrate"])
    wed_car = (_diet[0][3][0]["carbohydrate"] + _diet[0][3][1]["carbohydrate"] +
               _diet[0][3][2]["carbohydrate"] + _diet[0][3][3]["carbohydrate"])
    thu_car = (_diet[0][4][0]["carbohydrate"] + _diet[0][4][1]["carbohydrate"] +
               _diet[0][4][2]["carbohydrate"] + _diet[0][4][3]["carbohydrate"])
    fri_car = (_diet[0][5][0]["carbohydrate"] + _diet[0][5][1]["carbohydrate"] +
               _diet[0][5][2]["carbohydrate"] + _diet[0][5][3]["carbohydrate"])
    sat_car = (_diet[0][6][0]["carbohydrate"] + _diet[0][6][1]["carbohydrate"] +
               _diet[0][6][2]["carbohydrate"] + _diet[0][6][3]["carbohydrate"])
    all_car = sun_car + mon_car + tue_car + wed_car + thu_car + fri_car + sat_car

    sun_pro = (_diet[0][0][0]["protein"] + _diet[0][0][1]["protein"] +
               _diet[0][0][2]["protein"] + _diet[0][0][3]["protein"])
    mon_pro = (_diet[0][1][0]["protein"] + _diet[0][1][1]["protein"] +
               _diet[0][1][2]["protein"] + _diet[0][1][3]["protein"])
    tue_pro = (_diet[0][2][0]["protein"] + _diet[0][2][1]["protein"] +
               _diet[0][2][2]["protein"] + _diet[0][2][3]["protein"])
    wed_pro = (_diet[0][3][0]["protein"] + _diet[0][3][1]["protein"] +
               _diet[0][3][2]["protein"] + _diet[0][3][3]["protein"])
    thu_pro = (_diet[0][4][0]["protein"] + _diet[0][4][1]["protein"] +
               _diet[0][4][2]["protein"] + _diet[0][4][3]["protein"])
    fri_pro = (_diet[0][5][0]["protein"] + _diet[0][5][1]["protein"] +
               _diet[0][5][2]["protein"] + _diet[0][5][3]["protein"])
    sat_pro = (_diet[0][6][0]["protein"] + _diet[0][6][1]["protein"] +
               _diet[0][6][2]["protein"] + _diet[0][6][3]["protein"])
    all_pro = sun_pro + mon_pro + tue_pro + wed_pro + thu_pro + fri_pro + sat_pro

    sun_vit = (_diet[0][0][0]["vitamin"] + _diet[0][0][1]["vitamin"] +
               _diet[0][0][2]["vitamin"] + _diet[0][0][3]["vitamin"])
    mon_vit = (_diet[0][1][0]["vitamin"] + _diet[0][1][1]["vitamin"] +
               _diet[0][1][2]["vitamin"] + _diet[0][1][3]["vitamin"])
    tue_vit = (_diet[0][2][0]["vitamin"] + _diet[0][2][1]["vitamin"] +
               _diet[0][2][2]["vitamin"] + _diet[0][2][3]["vitamin"])
    wed_vit = (_diet[0][3][0]["vitamin"] + _diet[0][3][1]["vitamin"] +
               _diet[0][3][2]["vitamin"] + _diet[0][3][3]["vitamin"])
    thu_vit = (_diet[0][4][0]["vitamin"] + _diet[0][4][1]["vitamin"] +
               _diet[0][4][2]["vitamin"] + _diet[0][4][3]["vitamin"])
    fri_vit = (_diet[0][5][0]["vitamin"] + _diet[0][5][1]["vitamin"] +
               _diet[0][5][2]["vitamin"] + _diet[0][5][3]["vitamin"])
    sat_vit = (_diet[0][6][0]["vitamin"] + _diet[0][6][1]["vitamin"] +
               _diet[0][6][2]["vitamin"] + _diet[0][6][3]["vitamin"])
    all_vit = sun_vit + mon_vit + tue_vit + wed_vit + thu_vit + fri_vit + sat_vit

    return (templates.TemplateResponse
            ("diet.html", {"request": request,
                           "_diet": _diet, "all_soup": all_soup,
                           "sun_cal": sun_cal, "mon_cal": mon_cal, "tue_cal": tue_cal, "wed_cal": wed_cal,
                           "thu_cal": thu_cal, "fri_cal": fri_cal, "sat_cal": sat_cal, "all_cal": all_food,
                           "sun_car": sun_car, "mon_car": mon_car, "tue_car": tue_car, "wed_car": wed_car,
                           "thu_car": thu_car, "fri_car": fri_car, "sat_car": sat_car, "all_car": all_car,
                           "sun_pro": sun_pro, "mon_pro": mon_pro, "tue_pro": tue_pro, "wed_pro": wed_pro,
                           "thu_pro": thu_pro, "fri_pro": fri_pro, "sat_pro": sat_pro, "all_pro": all_pro,
                           "sun_vit": sun_vit, "mon_vit": mon_vit, "tue_vit": tue_vit, "wed_vit": wed_vit,
                           "thu_vit": thu_vit, "fri_vit": fri_vit, "sat_vit": sat_vit, "all_vit": all_vit
                           }))


@app.get("/add")
async def add(request: Request):
    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


@app.post("/add")
async def add(request: Request,
              food_type_id: int = Form(...),
              name: str = Form(...),
              ingredient: str = Form(...),
              spice: str = Form(...),
              recipe: str = Form(...),
              calorie: int = Form(...),
              carbohydrate: int = Form(...),
              protein: int = Form(...),
              vitamin: int = Form(...)
              ):
    new = """
    INSERT INTO food (food_type_id, name, ingredient, spice, recipe,
    calorie, carbohydrate, protein, vitamin)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    _new = (food_type_id,
            name, ingredient, spice, recipe,
            calorie, carbohydrate, protein, vitamin)
    db.execute(new, _new)
    db.commit()
    db.close()

    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


@app.get("/food")
async def food(request: Request):
    _food_name = _food_detail.food_name()
    _food_name = sorted(_food_name, key=lambda x: x["name"])

    return (templates.TemplateResponse
            ("search.html", {"request": request, "food_name": _food_name}))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
