#!/usr/bin/env python3
""" Authentication module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to handle authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Return the value of the Authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user (None for now)"""
        return None
