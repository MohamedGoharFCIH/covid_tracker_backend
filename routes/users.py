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


@app.route("/patients/", methods=["GET"])
@token_required
def getPatients(current_user):
    return user.getpatients(current_user)


@app.route("/user/", methods=["GET"])
@token_required
def get_current_user(current_user):
    return user.get_current_user(current_user)

@app.route("/user/", methods=["PUT"])
@token_required
def update_current_user(current_user):
    return user.update_user(current_user, str(current_user.id))

@app.route("/medicines/", methods=["GET"])
@token_required
def getMedicines(current_user):
    return user.getMedicines(current_user)


















