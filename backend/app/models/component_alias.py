import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class ComponentAlias(Base):
    __tablename__ = "component_aliases"

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

    alias = Column(
        String(200),
        nullable=False
    )
