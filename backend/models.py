from sqlalchemy import Column, Integer, Sequence, DateTime, String, ForeignKey, func
from sqlalchemy.orm import relationship

from database import Base


class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, Sequence("clients_id_seq", start=1), primary_key=True, index=True)
    score_numbers = Column(Integer, index=True)
    responsible = Column(String, ForeignKey('users.data'))
    surname = Column(String, index=True)
    name = Column(String, index=True)
    patronymic = Column(String, index=True)
    date_of_birth = Column(DateTime())
    inn = Column(Integer, index=True)
    status = Column(String, index=True, default='Не в работе')
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), server_default=None)

    users = relationship("Users", back_populates="clients")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence("users_id_seq", start=1), primary_key=True, index=True)
    data = Column(String, index=True) # ФИО
    login = Column(String, index=True)
    password = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), server_default=None)

    clients = relationship("Clients", back_populates="users")