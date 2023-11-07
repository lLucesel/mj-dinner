import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from mysqlclient_pool import ConnectionPool

from controller.page.base import page_router
from controller.rest.base import rest_router

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(page_router)
app.include_router(rest_router)


@app.on_event("startup")
def create_pool() -> None:
    app.state.pool = ConnectionPool(
        {
            "unix_socket": "/var/run/mysqld/mysqld.sock",
            "host": "mj.caletbhkxfd6.ap-northeast-2.rds.amazonaws.com",
            "port": 3306,
            "user": "admin_mj",
            "password": "77gundam77",
            "database": "dinner"
        },
        size=20,  # minimum size of the connections
        fillup=False  # create an empty pool initially
    )


@app.on_event("shutdown")
def cleanup() -> None:
    app.state.pool.close()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
