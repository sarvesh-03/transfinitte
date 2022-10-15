"""
Models for general exception responses
"""


from pydantic import BaseModel
from pydantic.fields import Field

class DirectLinksRequestModal(BaseModel):
    """
    Model for direct links request
    """

    state: str = Field(..., title="State", description="Name of the state")
    district: str = Field(..., title="District", description="Name of the district")
    aconst: str = Field(..., title="Assembly Constituency", description="Name of the assembly constituency")
    pconst: str = Field(..., title="Part Constituency", description="Name of the part constituency")    

class DirectLinksResponseModal(BaseModel):
    """
    Model for direct links response
    """

    message: list = Field(..., title="links",description="links for pdfs", example=["https://www.youtube.com/watch?v=dQw4w9WgXcQ"])