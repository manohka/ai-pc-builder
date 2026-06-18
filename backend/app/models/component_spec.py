import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class ComponentSpec(Base):
    __tablename__ = "component_specs"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    component_id = Column(
        UUID(as_uuid=True),
        ForeignKey("components.id"),
        nullable=False
    )

    spec_key = Column(
        String(100),
        nullable=False
    )

    spec_value = Column(
        String(200),
        nullable=False
    )
