import datetime
from sqlalchemy import event
from database.db import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
import secrets


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(500))
    usage = Column(Integer, default=3)
    added_at = Column(DateTime, default=datetime.datetime.now)
    token = Column(String(50000))


@event.listens_for(Users, 'before_insert')
def generate_token(mapper, connection, target):
    target.token = target.username + secrets.token_urlsafe(64)
