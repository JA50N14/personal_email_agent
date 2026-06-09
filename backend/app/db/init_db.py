from app.db.session import Base, engine
from app.db import models  # IMPORTANT: registers models


def init_db():
    Base.metadata.create_all(bind=engine)

