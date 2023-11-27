from fastapi import APIRouter, Request, Form, Depends, HTTPException
# from controllers.user import create_user, delete_user
# from controllers.auth import create_access_token
from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from passlib.context import CryptContext
from datetime import timedelta
from mysqlclient_pool import ConnectionPool
from starlette import status
from starlette.responses import HTMLResponse
from MySQLdb.cursors import DictCursor
from fastapi.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from routers.detail import FoodDetail
from db.db_conn import db


router = APIRouter()
templates = Jinja2Templates(directory="templates")

SECRET_KEY = "your-secret-key"
SESSION_TIMEOUT_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_from_session(request: Request):
    return request.session.get("user")


def get_current_user(request: Request = Depends(get_user_from_session)):
    return request.session.get("user")


def get_db_pool(request: Request):
    return request.app.state.pool


def is_authenticated(request: Request = Depends(get_user_from_session)):
    if request.session.get("user"):
        return True
    return False


# 회원 가입
@router.post("/register", response_class=HTMLResponse)
async def register(
        request: Request,
        username: str = Form(...),
        password: str = Form(...),
        db: ConnectionPool = Depends(get_db_pool),
):
    hashed_password = pwd_context.hash(password)

    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        query = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
        cursor.execute(query, (username, hashed_password))
        db.commit()

    return RedirectResponse(url="/login", status_code=303)


# 로그인
@router.post("/login", response_class=HTMLResponse)
async def login(
        request: Request,
        username: str = Form(...),
        password: str = Form(...),
        db: ConnectionPool = Depends(get_db_pool),
):
    with request.app.state.pool.fetch(cursor_type=DictCursor) as cursor:
        query = "SELECT password_hash FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

    if user and pwd_context.verify(password, user["password_hash"]):
        request.session["user"] = username
        return RedirectResponse(url="/main", status_code=303)

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지 않은 자격 증명")


# 로그아웃
@router.post("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/main", status_code=303)
