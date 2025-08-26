# scripts/init_db.py

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app
from extensions import db
import models

app = create_app()
with app.app_context():
    db.create_all()
    print("✓ Database tables created.")

