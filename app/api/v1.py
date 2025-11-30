from fastapi import APIRouter, HTTPException
from app.schemas import AskRequest, AskResponse
from app.services.iscool_service import IsCoolService

router = APIRouter(prefix="/v1")

service = IsCoolService()


@router.post("/ask", response_model=AskResponse)
async def ask(req: AskRequest):
    try:
        out = await service.answer(req.user_id, req.topic, req.explanation_level, req.detail_level)
        return AskResponse(reply=out["reply"], model=out["model"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
