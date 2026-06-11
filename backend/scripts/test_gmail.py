from app.email_providers.gmail_client import (
    get_recent_message_ids,
    get_message,
    get_header_value,
    get_plain_text_body,
)
from app.email_providers.gmail_provider import GmailProvider



def main():
    print("Fetching recent message IDs...\n")

    messages = get_recent_message_ids()

    print(f"Found {len(messages)} messages\n")

    if not messages:
        print("No messages found.")
        return

    message_id = messages[0]["id"]

    print(f"Using message ID: {message_id}\n")

    message = get_message(message_id)

    headers = message["payload"]["headers"]

    subject = get_header_value(
        headers,
        "Subject"
    )

    sender = get_header_value(
        headers,
        "From"
    )

    body = get_plain_text_body(message)

    print("=== SUBJECT ===")
    print(subject)

    print("\n=== SENDER ===")
    print(sender)

    print("\n=== BODY PREVIEW ===")
    print(body[:500])

#Output object of fetched email test
    # provider = GmailProvider()
    # print(provider.get_messages()[:1])


if __name__ == "__main__":
    main()