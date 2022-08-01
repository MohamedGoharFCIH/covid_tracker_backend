from app import app
from controller import user
from middlewares.auth_middleware import token_required

@app.route("/signup/", methods=["POST"])
def add_user():
    return user.add_user()


@app.route("/login/", methods=["POST"])
def login():
    return user.login()

@app.route("/users/", methods=["GET"])
@token_required
def getUsers(current_user):
    return user.getUsers(current_user)



@app.route("/user/", methods=["GET"])
@token_required
def get_current_user(current_user):
    return user.get_current_user(current_user)



















