# blueprints/public/__init__.py
from flask import Blueprint, render_template, request

public_bp = Blueprint("public_bp", __name__)

# ----- Public Home -----
@public_bp.get("/")
def home():
    return render_template("public/home.html")

@public_bp.get("/signin", endpoint="signin")
def signin():
    return "Sign-in page (coming soon)"

@public_bp.get("/signup", endpoint="signup")
def signup():
    return "Sign-up page (coming soon)"

@public_bp.get("/checkout", endpoint="checkout")
def checkout():
    plan = request.args.get("plan", "pro")
    return f"Checkout placeholder for plan: {plan}"


# Optional health check
@public_bp.get("/ping")
def ping():
    return "pong"
