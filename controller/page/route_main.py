import models
from starlette.responses import HTMLResponse
from db.db_conn import db
from starlette import status
from routers.choice import FoodChoice
from routers.detail import FoodDetail
from routers.diet import FoodDiet
from MySQLdb.cursors import DictCursor
from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

posts = []


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


# 등록 페이지 불러오기
@router.get("/add")
async def add(request: Request):
    return (templates.TemplateResponse
            ("add-food.html", {"request": request}))


# 입력 값 등록하기
@router.post("/add", response_class=HTMLResponse)
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
        new_add = models.Food
        new_add.food_type_id = food_type_id
        new_add.name = name
        new_add.ingredient = ingredient
        new_add.spice = spice
        new_add.recipe = recipe
        new_add.calorie = calorie
        new_add.carbohydrate = carbohydrate
        new_add.protein = protein
        new_add.vitamin = vitamin
        _new = (new_add.food_type_id,
                new_add.name, new_add.ingredient, new_add.spice, new_add.recipe,
                new_add.calorie, new_add.carbohydrate, new_add.protein, new_add.vitamin)
        cursor.execute(new, _new)
        db.commit()
        # db.close()

        # 임마 왜 not found로 가냐
        return RedirectResponse(url="/add", status_code=status.HTTP_201_CREATED)


# 검색기능 여기서 이상 생겨서 국만 안나오는듯
@router.get("/food")
async def food(request: Request, food_name: str = None):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        if food_name:
            _food_name = _food_detail.search_food(food_name)
        else:
            _food_name = _food_detail.food_name()
        _food_name = sorted(_food_name, key=lambda x: x["name"])

        return templates.TemplateResponse("search.html", {"request": request, "food_name": _food_name})


@router.get("/food/{food_name}")
async def food_recipe(request: Request, food_name: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _food_details = _food_detail.food_detail(food_name)
        _food_nutrients = _food_detail.food_nutrient(food_name)

        return templates.TemplateResponse(
            "food-recipe.html",
            {"request": request,
             "food_name": food_name,
             "food_detail": _food_details,
             "food_nutrient": _food_nutrients}
        )


# 메인 페이지
@router.get("/community", response_class=HTMLResponse)
async def read(request: Request):
    return templates.TemplateResponse("community.html", {"request": request, "posts": posts})


@router.get("/community/post", response_class=HTMLResponse)
async def read_post(request: Request):
    return templates.TemplateResponse("post.html", {"request": request})


@router.post("/community/post", response_class=HTMLResponse)
async def post(request: Request, title: str = Form(...), content: str = Form(...)):
    # 작성된 글을 리스트에 추가
    posts.append({"title": title, "content": content})
    # 작성 후에는 커뮤니티 글 목록 페이지로 리다이렉션
    return RedirectResponse(url="/community", status_code=303)
