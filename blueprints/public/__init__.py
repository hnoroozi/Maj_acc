from flask import Blueprint, render_template, request

public_bp = Blueprint("public_bp", __name__)

@public_bp.get("/")
def home():
    return render_template("public/home.html")

# --- Auth pages ---
@public_bp.get("/signin")
def signin():
    return render_template("auth/signin.html")

@public_bp.get("/signup")
def signup():
    return render_template("auth/signup.html")

@public_bp.post("/signup")
def signup_post():
    # TODO: handle form later
    return "Signed up (mock)!"

@public_bp.post("/signin")
def signin_post():
    # TODO: handle login later
    return "Signed in (mock)!"

@public_bp.get("/checkout")
def checkout():
    plan = request.args.get("plan", "pro")
    return f"Checkout placeholder for plan: {plan}"
