from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.data_engineering_pipeline.schemas import AgenticDataEngineeringPipelineSessionCreate, AgenticDataEngineeringPipelineSessionResponse
from app.domain.data_engineering_pipeline.service import AgenticDataEngineeringPipelineService

router = APIRouter(prefix="/api/v1/data_engineering_pipeline", tags=["Agentic Data Engineering Pipeline Domain"])

@router.post("/sessions", response_model=AgenticDataEngineeringPipelineSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticDataEngineeringPipelineSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Data Engineering Pipeline.
    """
    return AgenticDataEngineeringPipelineService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticDataEngineeringPipelineSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticDataEngineeringPipelineService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
