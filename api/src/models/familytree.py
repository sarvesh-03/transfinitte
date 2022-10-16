"""
User model
"""


from pydantic import BaseModel
from pydantic.fields import Field

from src.models.relation import Relation


class UserRelation(BaseModel):
    """
    Response model for preferences
    """

    id: str = Field(
        ...,
        title="id",
        description="Id",
    )
    gender: str = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
    parents: list[Relation] = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
    spouses: list[Relation] = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
    children: list[Relation] = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
    siblings: list[Relation] = Field(
        ...,
        title="type",
        description="Domain of form response that needs to be downloaded",
    )
 