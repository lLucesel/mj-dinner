from fastapi import APIRouter
from starlette import status
from starlette.responses import Response
import _ran

router = APIRouter

@router.get("/side")
async def side():
    # HTML 템플릿 파일 (templates/side.html)을 렌더링합니다.
    return templates.TemplateResponse("side.html", {"request": request})