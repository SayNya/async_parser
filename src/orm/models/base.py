from sqlalchemy import (
    Column,
    Integer,
    DateTime,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class BaseIDModel(Base):
    __abstract__ = True
    __table_args__ = ()

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
