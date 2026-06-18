import uuid

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class RecommendationRule(Base):
    __tablename__ = "recommendation_rules"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    source_component_type = Column(
        String(50),
        nullable=False
    )

    source_tier = Column(
        Integer,
        nullable=False
    )

    target_component_type = Column(
        String(50),
        nullable=False
    )

    min_target_tier = Column(
        Integer,
        nullable=False
    )

    max_target_tier = Column(
        Integer,
        nullable=False
    )

    build_profile = Column(
        String(50),
        nullable=False
    )
