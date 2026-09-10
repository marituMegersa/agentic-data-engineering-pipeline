from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.data_engineering_pipeline.models import AgenticDataEngineeringPipelineSession, AgenticDataEngineeringPipelineItem
from app.domain.data_engineering_pipeline.schemas import AgenticDataEngineeringPipelineSessionCreate, AgenticDataEngineeringPipelineItemCreate

class AgenticDataEngineeringPipelineService:
    @staticmethod
    def create_session(db: Session, data: AgenticDataEngineeringPipelineSessionCreate) -> AgenticDataEngineeringPipelineSession:
        db_obj = AgenticDataEngineeringPipelineSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticDataEngineeringPipelineSession:
        return db.query(AgenticDataEngineeringPipelineSession).filter(AgenticDataEngineeringPipelineSession.id == session_id).first()
