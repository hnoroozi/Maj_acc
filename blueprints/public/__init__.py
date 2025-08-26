from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user
from app import db
from models import User
from extensions import db

public_bp = Blueprint("public_bp", __name__)

@public_bp.get("/")
def home():
    return render_template("public/home.html")

@public_bp.get("/signin")
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("app_bp.dashboard"))
    return render_template("auth/signin.html")

@public_bp.post("/signin")
def signin_post():
    email = request.form.get("email","").strip().lower()
    password = request.form.get("password","")
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        flash("Invalid email or password.", "error")
        return redirect(url_for("public_bp.signin"))
    login_user(user, remember=True)
    return redirect(url_for("app_bp.dashboard"))

@public_bp.get("/signup")
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("app_bp.dashboard"))
    return render_template("auth/signup.html")

@public_bp.post("/signup")
def signup_post():
    name = request.form.get("name","").strip()
    email = request.form.get("email","").strip().lower()
    password = request.form.get("password","")
    if not name or not email or not password:
        flash("Please fill out all fields.", "error")
        return redirect(url_for("public_bp.signup"))
    if User.query.filter_by(email=email).first():
        flash("Email is already registered.", "error")
        return redirect(url_for("public_bp.signup"))
    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user); db.session.commit()
    login_user(user, remember=True)
    flash("Account created. Welcome!", "success")
    return redirect(url_for("app_bp.dashboard"))

@public_bp.get("/checkout", endpoint="checkout")
def checkout():
    plan = request.args.get("plan", "pro")
    return f"Checkout placeholder for plan: {plan}"
