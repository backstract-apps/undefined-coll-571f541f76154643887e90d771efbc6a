from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/persons/')
async def get_persons(db: Session = Depends(get_db)):
    return await service.get_persons(db)

@router.get('/persons/rollnumber')
async def get_persons_rollnumber( rollnumber: int , db: Session = Depends(get_db)):
    return await service.get_persons_rollnumber(db , rollnumber)

@router.post('/persons/')
async def post_persons( rollnumber: str, fullname: str, age: str, profession: str , db: Session = Depends(get_db)):
    return await service.post_persons(db , rollnumber, fullname, age, profession)

@router.put('/persons/rollnumber/')
async def put_persons_rollnumber( rollnumber: str, fullname: str, age: str, profession: str , db: Session = Depends(get_db)):
    return await service.put_persons_rollnumber(db , rollnumber, fullname, age, profession)

@router.delete('/persons/rollnumber')
async def delete_persons_rollnumber( rollnumber: int , db: Session = Depends(get_db)):
    return await service.delete_persons_rollnumber(db , rollnumber)

@router.get('/addresses/')
async def get_addresses(db: Session = Depends(get_db)):
    return await service.get_addresses(db)

@router.get('/addresses/id')
async def get_addresses_id( id: int , db: Session = Depends(get_db)):
    return await service.get_addresses_id(db , id)

@router.post('/addresses/')
async def post_addresses( id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str , db: Session = Depends(get_db)):
    return await service.post_addresses(db , id, street, city, state, country, postal_code, created_at, updated_at)

@router.put('/addresses/id/')
async def put_addresses_id( id: str, street: str, city: str, state: str, country: str, postal_code: str, created_at: str, updated_at: str , db: Session = Depends(get_db)):
    return await service.put_addresses_id(db , id, street, city, state, country, postal_code, created_at, updated_at)

@router.delete('/addresses/id')
async def delete_addresses_id( id: int , db: Session = Depends(get_db)):
    return await service.delete_addresses_id(db , id)

@router.post('/testchintupana')
async def post_testchintupana( isWork: int, dev_name: str , db: Session = Depends(get_db)):
    return await service.post_testchintupana(db , isWork, dev_name)

@router.post('/returnsum')
async def post_returnsum( isWorking: int, dev_name: str , db: Session = Depends(get_db)):
    return await service.post_returnsum(db , isWorking, dev_name)

