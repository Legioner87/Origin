from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from homework_19 import config


engine = create_engine(
    config.SQLA_CONNECT_URL,
    echo=config.SQLA_ECHO
)

Base = declarative_base(bind=engine)