from MySQLdb.cursors import DictCursor
from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from choice import FoodChoice
from detail import FoodDetail
from diet import FoodDiet

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def main(request: Request):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_choice = FoodChoice(cursor)
        ran_side_name = _food_choice.ran_side()
        ran_soup_name = _food_choice.ran_soup()

        return (templates.TemplateResponse
                ("main.html", {"request": request,
                               "side_name": ran_side_name,
                               "soup_name": ran_soup_name}))


@router.get("/side")
async def side(request: Request):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _side_name = _food_detail.side_name()
        _side_name = sorted(_side_name, key=lambda x: x["name"])

        return (templates.TemplateResponse
                ("side.html", {"request": request, "side_name": _side_name}))


@router.get("/soup")
async def soup(request: Request):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _soup_name = _food_detail.soup_name()
        _soup_name = sorted(_soup_name, key=lambda x: x["name"])

        return (templates.TemplateResponse
                ("soup.html", {"request": request, "soup_name": _soup_name}))


@router.get("/side/{side_name}")
async def side_recipe(request: Request, side_name: str):
    # 클릭해서 들어간 side_name에 해당하는 요소들을 갖고와야함
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _side_details = _food_detail.side_detail(side_name)
        _side_nutrients = _food_detail.side_nutrient(side_name)

        return (templates.TemplateResponse(
            "side-recipe.html",
            {"request": request,
             "side_name": side_name,
             "side_detail": _side_details,
             "side_nutrient": _side_nutrients}
        ))


@router.post("/side/{side_name}")
async def delete_side(request: Request, side_name: str, _method: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        if _method == "delete":
            _delete = """
            DELETE food
            FROM food
            INNER JOIN food_type ON food.food_type_id = food_type.id
            WHERE name = %s and food_type_id = 1
            """
            cursor.execute(_delete, (side_name,))
            cursor.commit()
    return RedirectResponse(url="/side")


@router.get("/soup/{soup_name}")
async def soup_recipe(request: Request, soup_name: str):
    # 클릭해서 들어간 soup_name에 해당하는 요소들을 갖고 와야함
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _soup_details = _food_detail.soup_detail(soup_name)
        _soup_nutrients = _food_detail.soup_nutrient(soup_name)

        return (templates.TemplateResponse(
            "soup-recipe.html",
            {"request": request,
             "soup_name": soup_name,
             "soup_detail": _soup_details,
             "soup_nutrient": _soup_nutrients}
        ))


@router.delete("/soup/{soup_name}")
async def delete_soup(request: Request, soup_name: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _delete = """
        DELETE food
        FROM food
        INNER JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s and food_type_id = 2
        """
        cursor.execute(_delete, (soup_name,))
        cursor.commit()
        cursor.close()

        return RedirectResponse(url="/soup")


@router.get("/diet")
async def diet(request: Request):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_diet = FoodDiet(cursor)
        _diet = _food_diet.diet_plan()
    sun_side_cal = _diet[0][0]["calorie"] + _diet[0][1]["calorie"] + _diet[0][2]["calorie"]
    mon_side_cal = _diet[1][0]["calorie"] + _diet[1][1]["calorie"] + _diet[1][2]["calorie"]
    tue_side_cal = _diet[2][0]["calorie"] + _diet[2][1]["calorie"] + _diet[2][2]["calorie"]
    wed_side_cal = _diet[3][0]["calorie"] + _diet[3][1]["calorie"] + _diet[3][2]["calorie"]
    thu_side_cal = _diet[4][0]["calorie"] + _diet[4][1]["calorie"] + _diet[4][2]["calorie"]
    fri_side_cal = _diet[5][0]["calorie"] + _diet[5][1]["calorie"] + _diet[5][2]["calorie"]
    sat_side_cal = _diet[6][0]["calorie"] + _diet[6][1]["calorie"] + _diet[6][2]["calorie"]

    sun_soup_cal = _diet[0][3]["calorie"]
    mon_soup_cal = _diet[1][3]["calorie"]
    tue_soup_cal = _diet[2][3]["calorie"]
    wed_soup_cal = _diet[3][3]["calorie"]
    thu_soup_cal = _diet[4][3]["calorie"]
    fri_soup_cal = _diet[5][3]["calorie"]
    sat_soup_cal = _diet[6][3]["calorie"]

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

    sun_car = (_diet[0][0]["carbohydrate"] + _diet[0][1]["carbohydrate"] +
               _diet[0][2]["carbohydrate"] + _diet[0][3]["carbohydrate"])
    mon_car = (_diet[1][0]["carbohydrate"] + _diet[1][1]["carbohydrate"] +
               _diet[1][2]["carbohydrate"] + _diet[1][3]["carbohydrate"])
    tue_car = (_diet[2][0]["carbohydrate"] + _diet[2][1]["carbohydrate"] +
               _diet[2][2]["carbohydrate"] + _diet[2][3]["carbohydrate"])
    wed_car = (_diet[3][0]["carbohydrate"] + _diet[3][1]["carbohydrate"] +
               _diet[3][2]["carbohydrate"] + _diet[3][3]["carbohydrate"])
    thu_car = (_diet[4][0]["carbohydrate"] + _diet[4][1]["carbohydrate"] +
               _diet[4][2]["carbohydrate"] + _diet[4][3]["carbohydrate"])
    fri_car = (_diet[5][0]["carbohydrate"] + _diet[5][1]["carbohydrate"] +
               _diet[5][2]["carbohydrate"] + _diet[5][3]["carbohydrate"])
    sat_car = (_diet[6][0]["carbohydrate"] + _diet[6][1]["carbohydrate"] +
               _diet[6][2]["carbohydrate"] + _diet[6][3]["carbohydrate"])
    all_car = sun_car + mon_car + tue_car + wed_car + thu_car + fri_car + sat_car

    sun_pro = (_diet[0][0]["protein"] + _diet[0][1]["protein"] +
               _diet[0][2]["protein"] + _diet[0][3]["protein"])
    mon_pro = (_diet[1][0]["protein"] + _diet[1][1]["protein"] +
               _diet[1][2]["protein"] + _diet[1][3]["protein"])
    tue_pro = (_diet[2][0]["protein"] + _diet[2][1]["protein"] +
               _diet[2][2]["protein"] + _diet[2][3]["protein"])
    wed_pro = (_diet[3][0]["protein"] + _diet[3][1]["protein"] +
               _diet[3][2]["protein"] + _diet[3][3]["protein"])
    thu_pro = (_diet[4][0]["protein"] + _diet[4][1]["protein"] +
               _diet[4][2]["protein"] + _diet[4][3]["protein"])
    fri_pro = (_diet[5][0]["protein"] + _diet[5][1]["protein"] +
               _diet[5][2]["protein"] + _diet[5][3]["protein"])
    sat_pro = (_diet[6][0]["protein"] + _diet[6][1]["protein"] +
               _diet[6][2]["protein"] + _diet[6][3]["protein"])
    all_pro = sun_pro + mon_pro + tue_pro + wed_pro + thu_pro + fri_pro + sat_pro

    sun_vit = (_diet[0][0]["vitamin"] + _diet[0][1]["vitamin"] +
               _diet[0][2]["vitamin"] + _diet[0][3]["vitamin"])
    mon_vit = (_diet[1][0]["vitamin"] + _diet[1][1]["vitamin"] +
               _diet[1][2]["vitamin"] + _diet[1][3]["vitamin"])
    tue_vit = (_diet[2][0]["vitamin"] + _diet[2][1]["vitamin"] +
               _diet[2][2]["vitamin"] + _diet[2][3]["vitamin"])
    wed_vit = (_diet[3][0]["vitamin"] + _diet[3][1]["vitamin"] +
               _diet[3][2]["vitamin"] + _diet[3][3]["vitamin"])
    thu_vit = (_diet[4][0]["vitamin"] + _diet[4][1]["vitamin"] +
               _diet[4][2]["vitamin"] + _diet[4][3]["vitamin"])
    fri_vit = (_diet[5][0]["vitamin"] + _diet[5][1]["vitamin"] +
               _diet[5][2]["vitamin"] + _diet[5][3]["vitamin"])
    sat_vit = (_diet[6][0]["vitamin"] + _diet[6][1]["vitamin"] +
               _diet[6][2]["vitamin"] + _diet[6][3]["vitamin"])
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


@router.get("/add")
async def add(request: Request):
    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


@router.post("/add")
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
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        new = """
        INSERT INTO food (food_type_id, name, ingredient, spice, recipe,
        calorie, carbohydrate, protein, vitamin)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        _new = (food_type_id,
                name, ingredient, spice, recipe,
                calorie, carbohydrate, protein, vitamin)
        cursor.execute(new, _new)
        cursor.commit()
        cursor.close()

        return (templates.TemplateResponse
                ("add-food.html", {"request": request}))


@router.get("/food")
async def food(request: Request):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _food_name = _food_detail.food_name()
        _food_name = sorted(_food_name, key=lambda x: x["name"])

        return (templates.TemplateResponse
                ("search.html", {"request": request, "food_name": _food_name}))
