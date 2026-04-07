from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Applicant
from model import check_eligibility

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/check")
def check(data: Applicant):
    result = check_eligibility(data)
    return {"result": result}