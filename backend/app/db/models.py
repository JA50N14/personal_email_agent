import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base


class Email(Base):
    __tablename__ = "emails"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    provider_message_id = Column(String, unique=True, index=True, nullable=False)

    sender = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    body = Column(String, nullable=True)

    received_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    is_processed = Column(Boolean, default=False)


