from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from ..oauth2 import get_current_user
from typing import List
from ..database import Base, engine, connect_db
from .. import models
from .. import schemas


# Route API - import APIRouter
router = APIRouter(
    prefix="/owner", 
    tags=['Owner']
)


# With List [] - Response Model will Fail
@router.get('/', response_model=List[schemas.OwnerReturn])
def get_all_owners(db : Session = Depends(connect_db)):
    results = db.query(models.DB).all()
    #print(results)
    return results


@router.get('/{name}', response_model=List[schemas.OwnerReturn])
def get_owner_id(name: str, db : Session = Depends(connect_db)):
    # Remember to use Filter when retriving under condition
    owner_details = db.query(models.DB).filter(models.DB.name == name).all()
    return owner_details


# List [] is not needed in Response Model - find out why ?
@router.post('/', response_model=schemas.OwnerBase)
def insert_new_owner(inbound_details: schemas.NewOwner, db: Session = Depends(connect_db), user_id: int = Depends(get_current_user)):
    # Remember Before Adding New Data into DB, Make the Data as Dict
    new_details_insert = models.DB(**inbound_details.dict())
    
    db.add(new_details_insert)
    db.commit() # must commit the records
    db.refresh(new_details_insert)
    return new_details_insert


# If ID column is used, then working fine. But with Name column - issue occurs  - May be primary key ?
@router.put('/{id}', response_model=schemas.OwnerReturn)
def update_owner(id: int,update_inbound : schemas.UpdateOwner, db : Session = Depends(connect_db)):
    db_data = db.query(models.DB).filter(models.DB.id == id)
    val = db_data.first()
    # Remember to convert data into Dict & Synchronize the Session 
    db_data.update(update_inbound.dict(), synchronize_session=False)
    db.commit()
    #db.refresh(db_data)
    return db_data.first()


@router.delete('/{id}')
def delete_owner(id: int, db: Session = Depends(connect_db)):
    to_be_deleted = db.query(models.DB).filter(models.DB.id == id)
    to_be_deleted.delete(synchronize_session=False)
    db.commit()
    return f"Data has been Deleted for {id}"

