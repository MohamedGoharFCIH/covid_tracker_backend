
from app import app
from controller import user


@app.route("/signup/", methods=["POST"])
def add_user():
    return user.add_user()


@app.route("/login/", methods=["POST"])
def login():
    return user.login()

@app.route("/users/", methods=["GET"])
def getUsers():
    return user.getUsers()






















