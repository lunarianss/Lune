from datetime import datetime
import uuid
from domain.rag.models.enums import CreatedByRole

from sqlalchemy import String, PrimaryKeyConstraint, Index, Column, Integer, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.mysql import BIT
from sqlalchemy.sql import text


class Base(DeclarativeBase):
    pass


class UploadFile(Base):
    __tablename__ = "upload_files"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="upload_file_pkey"),
        Index("upload_file_tenant_idx", "tenant_id"),
    )

    id: Mapped[str] = Column(
        String(36), default=lambda: str(uuid.uuid4()), primary_key=True
    )
    tenant_id: Mapped[str] = Column(String(36), nullable=False)
    storage_type: Mapped[str] = Column(String(255), nullable=False)
    key: Mapped[str] = Column(String(255), nullable=False)
    name: Mapped[str] = Column(String(255), nullable=False)
    size: Mapped[int] = Column(Integer, nullable=False)
    extension: Mapped[str] = Column(String(255), nullable=False)
    mime_type: Mapped[str] = Column(String(255), nullable=True)
    created_by_role: Mapped[str] = Column(
        String(255), nullable=False, server_default=text("'account'")
    )
    created_by: Mapped[str] = Column(String(36), nullable=False)
    created_at: Mapped[datetime] = Column(
        DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    used: Mapped[list[int]] = Column(
        BIT(1), nullable=False, server_default=text("b'0'")
    )
    used_by: Mapped[str | None] = Column(String(36), nullable=True)
    used_at: Mapped[datetime | None] = Column(DateTime, nullable=True)
    hash: Mapped[str | None] = Column(String(255), nullable=True)

    def __init__(
        self,
        *,
        tenant_id: str,
        storage_type: str,
        key: str,
        name: str,
        size: int,
        extension: str,
        mime_type: str,
        created_by_role: CreatedByRole,
        created_by: str,
        created_at: datetime,
        used: bool,
        used_by: str | None = None,
        used_at: datetime | None = None,
        hash: str | None = None,
    ) -> None:
        self.tenant_id = tenant_id
        self.storage_type = storage_type
        self.key = key
        self.name = name
        self.size = size
        self.extension = extension
        self.mime_type = mime_type
        self.created_by_role = created_by_role.value
        self.created_by = created_by
        self.created_at = created_at
        self.used = used
        self.used_by = used_by
        self.used_at = used_at
        self.hash = hash
