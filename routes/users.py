
from app import app
from controller import user


@app.route("/signup/", methods=["POST"])
def add_user():
    return user.add_user()















