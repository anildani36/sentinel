import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from starlette.middleware.cors import CORSMiddleware

from src.config.app_config import get_configs
from src.injection.container import Application
from src.routes.actuator_routes import actuator_api_router
from src.routes.notification_routes import notification_api_router

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s'
)


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Application startup
    logger.info('Initializing application and loading dependencies...')
    logger.info(f'Application startup completed for env :: {get_configs().env_name}')
    yield
    # Application Shutdown


app = FastAPI(lifespan=lifespan)

security = HTTPBearer()

# Include all routers
app.include_router(actuator_api_router, prefix='/api/v1/actuator')
app.include_router(notification_api_router, prefix='/api/v1/notify')

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency Injection ( Do Not Move, this should be after including all routers )
container = Application()
app.container = container

if __name__ == '__main__':
    # Run App
    uvicorn.run(app, host="0.0.0.0", port=get_configs().port)
