import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env #noqa no quality assurance, put when error is not necessarily correct

app = Flask(__name__)
app.config["SECRET_KEY"]=os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///taskmanager.db" # os.environ.get("DB_URL")      
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False                          
db = SQLAlchemy(app)







from taskmanager import routes 