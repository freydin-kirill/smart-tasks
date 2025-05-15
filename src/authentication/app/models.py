from sqlalchemy import MetaData, Integer, String, Table, Column, Boolean

from common.database import Base

# Special variable
metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("full_name", String, nullable=True),
    Column("hashed_password", String, nullable=False),
    Column("disabled", Boolean, nullable=False),
)

# DB Models for SQLAlchemy
class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False, nullable=False)
