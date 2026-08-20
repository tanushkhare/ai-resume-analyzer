from fastapi import APIRouter
from app.schemas.resume import ResumeRequest, ResumeResponse
from app.services.parser import parse_resume_text

router = APIRouter(prefix="/api", tags=["Analysis"])

@router.post("/analyze", response_model=ResumeResponse)
def analyze_endpoint(data: ResumeRequest):
    return parse_resume_text(data.resume_text)
