"""
    Controllers for direct links request
"""
import imp
from src.controllers.directLink.meghalaya import getMeghalayaDetails
from src.models.errors import GenericError
from config.logger import logger
from src.controllers.directLink.tamilnadu import getTamilNaduDetails
from src.controllers.directLink.westbengal import getWestBengalDetails
from src.controllers.directLink.punjab import getPunjabDetails
from src.controllers.directLink.goa import getGoaDetails
from src.controllers.directLink.andhra import getAndhraDetails
from src.controllers.directLink.nctdelhi import getMDelhiDetails
from src.controllers.directLink.nagaland import getNagalandDetails
def get_direct_links(res):
      """
      Controller for getting direct links
      """
      try:
        print(res)
        state = res[0]
        dist = res[1]
        aconst = res[2]
        pconst = res[3]
        # state = "Andhra Pradesh"
        # dist = "Srikakulam"
        # aconst = "1"
        # pconst = "1"
        if state == "Tamil Nadu":
          return getTamilNaduDetails("https://www.elections.tn.gov.in/SSR2022_MR_05012022/",state,dist,aconst,pconst)
        elif state == "West Bengal":
          return getWestBengalDetails("http://ceowestbengal.nic.in/FinalRoll.aspx",state,dist,aconst,pconst)
        elif state == "Punjab":
          return getPunjabDetails("https://ceopunjab.gov.in/erollpdf2/",state,dist,aconst,pconst)
        elif state == "Goa":
          return getGoaDetails("https://ceogoa.nic.in/PDF/EROLL/MOTHERROLL/2021/",state,dist,aconst,pconst)
        elif state == "Andhra Pradesh":
          return getAndhraDetails("https://ceoaperolls.ap.gov.in/AP_Eroll_2022/Popuppage",state,dist,aconst,pconst)
        elif state == "Meghalaya":
          return getMeghalayaDetails("https://ceomeghalaya.nic.in/erolls/pdf/english/",state,dist,aconst,pconst)
        elif state == "NCT Of Delhi":
          return getMDelhiDetails("https://ceodelhi.gov.in/engdata/",state,dist,aconst,pconst)
        elif state == "Nagaland":
          return getNagalandDetails("https://ceo.nagaland.gov.in/Downloads/FinalRoll2022/",state,dist,aconst,pconst)
        return "OK"
      except GenericError as exception:
        logger.error(f"failed due to {exception}")