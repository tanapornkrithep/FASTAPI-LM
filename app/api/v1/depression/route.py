from fastapi import APIRouter
from .service import get_depression
from .scema import DepressionRequest,DepressionUpdate

router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return get_depression()


@router.get('/info', tags=['Depression'])
def info():
    return {"service": "Depression Assessment API", "version": "1.0"}


@router.delete('/depression', tags=['Depression'])
def delete_depression_record(record_id: int):
    return {"status": "deleted", "record_id": record_id}

@router.put('/depression', tags=['Depression'])
def update_depression_record(record_id: int, data: DepressionUpdate):
    return {"status": "updated", "record_id": record_id, "data": data}

@router.patch('/depression', tags=['Depression'])
def partial_update_depression_record(record_id: int, data: dict):
    return {"status": "partially updated", "record_id": record_id, "data": data}