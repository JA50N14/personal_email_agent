from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response

from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.email_repository import EmailRepository

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/inbox", response_class=HTMLResponse)
def inbox(request: Request, db: Session = Depends(get_db)):
    email_repository = EmailRepository(db)

    emails = email_repository.get_recent_emails(10)

    return templates.TemplateResponse(
        request=request,
        name="inbox.html",
        context={
            "emails": emails,
        },
    )

@router.post("/emails/{email_id}/skip")
def skip_email(email_id: str, db: Session = Depends(get_db)):
    repo = EmailRepository(db)

    repo.update_workflow_status(email_id, "skipped")

    # remove element from DOM
    return HTMLResponse("")