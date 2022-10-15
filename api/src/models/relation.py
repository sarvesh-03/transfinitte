"""
Relation model
"""


from pydantic import BaseModel
from pydantic.fields import Field


class Relation(BaseModel):
    """
    Response model for preferences
    """

    id: str = Field(
        ...,
        title="id",
        description="Id",
    )
    type: str = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
    