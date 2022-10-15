"""
    Route for direct links request
"""
from fileinput import filename
from math import dist
from fastapi import APIRouter, HTTPException
from src.models.errors import GenericError
from src.models.directLinks import DirectLinksRequestModal, DirectLinksResponseModal
from config.logger import logger #,"Tiruppur"
import requests
import os

router = APIRouter(prefix="/directLinks")
tamilnaduDistricts = ["Thiruvallur","Chennai","Kancheepuram","Vellore","Krishnagiri","Dharmapuri","Tiruvannamalai","Viluppuram","Salem","Namakkal","Erode","Nilgiris","Coimbatore","Dindigul","Karur","Tiruchirappalli","Perambalur","Cuddalore","Nagapattinam","Tiruvarur","Thanjavur","Pudukottai","Sivaganga","Madurai","Theni","Virudhunagar","Ramanathapuram","Thoothukudi","Tirunelveli","Kanniyakumari","Ariyalur","Tirupur","Kallakurichi","Tenkasi","Chengalpattu","Tirupattur","Ranippet","Mayiladuthurai"]
def addZeroes(num):
    numLen=len(num)
    if numLen==1:
        return "00"+num
    elif numLen==2:
        return "0"+num
    else: 
        return num
# @router.post("/getDirectLinks")
def get_direct_links(res):
      """
      POST route for getting direct links
      """
      try:
        state=res[0]
        dist=res[1]
        aconst=res[2]
        pconst=res[3]
        print(os.getcwd())
        basepath="/home/sarvesh/template/api/src/pdfs"
        filepath=state
        path=os.path.join(basepath,filepath)
        if not os.path.isdir(path):
          os.mkdir(path)
        distNo = tamilnaduDistricts.index(f"{dist}")+1
        print(distNo)
        acNo = "ac"+addZeroes(aconst)
        pcNo = addZeroes(pconst)
        laststring = f"{acNo}{pcNo}"
        url =f"https://www.elections.tn.gov.in/SSR2022_MR_05012022/dt{distNo}/{acNo}/{laststring}.pdf"
        print("Url" + url)
        res = requests.get(url)
        open(f"{path}/{laststring}.pdf", "wb").write(res.content)
      except GenericError as exception:
        logger.error(f"failed due to {exception}")
        raise HTTPException(
            status_code=403,
            detail=f"An unexpected error occurred while updating events:{Exception}",
        ) from Exception
