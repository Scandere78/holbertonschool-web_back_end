#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a salt.

    Args:
        password (str): Plain text password.

    Returns:
        bytes: Salted hash of the password.
    """
    # bcrypt.hashpw attend des bytes, donc on encode le mot de passe en UTF-8
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.
        Raises ValueError if user already exists.
        """
        try:
            # Vérifier si un utilisateur existe déjà
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # Hachage du mot de passe
            hashed_pwd = _hash_password(password)
            # Ajouter l'utilisateur à la base
            return self._db.add_user(email, hashed_pwd.decode("utf-8"))

    def valid_login(self, email: str, password: str) -> bool:
        """Check if email exists and password matches"""
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password.encode('utf-8'))
        except NoResultFound:
            return False


def _generate_uuid() -> str:
    """
    Generate a new UUID and return it as a string.
    Private function: should not be used outside auth.py
    """
    return str(uuid.uuid4())
