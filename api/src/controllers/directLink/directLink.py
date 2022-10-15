"""
    Controllers for direct links request
"""
import imp
from src.models.errors import GenericError
from config.logger import logger
from src.controllers.directLink.tamilnadu import getTamilNaduDetails
from src.controllers.directLink.westbengal import getWestBengalDetails
def get_direct_links(res):
      """
      Controller for getting direct links
      """
      try:
        # state = res[0]
        # dist = res[1]
        # aconst = res[2]
        # pconst = res[3]
        state="West Bengal"
        dist = "JALPAIGURI"
        aconst = 14
        pconst = 172
        if state == "Tamil Nadu":
          getTamilNaduDetails("https://www.elections.tn.gov.in/SSR2022_MR_05012022/",state,dist,aconst,pconst)
        elif state == "West Bengal":
          getWestBengalDetails("http://ceowestbengal.nic.in/FinalRoll.aspx",state,dist,aconst,pconst)
        return "OK"
      except GenericError as exception:
        logger.error(f"failed due to {exception}")