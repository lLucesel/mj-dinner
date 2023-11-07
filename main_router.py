from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from routers import lotto_router


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(lotto_router.router)


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


# href 안에 넣을것 {{ url_for('side') }}
# href 안에 넣을것 {{ url_for('soup') }}
# href 안에 넣을것 {{ url_for('diet') }}
# href 안에 넣을것 {{ url_for('register') }}
