"""
Relation model
"""


from pydantic import BaseModel
from pydantic.fields import Field
from typing import Optional

class Relation(BaseModel):
    """
    Response model for preferences
    """
    
    id: Optional[str] = Field(
        ...,
        title="id",
        description="Id",
    )
    type: Optional[str] = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
    