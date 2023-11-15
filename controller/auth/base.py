from fastapi import APIRouter
from controller.auth import route_auth

auth_router = APIRouter()
auth_router.include_router(route_auth.router)
