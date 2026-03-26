from typing import List

from pydantic import BaseModel, Field

from src.model.notification_model import NotificationMetadata


class NotificationRequestModel(BaseModel):
    notifications: List[NotificationMetadata] = Field(..., title='notifications')
