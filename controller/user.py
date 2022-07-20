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


def login():
    try:
        record = json.loads(request.data)
        if not record:
            return {
                "message": "No user data ",
                "data": None,
                "error": "Bad request"
            }, 400
        fetched_user = User.objects(email=record['email']).first()
        if not fetched_user or not bcrypt.check_password_hash(fetched_user["password"], record["password"]):
            return jsonify({
                    "message": "Error fetching auth token!, invalid email or password",
                    "data": None,
                    "error": "Unauthorized",                 
                }), 404
        
        token = jwt.encode(
                        {"user_id":str(fetched_user.id), "email":fetched_user["email"], "name":fetched_user["name"]},
                        app.config["SECRET_KEY"],
                        algorithm="HS256")

        return {
                "message": " Successfully fetched auth token",
                "token": token,
                
                
            }, 200    
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500