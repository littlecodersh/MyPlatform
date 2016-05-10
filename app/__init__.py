try:
    from flask import Flask
    app = Flask(__name__)
    import views
    # init_menu()
    # from app.plugins.menu import init_menu
except:
    pass


