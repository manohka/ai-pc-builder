import uuid

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class Component(Base):
    __tablename__ = "components"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(200),
        nullable=False
    )

    component_type = Column(
        String(50),
        nullable=False
    )

    brand = Column(
        String(100),
        nullable=False
    )

    tier = Column(
        Integer,
        nullable=False
    )

    price = Column(
        Numeric(10, 2),
        nullable=True
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at = Column(
        DateTime,
        nullable=True
    )

    updated_at = Column(
        DateTime,
        nullable=True
    )
