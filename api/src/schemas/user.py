"""
User Schema
"""

from sqlalchemy import Column, Integer, String

from config.database import Base


class User(Base):
    """User Schemas"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True,nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)

    def __init__(self, name, cat, size, type, genere):
        self.name = name
        self.category = cat
        self.size = size
        self.type = type
        self.genere = genere
