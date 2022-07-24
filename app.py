from operator import imod
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from models.user import User
from models.medicine import Medicine
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
DB = os.environ.get('DB')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))



app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': DB,
    'host': DB_HOST,
    'port': DB_PORT
}
app.config['SECRET_KEY'] = SECRET_KEY
db = MongoEngine()
db.init_app(app)



@app.route('/', methods=['GET'])
def start():
    return{
        "message" :"Server start running"
    }


from routes import users

if __name__ == "__main__":
    app.run(debug=True)