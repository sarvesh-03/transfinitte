"""
Department Router
"""

import imp
from lib2to3.pgen2 import driver
from fastapi import APIRouter, Depends, HTTPException
from src.controllers.electoral_bot import get_captcha_bot, get_cred_details
from src.models.electoral import ElectoralRequest
from src.models.errors import GenericError
from config.logger import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from src.controllers.directLink.directLink import get_direct_links
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


router = APIRouter(prefix="/electoral")

@router.on_event("startup")
async def start_driver():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=chrome_options)
    
@router.on_event("shutdown")
async def start_driver():
    driver.quit()
    
@router.post("/details/")
async def post_details(
    request:ElectoralRequest
) -> bytes:

    try:
        driver.get("https://electoralsearch.in/")
        return get_captcha_bot(request=request,driver=driver)
        
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
        res_list = get_cred_details(code,driver=driver)
        print(res_list)
        get_direct_links(res_list)
        return {"response":res_list}
    except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while fetching departments:{exception}",
        ) from exception

