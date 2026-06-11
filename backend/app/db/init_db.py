from app.db.session import Base, engine

# IMPORTANT: registers models
from app.db import models  
from app.db.draft_models import EmailDraft


def init_db():
    Base.metadata.create_all(bind=engine)

