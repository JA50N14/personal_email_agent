from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.email_repository import EmailRepository
from app.services.draft_repository import DraftRepository
from app.services.draft_service import DraftService
from app.agents.draft_generator import DraftGenerator

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.post("/emails/{email_id}/generate-draft", response_class=HTMLResponse)
def generate_draft(
    request: Request,
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

    return templates.TemplateResponse(
        request=request,
        name="partials/draft_created.html",
        context={
            "draft": draft,
        },
    )

@router.get(
    "/drafts/{draft_id}",
    response_class=HTMLResponse,
)
def get_draft(
    request: Request,
    draft_id: int,
    db: Session = Depends(get_db),
):
    draft_repository = DraftRepository(db)

    draft = draft_repository.get_by_id(draft_id)

    if draft is None:
        raise HTTPException(
            status_code=404,
            detail="Draft not found",
        )

    return templates.TemplateResponse(
        request=request,
        name="draft_detail.html",
        context={
            "draft": draft,
        },
    )
