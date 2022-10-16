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
        state = res[0]
        dist = res[1]
        aconst = res[2]
        pconst = res[3]
        # state = "Andhra Pradesh"
        # dist = "Srikakulam"
        # aconst = "1"
        # pconst = "1"
        # state="Nagaland"
        # dist = "JALPAIGURI"
        # aconst = "1"
        # pconst = "4"
        if state == "Tamil Nadu":
          return getTamilNaduDetails("https://www.elections.tn.gov.in/SSR2022_MR_05012022/",state,dist,aconst,pconst)
        elif state == "West Bengal":
          getWestBengalDetails("http://ceowestbengal.nic.in/FinalRoll.aspx",state,dist,aconst,pconst)
        elif state == "Punjab":
          getPunjabDetails("https://ceopunjab.gov.in/erollpdf2/",state,dist,aconst,pconst)
        elif state == "Goa":
          getGoaDetails("https://ceogoa.nic.in/PDF/EROLL/MOTHERROLL/2021/",state,dist,aconst,pconst)
        elif state == "Andhra Pradesh":
          getAndhraDetails("https://ceoaperolls.ap.gov.in/AP_Eroll_2022/Popuppage",state,dist,aconst,pconst)
        elif state == "Meghalaya":
          getMeghalayaDetails("https://ceomeghalaya.nic.in/erolls/pdf/english/",state,dist,aconst,pconst)
        elif state == "NCT Of Delhi":
          getMDelhiDetails("https://ceodelhi.gov.in/engdata/",state,dist,aconst,pconst)
        elif state == "Nagaland":
          return getNagalandDetails("https://ceo.nagaland.gov.in/Downloads/FinalRoll2022/",state,dist,aconst,pconst)
        return "OK"
      except GenericError as exception:
        logger.error(f"failed due to {exception}")