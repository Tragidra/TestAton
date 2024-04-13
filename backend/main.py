import sqlite3
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import schemas, models
from database import engine, SessionLocal
from models import Clients, Users

app = FastAPI()
origins = ["http://localhost:8000", "http://127.0.0.1:8000"]
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    # file = "app.db"
    # try:
    #     conn = sqlite3.connect(file)
    #     res = "Database Sqlite3.db formed."
    # except:
    #     res = "Database Sqlite3.db not formed."
    # return {"message": res}
    return {'1': 1}


# @app.get("/clients/", response_model=list[schemas.Clients])
# async def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     anime_outsides = db.query(Clients).offset(skip).limit(limit).all()
#     return anime_outsides


@app.get("/clients/{user_data}", response_model=schemas.Clients)
async def read_clients_by_filter(user_data: str, db: Session = Depends(get_db)):
    clients = db.query(Clients).filter(Clients.responsible == user_data).all()
    if clients is None:
        raise HTTPException(status_code=404, detail="Клиенты не найдены")
    return clients


@app.post("/clients/update/", response_model=schemas.ClientsUpdate)
async def update_clients(clients: schemas.ClientsUpdate, db: Session = Depends(get_db)):
    # get the existing data
    db_clients = db.query(Clients).filter(Clients.id == clients.id).one_or_none()
    if db_clients is None:
        raise HTTPException(status_code=404, detail="Клиент не найден")

    # Update model class variable from requested fields
    for var, value in vars(clients).items():
        setattr(db_clients, var, value) if value or str(value) == 'False' else None

    db.add(db_clients)
    db.commit()
    db.refresh(db_clients)
    return db_clients


@app.post("/clients/create", response_model=schemas.ClientsCreate)
async def create_clients(clients: schemas.ClientsCreate, db: Session = Depends(get_db)):
    db_clients = Clients(score_numbers=clients.score_numbers, responsible=clients.responsible,
                         surname=clients.surname, name=clients.name, date_of_birth=clients.date_of_birth,
                         patronymic=clients.patronymic, inn=clients.inn, status=clients.status
                         )
    db.add(db_clients)
    db.commit()
    db.refresh(db_clients)
    return db_clients


@app.post("/users/create", response_model=schemas.UsersCreate)
async def create_users(users: schemas.UsersCreate, db: Session = Depends(get_db)):
    db_users = Users(data=users.data, login=users.login, password=users.password)
    db.add(db_users)
    db.commit()
    db.refresh(db_users)
    return db_users


@app.post("/user/login")
async def login_user(user: schemas.UsersLogin, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.login == user.login and Users.password == user.password).one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    else:
        print(db_user)
        db_user = db.query(Clients).filter(Clients.responsible == db_user.data).all()
        print(db_user)
    return db_user
