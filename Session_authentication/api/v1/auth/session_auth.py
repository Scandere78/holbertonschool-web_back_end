#!/usr/bin/env python3
""" Module session_auth """
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session authentication class - inherits from Auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a given user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Retourne l'utilisateur courant à partir du cookie de session"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Supprime la session (déconnexion de l'utilisateur)"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        if session_id not in self.user_id_by_session_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
