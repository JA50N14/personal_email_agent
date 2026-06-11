import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def get_gmail_service():
    creds = Credentials.from_authorized_user_file(
        "token.json",
        SCOPES
    )

    return build(
        "gmail",
        "v1",
        credentials=creds
    )

def get_recent_message_ids():
    service = get_gmail_service()

    results = (
        service.users()
        .messages()
        .list(
            userId="me",
            maxResults=10
        )
        .execute()
    )

    return results.get("messages", [])

def get_message(message_id: str):
    service = get_gmail_service()

    return (
        service.users()
        .messages()
        .get(
            userId="me",
            id=message_id
        )
        .execute()
    )


def get_header_value(headers, header_name):
    for header in headers:
        if header["name"] == header_name:
            return header["value"]

    return None

def get_plain_text_body(message):
    parts = message["payload"].get("parts", [])

    for part in parts:
        if part["mimeType"] == "text/plain":

            encoded_body = part["body"].get("data")

            if not encoded_body:
                return ""

            decoded_body = base64.urlsafe_b64decode(
                encoded_body
            ).decode("utf-8")

            return decoded_body

    return ""