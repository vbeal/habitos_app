from config import engine, Base
from models import Habito

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
