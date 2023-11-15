import models
from starlette import status
from starlette.requests import Request
from starlette.responses import HTMLResponse
from models import Food, FoodType
from db.db_conn import db
from MySQLdb.cursors import DictCursor
from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from routers.detail import FoodDetail

router = APIRouter()
templates = Jinja2Templates(directory="templates")


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


@router.post("/side/{side_name}/delete")
async def delete_side(request: Request, side_name: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _delete = """
        DELETE food
        FROM food
        INNER JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s and food_type_id = 1
        """
        cursor.execute(_delete, (side_name,))
        db.commit()
        # db.close()

    return RedirectResponse(url="/side", status_code=status.HTTP_204_NO_CONTENT)


@router.post("/soup/{soup_name}/delete")
async def delete_soup(request: Request, soup_name: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _delete = """
        DELETE food
        FROM food
        INNER JOIN food_type ON food.food_type_id = food_type.id
        WHERE name = %s and food_type_id = 2
        """
        cursor.execute(_delete, (soup_name,))
        db.commit()
        # db.close()

        return RedirectResponse(url="/soup", status_code=status.HTTP_204_NO_CONTENT)


@router.get("/side/{side_name}/edit")
async def update_side(request: Request, side_name: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _side_details = _food_detail.side_detail(side_name)
        _side_nutrients = _food_detail.side_nutrient(side_name)

    return templates.TemplateResponse(
        "side-edit.html", {"request": request,
                           "side_name": side_name,
                           "side_detail": _side_details,
                           "side_nutrient": _side_nutrients}
    )


@router.get("/soup/{soup_name}/edit")
async def update_soup(request: Request, soup_name: str):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _food_detail = FoodDetail(cursor)
        _soup_details = _food_detail.soup_detail(soup_name)
        _soup_nutrients = _food_detail.soup_nutrient(soup_name)

    return templates.TemplateResponse(
        "soup-edit.html", {"request": request,
                           "soup_name": soup_name,
                           "soup_detail": _soup_details,
                           "soup_nutrient": _soup_nutrients}
    )


@router.post("/side/{side_name}/edit")
async def update_side_recipe(request: Request, side_name: str,
                             ingredient: str = Form(...),
                             spice: str = Form(...),
                             recipe: str = Form(...),
                             calorie: int = Form(...),
                             carbohydrate: int = Form(...),
                             protein: int = Form(...),
                             vitamin: int = Form(...)
                             ):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _update = """
        UPDATE food
        INNER JOIN food_type ON food.food_type_id = food_type.id
        SET ingredient = %s, spice = %s, recipe = %s,
        calorie = %s, carbohydrate = %s, protein = %s, vitamin = %s
        WHERE name = %s and food_type = '반찬'
        """
        _new = (ingredient, spice, recipe,
                calorie, carbohydrate, protein, vitamin,
                side_name)
        cursor.execute(_update, _new)
        db.commit()

        return RedirectResponse(url=f"/side/{side_name}", status_code=status.HTTP_200_OK)


@router.post("/soup/{soup_name}/edit")
async def update_soup_recipe(request: Request, soup_name: str,
                             ingredient: str = Form(...),
                             spice: str = Form(...),
                             recipe: str = Form(...),
                             calorie: int = Form(...),
                             carbohydrate: int = Form(...),
                             protein: int = Form(...),
                             vitamin: int = Form(...)
                             ):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        _update = """
        UPDATE food
        INNER JOIN food_type ON food.food_type_id = food_type.id
        SET ingredient = %s, spice = %s, recipe = %s,
        calorie = %s, carbohydrate = %s, protein = %s, vitamin = %s
        WHERE name = %s and food_type = '반찬'
        """
        _new = (ingredient, spice, recipe,
                calorie, carbohydrate, protein, vitamin,
                soup_name)
        cursor.execute(_update, _new)
        db.commit()

        return RedirectResponse(url=f"/soup/{soup_name}", status_code=status.HTTP_200_OK)
