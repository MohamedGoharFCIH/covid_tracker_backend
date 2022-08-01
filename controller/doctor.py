from datetime import datetime
from app import app
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from models.doctor import Doctor
from werkzeug.security import check_password_hash

def login():
    # login code goes here
    if(request.method == 'POST'):
        email = request.form.get('email')
        password = request.form.get('password')

        doctor = Doctor.objects(email=email).first()
        if email == doctor['email'] and password == doctor['password']:
            
            session['doctor'] = str(doctor.id)
            print("session", session)
            return redirect('/admin')
    
    if "doctor" in session:
            return redirect('/admin')
    return render_template("login.html")
 

def logout():
    session.pop("doctor", None)
    return redirect('/adminlogin')
    

