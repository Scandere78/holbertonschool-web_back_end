#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt


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
