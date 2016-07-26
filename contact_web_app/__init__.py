from flask import Flask


app = Flask(__name__)
from contact_web_app import views
