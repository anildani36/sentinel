import logging

import boto3

from src.config.app_config import get_configs
from src.model.notification_model import NotificationMetadata
from src.service.notification.base_notification_service import BaseNotificationService

logger = logging.getLogger(__name__)


class EmailNotificationService(BaseNotificationService):
    def __init__(self):
        super().__init__()
        self.ses = boto3.client(
            "ses",
            aws_access_key_id=get_configs().aws_access_key_id,
            aws_secret_access_key=get_configs().aws_secret_access_key,
            region_name=get_configs().aws_region
        )

    async def send_notification(self, notification_metadata: NotificationMetadata):
        msg = {
            "Source": notification_metadata.from_email,
            "Destination": {
                "ToAddresses": notification_metadata.to,
                "CcAddresses": notification_metadata.cc,
                "BccAddresses": notification_metadata.bcc,
            },
            "Message": {
                "Body": {
                    "Text": {
                        "Data": notification_metadata.body,
                    },
                },
                "Subject": {
                    "Data": notification_metadata.subject,
                },
            },
        }

        try:
            response = self.ses.send_email(**msg)
            logger.info(
                f"Email sent successfully to {notification_metadata.to} subject: {notification_metadata.subject} : {response}")
        except Exception as err:
            logger.error(
                f"Error sending email to {notification_metadata.to} subject: {notification_metadata.subject} : {err}")
