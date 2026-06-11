from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.email_repository import EmailRepository

EMAIL_FETCH_DAYS_LIMIT = 10

router = APIRouter()


@router.get("/emails")
def get_emails(
    db: Session = Depends(get_db),
):
    email_repository = EmailRepository(db)

    emails = email_repository.get_recent_emails(EMAIL_FETCH_DAYS_LIMIT)

    return [
        {
            "id": str(email.id),
            "sender": email.sender,
            "subject": email.subject,
            "received_at": email.received_at,
        }
        for email in emails
    ]
