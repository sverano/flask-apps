from app import db
from app import User
db.create_all()
db.session.commit()