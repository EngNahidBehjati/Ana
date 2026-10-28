from fastapi import FastAPI

from apps.agencies.router import router as agency_router

app = FastAPI(title="Ana-Backend", version="0.1.0")
app.include_router(agency_router, prefix="/api/v1")


@app.get("/health")
def health_check():
    return {"status": 200, "message": "OK"}
