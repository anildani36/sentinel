import logging

from src.enums.notification_type_enum import NotificationType
from src.model.notification_request_model import NotificationRequestModel
from src.service.notification import EmailNotificationService, TeamsNotificationService

logger = logging.getLogger(__name__)


class SentinelService:
    def __init__(self, email_notification: EmailNotificationService, teams_notification: TeamsNotificationService):
        self.email_notification = email_notification
        self.teams_notification = teams_notification

    async def notify(self, notifications: NotificationRequestModel):
        for notification in notifications:
            if notification.type == NotificationType.EMAIL:
                await self.email_notification.send_notification(notification)

            if notification.type == NotificationType.TEAMS:
                await self.teams_notification.send_notification(notification)
