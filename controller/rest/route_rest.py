from fastapi import APIRouter
from starlette.requests import Request

from models import Food

router = APIRouter()


@router.put("/side/{side_name}")
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
