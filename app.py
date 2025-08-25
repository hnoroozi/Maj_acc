from flask import Flask
from blueprints.public import public_bp
from blueprints.app import app_bp

app = Flask(__name__)
app.register_blueprint(public_bp)
app.register_blueprint(app_bp)

if __name__ == "__main__":
    app.run(debug=True)

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("errors/500.html"), 500
