from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.email_repository import EmailRepository
from app.services.draft_repository import DraftRepository
from app.services.draft_service import DraftService
from app.agents.draft_generator import DraftGenerator

router = APIRouter()


@router.post("/emails/{email_id}/generate-draft")
def generate_draft(
    email_id: UUID,
    db: Session = Depends(get_db),
):
    email_repository = EmailRepository(db)
    draft_repository = DraftRepository(db)
    draft_generator = DraftGenerator()

    draft_service = DraftService(
        email_repository=email_repository,
        draft_repository=draft_repository,
        draft_generator=draft_generator,
    )

    draft = draft_service.generate_draft_for_email(
        email_id=email_id
    )

    return {
        "draft_id": str(draft.id),
        "email_id": str(draft.email_id),
        "status": draft.status,
    }
