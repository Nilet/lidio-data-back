from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes import router as LabRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Adjust this to the domain of your Next.js app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health-check", tags=["Root"])
async def healthCheck():
    return {
        "message":
        "Working as expected"
    }

app.include_router(LabRouter, prefix='/lab')
