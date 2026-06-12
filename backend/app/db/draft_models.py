from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from app.db.session import Base


class EmailDraft(Base):
    __tablename__ = "email_drafts"

    id = Column(Integer, primary_key=True, index=True)

    email_id = Column(UUID(as_uuid=True), ForeignKey("emails.id"), nullable=False)

    draft_body = Column(Text, nullable=False)

    status = Column(String, default="pending")  # pending | rejected | sent

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())