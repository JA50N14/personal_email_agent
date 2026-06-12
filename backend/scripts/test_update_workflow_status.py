import app.db  # forces Email + EmailDraft registration

from app.db.session import SessionLocal
from app.services.email_repository import EmailRepository


def main():
    db = SessionLocal()

    try:
        email_repository = EmailRepository(db)

        email_id = "8a593922-5555-4a7d-8fb3-15160d26100d"

        email = email_repository.update_workflow_status(
            email_id=email_id,
            workflow_status="skipped",
        )

        print("Updated email:")
        print(f"id={email.id}")
        print(f"workflow_status={email.workflow_status}")

    finally:
        db.close()


if __name__ == "__main__":
    main()