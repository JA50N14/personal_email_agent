from app.email_providers.base import EmailProvider


class GmailProvider(EmailProvider):

    def get_messages(self):
        return [
            {
                "provider_message_id": "gmail_001",
                "sender": "alice@example.com",
                "subject": "Welcome",
                "body": "Hello from Gmail"
            }
        ]