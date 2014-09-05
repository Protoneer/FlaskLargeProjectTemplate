from flask import Blueprint, render_template

mod_www = Blueprint('www', __name__, url_prefix = '/')

@mod_www.route('/', methods=['GET', 'POST'])
@mod_www.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('www/index.html')