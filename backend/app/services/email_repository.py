from sqlalchemy.orm import Session
from app.db.models import Email


class EmailRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_provider_message_id(self, provider_message_id: str):
        return (
            self.db.query(Email)
            .filter(Email.provider_message_id == provider_message_id)
            .first()
        )

    def create_email(self, provider_message_id: str, sender: str, subject: str, body: str):
        email = Email(
            provider_message_id=provider_message_id,
            sender=sender,
            subject=subject,
            body=body
        )

        self.db.add(email)
        self.db.commit()
        self.db.refresh(email)

        return email
    
    def get_by_id(self, email_id: int):
        return (
            self.db.query(Email)
            .filter(Email.id == email_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Email).all()
    
    