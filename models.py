from fastapi import Form
from pydantic import BaseModel


class FoodType(BaseModel):
    id: int
    food_type: str


class Food(BaseModel):
    ingredient: str
    spice: str
    recipe: str
    calorie: int
    carbohydrate: int
    protein: int
    vitamin: int


class UsersSign(BaseModel):
    user_id: str
    password: str
    email: str


class UsersUnsign(BaseModel):
    user_id: int


class UserLogin(BaseModel):
    user_id: str
    password: str


class Community(BaseModel):
    title: str
    content: str


class Comment(BaseModel):
    text: str
