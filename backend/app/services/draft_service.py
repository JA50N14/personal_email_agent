from app.agents.draft_generator import DraftGenerator
from app.services.email_repository import EmailRepository
from app.services.draft_repository import DraftRepository


class DraftService:

    def __init__(
        self,
        email_repository: EmailRepository,
        draft_repository: DraftRepository,
        draft_generator: DraftGenerator,
    ):
        self.email_repository = email_repository
        self.draft_repository = draft_repository
        self.draft_generator = draft_generator

    def generate_draft_for_email(
        self,
        email_id: int,
    ):
        email = self.email_repository.get_by_id(email_id)

        if email is None:
            raise ValueError(
                f"Email {email_id} not found"
            )
        
        existing_draft = (
            self.draft_repository.get_pending_draft_for_email(
                email.id
            )
        )

        if existing_draft:
            return existing_draft

        draft_body = self.draft_generator.generate(
            {
                "sender": email.sender,
                "subject": email.subject,
                "body": email.body,
            }
        )

        draft = self.draft_repository.create_draft(
            email_id=email.id,
            draft_body=draft_body,
        )

        return draft
    