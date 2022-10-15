"""
    Controllers for direct links request
"""
import imp
from src.models.errors import GenericError
from config.logger import logger
from src.controllers.directLink.tamilnadu import getTamilNaduDetails
from src.controllers.directLink.westbengal import getWestBengalDetails
from src.controllers.directLink.punjab import getPunjabDetails
from src.controllers.directLink.goa import getGoaDetails
def get_direct_links(res):
      """
      Controller for getting direct links
      """
      try:
        state = res[0]
        dist = res[1]
        aconst = res[2]
        pconst = res[3]
        if state == "Tamil Nadu":
          getTamilNaduDetails("https://www.elections.tn.gov.in/SSR2022_MR_05012022/",state,dist,aconst,pconst)
        elif state == "West Bengal":
          getWestBengalDetails("http://ceowestbengal.nic.in/FinalRoll.aspx",state,dist,aconst,pconst)
        elif state == "Punjab":
          getPunjabDetails("https://ceopunjab.gov.in/erollpdf2/",state,dist,aconst,pconst)
        elif state == "Goa":
          getGoaDetails("https://ceogoa.nic.in/erollpdf2/",state,dist,aconst,pconst)
        return "OK"
      except GenericError as exception:
        logger.error(f"failed due to {exception}")