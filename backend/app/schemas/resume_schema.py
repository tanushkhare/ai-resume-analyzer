from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class SkillGapAnalysis(BaseModel):
    matched_skills: List[str]
    missing_skills: List[str]
    match_percentage: float
    seniority_level: str

class ResumeAnalysisResponse(BaseModel):
    filename: str
    parsed_sections: Dict[str, str]
    extracted_entities: Dict[str, List[str]]
    skill_analysis: SkillGapAnalysis
    recommendations: List[str]
