from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from config.connection import db

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()


class Aluno(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ra = Column(Integer)
    name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))

    # Definindo características da classe.
    def __init__(self, ra: int, name: str, last_name: str, email: str, password: str):
        self.ra = ra
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password


# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
