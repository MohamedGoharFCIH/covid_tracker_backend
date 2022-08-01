from datetime import datetime
from app import app
import json
from operator import imod
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from models.user import User
from models.medicine import Medicine
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
            {
            "user_id":str(fetched_user.id),
            "email":fetched_user["email"],
            "name":fetched_user["name"]
            },

            app.config["SECRET_KEY"],
            algorithm="HS256")
        return {"message": " Successfully fetched auth token","user": fetched_user, "token":token}, 200    
    
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500


def getUsers(current_user):
   
    users =  User.objects()
    try:
        return {
            "users": users,
            "count": len(users),
            "message":" users data fetched successfully"
        },200
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500

def update_user(current_user, id):
    try:
        record = json.loads(request.data)
        if not record:
                return {
                    "message": "No user data ",
                    "data": None,
                    "error": "Bad request"
                }, 400    
        old_user = User.objects(id=str(id)).first()
        if not old_user :
            return {
                        "message": "Error fetching user not found",
                        "data": None,
                        "error": "not found",                 
                    }, 404
        old_user.update(**record)
        return {
            "message":"User updated "
        }, 200
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500


def getMedicines(current_user):
    try:

        print(current_user.medicines)
        return {
            "data":current_user.medicines
        }
    except Exception as e :
        return {"message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500


def getpatients(current_user):
    patients = User.objects(temperature__gte=38)
    try:
        return {
            "users": patients,
            "count": len(patients),
            "message":" users data fetched successfully"
        },200
    except Exception as e:
        return {
            "message": "Something went wrong",
            "error": str(e),
            "data": None
        }, 500

def get_current_user(current_user):
    return jsonify({
        "message": "successfully retrieved user profile",
        "data": current_user
    })



