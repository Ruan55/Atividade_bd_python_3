from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Parâmetros para conexão com o banco de dados.
db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

# Endereço/Caminho para conexão com banco de dados MySQL.
DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Conectando ao banco de dados.
db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()


# Gerenciando conexão com banco de dados.
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except Exception as error:
        db.rollback()
        raise error
    finally:
        db.close()
