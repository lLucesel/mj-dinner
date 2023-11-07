from pydantic import BaseModel


class FoodType(BaseModel):
    #  def __init__(self, **data: Any):
    #      super().__init__(**data)

    id: int
    food_type: str


class Food(BaseModel):
    #def __init__(self, **data: Any):
    #    super().__init__(**data)

    food_type_id: int
    name: str
    ingredient: str
    spice: str
    recipe: str
    calorie: int
    carbohydrate: int
    protein: int
    vitamin: int
