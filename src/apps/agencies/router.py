from fastapi import APIRouter

from apps.agencies.schemas import AgencyCreateRequest

router = APIRouter(prefix="/agencies", tags=["agancy"])


@router.get("/ping")
def get_agency():
    return {"agency": "is-ready"}


@router.post("/agencies")
def create_agency(payload: AgencyCreateRequest):
    return {"name": payload.name, "status": 200}
