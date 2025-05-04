from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from grocery_app.extensions import app
from grocery_app.models import User

# create login manager
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# create bcrypt
bcrypt = Bcrypt(app)

# import routes and register blueprints
from grocery_app.routes import main, auth
app.register_blueprint(main)
app.register_blueprint(auth) 
