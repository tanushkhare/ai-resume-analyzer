from pydantic import BaseModel
from typing import List, Optional

class ResumeRequest(BaseModel):
    resume_text: str
    job_description: Optional[str] = ""

class ResumeResponse(BaseModel):
    status: str
    extracted_email: str
    extracted_phone: str
    skills_matched: List[str]
    fit_score: str
    recommendation: str
