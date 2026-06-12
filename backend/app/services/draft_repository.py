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
    
    def get_pending_draft_for_email(self, email_id):
        return (
            self.db.query(EmailDraft)
            .filter(
                EmailDraft.email_id == email_id,
                EmailDraft.status == "pending",
            )
            .first()
        )

    def get_drafts_for_email(self, email_id):
        return (
            self.db.query(EmailDraft)
            .filter(EmailDraft.email_id == email_id)
            .order_by(EmailDraft.created_at.desc())
            .all()
        )
    
    def get_by_id(self, draft_id: int):
        return (
            self.db.query(EmailDraft)
            .filter(EmailDraft.id == draft_id)
            .first()
        )