from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.app.schemas.resume_schema import ResumeAnalysisResponse, SkillGapAnalysis
from backend.app.services.nlp_parser import parser_service

router = APIRouter(prefix="/api/v1/resume", tags=["Resume NLP Analyzer"])

@router.post("/analyze", response_model=ResumeAnalysisResponse)
async def analyze_resume(file: UploadFile = File(...)):
    file_bytes = await file.read()
    raw_text = parser_service.extract_text_from_stream(file_bytes, file.filename)
    analysis = parser_service.analyze_skills(raw_text)
    
    return ResumeAnalysisResponse(
        filename=file.filename,
        parsed_sections={"raw_character_count": str(len(raw_text)), "word_count": str(len(raw_text.split()))},
        extracted_entities={"skills_detected": analysis["all_extracted"]},
        skill_analysis=SkillGapAnalysis(
            matched_skills=analysis["matched_skills"],
            missing_skills=analysis["missing_skills"],
            match_percentage=analysis["match_percentage"],
            seniority_level=analysis["seniority_level"]
        ),
        recommendations=analysis["recommendations"]
    )
