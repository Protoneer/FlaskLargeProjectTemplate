from flask import Flask, render_template

app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Simple HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.mod_api.blueprint import mod_api as api_module
from app.mod_www.blueprint import mod_www as www_module

# Register blueprint(s)
app.register_blueprint(api_module)
app.register_blueprint(www_module)
