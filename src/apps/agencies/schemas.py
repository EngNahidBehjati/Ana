from pydantic import BaseModel, Field


class AgencyCreateRequest(BaseModel):
    name: str = Field(min_length=3, max_length=25)
