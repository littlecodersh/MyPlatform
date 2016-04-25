import sae

# site-packages
sae.add_vendor_dir('vendor')

from app import app

# app.debug = True
application = sae.create_wsgi_app(app)
