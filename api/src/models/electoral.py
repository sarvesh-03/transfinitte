"""
Electoral model
"""


from pydantic import BaseModel
from pydantic.fields import Field


class ElectoralRequest(BaseModel):
    """
    Response model for preferences
    """

    name: str = Field(
        ...,
        title="name",
        description="Domain of form response that needs to be downloaded",
    )
    fname: str = Field(
        ...,
        title="fname",
        description="Domain of form response that needs to be downloaded",
    )
    year: str = Field(
        ...,
        title="year",
        description="year students's form response that needs to be downloaded",
    )
    month: str = Field(
        ...,
        title="month",
        description="year students's form response that needs to be downloaded",
    )
    day: str = Field(
        ...,
        title="day",
        description="year students's form response that needs to be downloaded",
    )
    gender: str = Field(
        ...,
        title="year",
        description="year students's form response that needs to be downloaded",
    )
    state: str = Field(
        ...,
        title="state",
        description="year students's form response that needs to be downloaded",
    )
    district: str = Field(
        ...,
        title="district",
        description="year students's form response that needs to be downloaded",
    )
    ac: str = Field(
        ...,
        title="ac",
        description="year students's form response that needs to be downloaded",
    )

