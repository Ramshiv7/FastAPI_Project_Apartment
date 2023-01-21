from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from .database import Base, engine, connect_db
from . import models
from . import schemas

# Engine Binds all to Create DB based on Model using Engine - Models.Base.metadata.create_all(bind=<engine_name>)
models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# With List [] - Response Model will Fail
@app.get('/owner', response_model=List[schemas.OwnerReturn])
def get_all_owners(db : Session = Depends(connect_db)):
    results = db.query(models.DB).all()
    #print(results)
    return results


@app.get('/owner/{name}', response_model=List[schemas.OwnerReturn])
def get_owner_id(name: str, db : Session = Depends(connect_db)):
    # Remember to use Filter when retriving under condition
    owner_details = db.query(models.DB).filter(models.DB.name == name).all()
    return owner_details


# List [] is not needed in Response Model - find out why ?
@app.post('/owner', response_model=schemas.OwnerBase)
def insert_new_owner(inbound_details: schemas.NewOwner, db: Session = Depends(connect_db)):
    # Remember Before Adding New Data into DB, Make the Data as Dict
    new_details_insert = models.DB(**inbound_details.dict())
    db.add(new_details_insert)
    db.commit() # must commit the records
    db.refresh(new_details_insert)
    return new_details_insert


# If ID column is used, then working fine. But with Name column - issue occurs  - May be primary key ?
@app.put('/owner/{id}', response_model=schemas.OwnerReturn)
def update_owner(id: int,update_inbound : schemas.UpdateOwner, db : Session = Depends(connect_db)):
    db_data = db.query(models.DB).filter(models.DB.id == id)
    val = db_data.first()
    # Remember to convert data into Dict & Synchronize the Session 
    db_data.update(update_inbound.dict(), synchronize_session=False)
    db.commit()
    #db.refresh(db_data)
    return db_data.first()



@app.post('/login', response_model=schemas.LoginReturn)
def login_details(details: schemas.OwnerLogin, db: Session = Depends(connect_db)):
    new_data = models.Login(**details.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data