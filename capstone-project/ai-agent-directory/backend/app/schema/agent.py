from typing import Optional

from pydantic import BaseModel, Field


class AgentSchema(BaseModel):
    id: Optional[int] = Field(
        None, description="Unique identifier for the agent"
    )
    name: str = Field(..., description="Name of the agent")
    description: Optional[str] = Field(
        None, max_length=1000, description="Description of the agent"
    )
    homepage_url: Optional[str] = Field(
        None, max_length=100, description="Homepage URL of the agent"
    )
    category: Optional[str] = Field(
        None, max_length=1000, description="Category of the agent"
    )
    source: Optional[str] = Field(
        None, max_length=1000, description="Source of the agent information"
    )
    trending: Optional[int] = Field(
        False, description="Indicates if the agent is trending"
    )

    class Config:
        from_attributes = True


class AgentTrendingUpdate(BaseModel):
    trending: bool


class AgentTrendingResponse(BaseModel):
    name: str
    trending: bool

    class Config:
        from_attributes = True
