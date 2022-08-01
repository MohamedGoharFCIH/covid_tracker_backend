from app import app
from controller import doctor 

@app.route("/adminlogin/", methods=["POST", "GET"])
def doctor_login():
    return doctor.login()


@app.route("/adminlogout/", methods=["GET"])
def doctor_logout():
    return doctor.logout()