from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from contextlib import asynccontextmanager

from app.api.draft_routes import router as draft_router
from app.api.email_routes import router as email_router
from app.api.ui_routes import router as ui_router
from app.db.init_db import init_db
from app.db.session import get_db
from app.services.email_repository import EmailRepository
from app.email_providers.gmail_provider import GmailProvider
from app.services.email_sync_service import EmailSyncService

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(draft_router)
app.include_router(email_router)
app.include_router(ui_router)

@app.get("/")
def root():
    return {"message": "Email Agent API"}

@app.get("/health/db")
def database_health_check(db: Session = Depends(get_db)):
    return {"status": "database dependency working"}

@app.get("/health/postgres")
def postgres_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "postgres connected"
    }

@app.post("/test/email")
def create_test_email(db: Session = Depends(get_db)):
    email_repo = EmailRepository(db)

    email = email_repo.create_email(
        provider_message_id="test-message-1",
        sender="bob@example.com",
        subject="Test Subject",
        body="Test Body"
    )

    return {
        "id": str(email.id),
        "sender": email.sender,
        "subject": email.subject
    }

@app.post("/sync")
def sync_emails(db: Session = Depends(get_db)):
    email_repository = EmailRepository(db)

    email_provider = GmailProvider()

    sync_service = EmailSyncService(
        email_provider=email_provider,
        email_repository=email_repository
    )

    sync_service.sync_emails()

    return {
        "status": "sync completed"
    }






# def main():
#     print("Hello from backend!")


# if __name__ == "__main__":
#     main()
