from app import app
import json
from operator import imod
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from models.user import User
import jwt
bcrypt = Bcrypt(app)

def add_user():
    try:
        record = json.loads(request.data)
        if not record:
            return {
                "message": "No user data ",
                "data": None,
                "error": "Bad request"
            }, 400
        found_user = User.objects(email=record['email']).first()
        if(found_user):
            return jsonify(
                {
                "message": "User already exists",
                "error": "Conflict",
                "data": None
                }), 409
        pw_hash = bcrypt.generate_password_hash(record['password'])
        user = User(name=record['name'], email=record['email'], password=pw_hash)
        user.save()
        return  jsonify(
                {
                "message": "User created ",
                "data": user
                }), 201
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500


