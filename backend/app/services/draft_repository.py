from sqlalchemy.orm import Session

from app.db.draft_models import EmailDraft


class DraftRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_draft(
        self,
        email_id: int,
        draft_body: str,
        status: str = "pending"
    ):
        draft = EmailDraft(
            email_id=email_id,
            draft_body=draft_body,
            status=status
        )

        self.db.add(draft)
        self.db.commit()
        self.db.refresh(draft)

        return draft