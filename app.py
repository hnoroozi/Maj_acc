from flask import Flask, render_template
import os

from extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///majelani.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # init extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "public_bp.signin"

    from models import User

    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))

    # register blueprints
    from blueprints.public import public_bp
    from blueprints.app import app_bp
    app.register_blueprint(public_bp)
    app.register_blueprint(app_bp)

    @app.errorhandler(404)
    def not_found(e): return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(e): return render_template("errors/500.html"), 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)