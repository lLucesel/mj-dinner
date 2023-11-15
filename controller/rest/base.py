from fastapi import APIRouter
from controller.rest import route_rest

rest_router = APIRouter()
rest_router.include_router(route_rest.router)
