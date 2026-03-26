import logging

from src.model.notification_request_model import NotificationRequestModel
from src.service.sentinel_service import SentinelService

logger = logging.getLogger(__name__)


class NotificationController:

    def __init__(self, sentinel_service: SentinelService):
        self.sentinel_service = sentinel_service

    async def handle_notification(self, notifications: NotificationRequestModel):
        return await self.sentinel_service.notify(notifications)
