# app.py
from flask import Flask
from blueprints.public import public_bp

app = Flask(__name__)
app.register_blueprint(public_bp)

if __name__ == "__main__":
    app.run(debug=True)
