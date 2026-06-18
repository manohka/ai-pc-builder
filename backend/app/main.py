from fastapi import FastAPI

from app.api.recommendation_controller import (
    router as recommendation_router
)

app = FastAPI(
    title="AI PC Builder API"
)

app.include_router(
    recommendation_router
)
