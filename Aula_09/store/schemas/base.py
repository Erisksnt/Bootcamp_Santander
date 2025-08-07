import datetime
import uuid
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
