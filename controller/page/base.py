from fastapi import APIRouter

from controller.page import route_main

page_router = APIRouter()
page_router.include_router(route_main.router)
