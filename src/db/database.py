from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String, )
from sqlalchemy.ext.declarative import declarative_base

from src.db.utils import CustomBaseModel

Base = declarative_base(cls=CustomBaseModel)


class Users(Base):
    __tablename__ = "user_info"

    user_id = Column(
        Integer,
        primary_key=True,
        unique=True,
    )
    email_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    logout = Column(Boolean, nullable=False)


class TaskInformation(Base):
    __tablename__ = "task_information"

    task_id = Column(
        Integer,
        primary_key=True,
        unique=True,
    )
    task_name = Column(String, nullable=False)
    deadline = Column(DateTime, nullable=True)
    description = Column(String, nullable=True)
    user_id = Column(
        Integer,
        ForeignKey("user_info.user_id"),
        nullable=False,
    )
    complete_status = Column(Boolean, nullable=False)
