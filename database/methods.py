from sqlalchemy.orm import Session
from models.mbase import Users


def get_user_token(db: Session, token: str):
    return db.query(Users).filter(Users.token == token).first()


def update_token(db: Session, token: str, data: dict):
    db_token = db.query(Users).filter(Users.token == token).first()
    for key, value in data.items():
        setattr(db_token, key, value)
    db.commit()
    db.refresh(db_token)
    return db_token
