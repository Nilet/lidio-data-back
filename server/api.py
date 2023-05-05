from fastapi import FastAPI
from server.routes import router as LabRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
        "https://lidio-data.vercel.app/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health-check", tags=["Root"])
async def healthCheck():
    return {
        "message":
        "Working as expected"
    }

app.include_router(LabRouter, prefix='/api/lab')
