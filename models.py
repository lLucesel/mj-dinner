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


class Todo(BaseModel):
    content: str
