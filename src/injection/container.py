from dependency_injector import containers, providers

from src.controllers.notification_controller import NotificationController
from src.service.notification.email_notification_service import EmailNotificationService
from src.service.notification.teams_notification_service import TeamsNotificationService
from src.service.sentinel_service import SentinelService


class Gateways(containers.DeclarativeContainer):
    ...


class Services(containers.DeclarativeContainer):

    gateways = providers.DependenciesContainer()

    sentinel_service = providers.Factory(
        SentinelService,
    )

    email_notification_service = providers.Factory(
        EmailNotificationService
    )

    teams_notification_service = providers.Factory(
        TeamsNotificationService,
    )

    notification_controller = providers.Factory(
        NotificationController,
        sentinel_service=sentinel_service,
    )

class Application(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[
        'src.routes.actuator_routes',
        'src.routes.notification_routes',
    ])

    gateways = providers.Container(
        Gateways
    )

    services = providers.Container(
        Services,
        gateways=gateways,
    )
