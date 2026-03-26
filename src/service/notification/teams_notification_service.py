import json
import logging

import httpx

from src.model.notification_model import NotificationMetadata
from src.service.notification.base_notification_service import BaseNotificationService

logger = logging.getLogger(__name__)


class TeamsNotificationService(BaseNotificationService):
    def __init__(self):
        super().__init__()
        self.webhook_url = ""
        self.headers = {"Content-Type": "application/json"}

    async def send_notification(self, notification_metadata: NotificationMetadata):
        """
            send a simple text message to an MS Teams channel using a webhook

            The webhook receives a simple message,
            the Power Automate workflow creates an adaptive card and posts to MS Teams
            Ensure that the Power Automate workflow has been so configured.
        """
        payload = json.dumps(
            {
                "@context": "http://schema.org/extensions",
                "type": "MessageCard",
                "title": notification_metadata.subject,
                "summary": "This workflow accepts a direct message rather than a preformed adaptive card",
                "text": notification_metadata.body,
                "themeColor": "2DC72D"
            }
        )

        try:
            response = httpx.post(url=self.webhook_url, content=payload, headers=self.headers)
            logger.info(f"response status: {response.status_code}")
        except Exception as e:
            logger.info(f"error: {e}")
