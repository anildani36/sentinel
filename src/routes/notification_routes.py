import logging

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Body, Depends

from src.controllers.notification_controller import NotificationController
from src.injection.container import Application
from src.model.notification_request_model import NotificationRequestModel

logger = logging.getLogger(__name__)

notification_api_router = APIRouter(tags=["Notification API"])


@notification_api_router.post("/")
@inject
async def notify(
        request: NotificationRequestModel,
        notification_controller: NotificationController = Depends(Provide[Application.services.notification_controller])
):
    return await notification_controller.handle_notification(request)
