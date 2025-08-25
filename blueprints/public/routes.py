# app.py یا blueprints/public/routes.py
from flask import render_template

@public_bp.get("/")
def home():
    return render_template("public/home.html")

@app.get("/signin")
def signin():
    return "Sign-in page (coming soon)"

@app.get("/signup")
def signup():
    return "Sign-up page (coming soon)"

@app.get("/checkout")
def checkout():
    plan = request.args.get("plan", "pro")
    return f"Checkout placeholder for plan: {plan}"

