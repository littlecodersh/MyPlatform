from flask import Flask

app = Flask(__name__)

import views

from app.plugins.menu import init_menu
init_menu()
