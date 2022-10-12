from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return {"message": "ok"}


@app.get("/items", response_model=List[schemas.Item])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@app.post("/items", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item)
