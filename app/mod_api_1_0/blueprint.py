from flask import Blueprint, render_template

mod_api = Blueprint('api', __name__, url_prefix = '/api_1_0')

@mod_api.route('/', methods=['GET', 'POST'])
@mod_api.route('/getdata', methods=['GET', 'POST'])
def getdata():
    return render_template('api_1_0/getdata.html')