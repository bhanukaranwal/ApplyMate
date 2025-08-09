from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import endpoints, cover_letters
import uvicorn

app = FastAPI(
    title="ApplyMate — Job Application Tracker & Auto Cover Letter Writer",
    description="Track job applications, scrape job listings, and auto-generate tailored cover letters.",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(endpoints.router, prefix="/api/jobs", tags=["Job Listings"])
app.include_router(cover_letters.router, prefix="/api/cover-letter", tags=["Cover Letters"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to ApplyMate API — Ready to help you land your dream job!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
