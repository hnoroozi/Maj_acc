from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, logout_user

app_bp = Blueprint("app_bp", __name__, url_prefix="/app")

@app_bp.get("/dashboard")
@login_required
def dashboard():
    stats = {"mrr":18920,"invoices":{"paid":121,"pending":9,"overdue":4},"tax_q3":3412}
    return render_template("app/dashboard.html", stats=stats)

@app_bp.get("/logout")
def logout():
    logout_user()
    return redirect(url_for("public_bp.signin"))