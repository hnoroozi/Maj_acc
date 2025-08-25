# blueprints/app/__init__.py
from flask import Blueprint, render_template, redirect, url_for, request

app_bp = Blueprint("app_bp", __name__, url_prefix="/app")

def is_authenticated():

    return True

@app_bp.before_request
def _guard():

    if request.endpoint in ("app_bp.logout",):
        return
    if not is_authenticated():
        return redirect(url_for("public_bp.signin"))

# --- Dashboard ---
@app_bp.get("/dashboard")
def dashboard():

    stats = {
        "mrr": 18920,
        "invoices": {"paid": 121, "pending": 9, "overdue": 4},
        "tax_q3": 3412,
    }
    return render_template("app/dashboard.html", stats=stats)

@app_bp.get("/logout")
def logout():
    return redirect(url_for("public_bp.signin"))
