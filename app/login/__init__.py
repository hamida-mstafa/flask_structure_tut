from flask import Blueprint
login_blueprint = Blueprint(
    'login',
    __name__,
    template_folder='templates/login'
    )