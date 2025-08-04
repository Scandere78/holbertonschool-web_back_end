#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """Home route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "email and password required"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/session", methods=["POST"])
def login():
    """
    Handle user login.
    - Expects 'email' and 'password' in form data.
    - If invalid credentials: abort(401)
    - If valid: create a session, set session_id cookie, return JSON.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None:
        abort(401)

    # Vérifier identifiants
    if not AUTH.valid_login(email, password):
        abort(401)

    # Créer une session
    session_id = AUTH.create_session(email)
    if session_id is None:
        abort(401)

    # Construire la réponse JSON
    resp = make_response(jsonify({"email": email, "message": "logged in"}))
    resp.set_cookie("session_id", session_id, path="/")

    return resp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
