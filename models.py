from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config import Base
from datetime import datetime, timezone

class Habito(Base):
    __tablename__ = 'habitos'

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    concluido = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    data_conclusao = Column(DateTime, nullable=True)
