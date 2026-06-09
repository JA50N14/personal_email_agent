from app.email_providers.base import EmailProvider
from app.services.email_repository import EmailRepository


class EmailSyncService:

    def __init__(
        self,
        email_provider: EmailProvider,
        email_repository: EmailRepository
    ):
        self.email_provider = email_provider
        self.email_repository = email_repository
    
    def get_messages(self):
        return self.email_provider.get_messages()

    def sync_emails(self):
        messages = self.email_provider.get_messages()

        for message in messages:

            existing_email = (
                self.email_repository.get_by_provider_message_id(
                    message["provider_message_id"]
                )
            )

            if existing_email:
                continue

            self.email_repository.create_email(
                provider_message_id=message["provider_message_id"],
                sender=message["sender"],
                subject=message["subject"],
                body=message["body"]
            )