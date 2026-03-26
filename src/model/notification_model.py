from typing import Optional

from pydantic import BaseModel, EmailStr, Field, model_validator

from src.enums.notification_type_enum import NotificationType


class NotificationMetadata(BaseModel):
    type: NotificationType = Field(..., title="notification type")

    subject: str
    body: str

    # Email fields
    from_email: Optional[EmailStr] = None
    to: list[EmailStr] = Field(default_factory=list)
    cc: list[EmailStr] = Field(default_factory=list)
    bcc: list[EmailStr] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_by_type(self):
        if self.type == "email":
            if not self.from_email:
                raise ValueError("from_email is required for email notifications")
            if not self.to or not len(self.to) > 0:
                raise ValueError("at least one recipient in 'to' is required for email")

        return self