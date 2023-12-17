from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Aqui é o caminho/path do banco de dados
engine = create_engine('sqlite:///database.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # Aqui: importação dos modelos para que sejam registrados no metadados do SQLAlchemy
    from models import Task # Substituir 'Task' pelo nome do modelo
    Base.metadata.create_all(bind=engine)