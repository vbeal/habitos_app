from sqlalchemy.orm import Session
from models import Habito
from config import SessionLocal
from datetime import datetime, timezone

db: Session = SessionLocal()

def delete_habito(titulo):
    habito = db.query(Habito).filter(Habito.titulo == titulo).first()
    if habito:
        db.delete(habito)
        db.commit()

def update_habito_status(titulo, concluido):
    habito = db.query(Habito).filter(Habito.titulo == titulo).first()
    if habito:
        habito.concluido = concluido
        if concluido:
            habito.data_conclusao = datetime.now(timezone.utc)
        else:
            habito.data_conclusao = None
        db.commit()

def add_habito(titulo):
    new_habito = Habito(titulo=titulo)
    db.add(new_habito)
    db.commit()

def update_habito(old_title, new_title):
    habito = db.query(Habito).filter(Habito.titulo == old_title).first()
    if habito:
        habito.titulo = new_title
        db.commit()
