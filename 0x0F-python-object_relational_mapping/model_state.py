#!/usr/bin/python3
"""Define a State class mapping to the states table in the database."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of the declarative base
Base = declarative_base()


class State(Base):
    """Define a State class mapping to the states table in the database."""

    __tablename__ = 'states'  # Link to the MySQL table 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
