from dotenv import load_dotenv

load_dotenv()

from app.db.session import SessionLocal
from app.services.email_repository import EmailRepository
from app.services.draft_repository import DraftRepository
from app.services.draft_service import DraftService
from app.agents.draft_generator import DraftGenerator


def main():
    db = SessionLocal()

    try:
        email_repository = EmailRepository(db)
        draft_repository = DraftRepository(db)
        draft_generator = DraftGenerator()

        draft_service = DraftService(
            email_repository=email_repository,
            draft_repository=draft_repository,
            draft_generator=draft_generator,
        )

        emails = email_repository.get_all()

        if not emails:
            print("No emails found in database.")
            return

        email = emails[0]

        print(f"Generating draft for email {email.id}")
        print(f"Subject: {email.subject}")
        print()

        draft = draft_service.generate_draft_for_email(
            email.id
        )

        print("Draft created!")
        print(f"Draft ID: {draft.id}")
        print(f"Status: {draft.status}")
        print()
        print("Draft Preview:")
        print("-" * 50)
        print(draft.draft_body[:1000])

    finally:
        db.close()


if __name__ == "__main__":
    main()
