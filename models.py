from fastapi import Form
from pydantic import BaseModel


class FoodType(BaseModel):
    food_type: str


class Food(BaseModel):
    ingredient: str
    spice: str
    recipe: str
    calorie: int
    carbohydrate: int
    protein: int
    vitamin: int


class FoodAdd(BaseModel):
    food_type_id: str
    name: str
    ingredient: str
    spice: str
    recipe: str
    calorie: int
    carbohydrate: int
    protein: int
    vitamin: int


class Todo(BaseModel):
    content: str

    @classmethod
    def as_form(cls, content: str = Form(...)):
        return cls(content=content)
