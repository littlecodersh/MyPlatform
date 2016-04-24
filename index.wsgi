from client import app
import sae

#app.debug = True
application = sae.create_wsgi_app(app)
