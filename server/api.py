from fastapi import FastAPI
from server.routes import router as LabRouter

app = FastAPI()


@app.get("/health-check", tags=["Root"])
async def healthCheck():
    return {
        "message":
        "Working as expected"
    }

app.include_router(LabRouter, prefix='/lab')
