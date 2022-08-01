from flask import Flask, request, jsonify, session, redirect
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.mongoengine import ModelView
from flask_mongoengine import MongoEngine
import os
import datetime
from dotenv import load_dotenv
from flask_admin.menu import MenuLink
from flask_cors import CORS

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
DB = os.environ.get('DB')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = int(os.environ.get('DB_PORT'))





app = Flask(__name__)
CORS(app)

app.config['MONGODB_SETTINGS'] = {
    'db': DB,
    'host': DB_HOST,
    'port': DB_PORT
}
app.config['SECRET_KEY'] = SECRET_KEY
db = MongoEngine()
db.init_app(app)


from models.medicine import Medicine 
from models.user import User
from models.doctor import Doctor

@app.route('/', methods=['GET'])
def start():
    return{
        "message" :"Server start running",
    }


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        print("from redirect", session)
        if "doctor" in session:
            return True
    
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect('/adminlogin')


class UserView(ModelView):

    # def _list_name(self, context, model, name):
    #     medicines_list = []
    #     for m in model.medicines:
    #         medicines_list.append(m.name)
    #     return medicines_list

    column_filters = ['name']
    column_exclude_list = ['password', ]
    column_searchable_list = ('name', 'email')
    # column_formatters = {
    #     'medicines': _list_name
    # }


    form_ajax_refs = {
        'medicines': {
            'fields': ('name',)
        }
    }

class DoctorView(ModelView):
    column_filters = ['name']
    column_searchable_list = ('name', 'email')
    column_exclude_list = ['password']



 
admin = Admin(app, index_view=MyAdminIndexView())

# Add views
admin.add_view(UserView(User))
admin.add_view(ModelView(Medicine))
admin.add_view(DoctorView(Doctor))
admin.add_link(MenuLink(name='logout', category='', url='/adminlogout'))



from routes import users
from routes import doctors
if __name__ == "__main__":

    app.run(debug=True)

    
