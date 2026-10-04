from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ana.api.health import router as health_router
from ana.core.config import get_settings
from ana.core.logging import configure_logging

settings = get_settings()
configure_logging(settings.log_level)

app = FastAPI(title="Ana API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin).rstrip("/") for origin in settings.cors_origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health_router, prefix="/api/v1")
