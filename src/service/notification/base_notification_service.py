import logging
from abc import abstractmethod, ABC

from src.model.notification_model import NotificationMetadata

logger = logging.getLogger(__name__)


class BaseNotificationService(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def send_notification(self, notification_metadata: NotificationMetadata):
        pass
