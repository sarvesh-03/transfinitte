"""
Department Router
"""

from fastapi import APIRouter, Depends, HTTPException
from api.src.controllers.electoral_bot import get_captcha_bot, get_cred_details
from api.src.models.electoral import ElectoralRequest
from api.src.models.errors import GenericError
from config.logger import logger
from main import driver

router = APIRouter(prefix="/electoral")


@router.post("/details/")
async def post_details(
    request:ElectoralRequest
) -> bytes:

    try:
        driver.get("https://electoralsearch.in/")
        return get_captcha_bot(request=request)
        
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching departments:{exception}",
        ) from exception


@router.post("/code/")
async def post_code(
    code:str
):

    try:
        res_list = get_cred_details(code)
        return {"response":res_list}
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching departments:{exception}",
        ) from exception

