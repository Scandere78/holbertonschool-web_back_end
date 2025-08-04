#!/usr/bin/env python3
"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance"""

        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self._session = None

    @property
    def session(self) -> Session:
        """Memoized session object"""
        if self._session is None:
            DBSession = sessionmaker(bind=self._engine)
            self._session = DBSession()
        return self._session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database and return the user object"""
        new_user = User(email=email, hashed_password=hashed_password)
        self.session.add(new_user)
        self.session.commit()
        return new_user
