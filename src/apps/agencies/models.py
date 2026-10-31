from enum import Enum as PythonEnum
from uuid import UUID, uuid4

from sqlalchemy import Enum as SAEnum
from sqlalchemy import String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from config.database import Base


class AgencyStatus(str, PythonEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class Agency(Base):
    __tablename__ = "agencies"

    id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[AgencyStatus] = mapped_column(
        SAEnum(
            AgencyStatus,
            name="ck_agencies_status",
            native_enum=False,
            create_constraint=True,
            values_callable=lambda enum_cls: [member.value for member in enum_cls],
            length=20,
        ),
        nullable=False,
    )
