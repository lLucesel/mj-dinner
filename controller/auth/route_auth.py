import models
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from controllers.user import create_user, delete_user
from controllers.auth import create_access_token
from .database import get_db
from starlette.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

