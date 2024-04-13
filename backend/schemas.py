from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class UsersBase(BaseModel):
    data: str
    login: str
    password: str


class Users(UsersBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)


class UsersLogin(BaseModel):
    login: str
    password: str


class UsersCreate(UsersBase):
    pass


class UsersUpdate(BaseModel):
    id: int
    data: Optional[str]
    login: Optional[str]
    password: Optional[str]
    model_config = ConfigDict(from_attributes=True)


class ClientsBase(BaseModel):
    score_numbers: int
    responsible: str
    surname: str
    name: str
    patronymic: str
    inn: int
    status: str
    date_of_birth: datetime


class ClientsCreate(ClientsBase):
    pass


class Clients(ClientsBase):
    id: int
    users: Users
    created_at: datetime
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)


class ClientsUpdate(BaseModel):
    id: Optional[int]
    score_numbers: Optional[int]
    responsible: Optional[str]
    surname: Optional[str]
    name: Optional[str]
    patronymic: Optional[str]
    inn: Optional[int]
    status: Optional[str]
    date_of_birth: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)