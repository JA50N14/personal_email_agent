from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
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