from app.email_providers.base import EmailProvider

from app.email_providers.gmail_client import (
    get_recent_message_ids,
    get_message,
    get_header_value,
    get_plain_text_body,
)


class GmailProvider(EmailProvider):

    def get_messages(self):
        messages = get_recent_message_ids()

        results = []

        for msg in messages:
            message = get_message(msg["id"])

            headers = message["payload"]["headers"]

            subject = get_header_value(headers, "Subject")
            sender = get_header_value(headers, "From")
            body = get_plain_text_body(message)

            results.append({
                "provider_message_id": msg["id"],
                "sender": sender,
                "subject": subject,
                "body": body
            })

        return results