"""
    Controllers for direct links request
"""
from src.models.errors import GenericError
from config.logger import logger
from src.controllers.directLink.tamilnadu import getTamilNaduDetails
def get_direct_links(res):
      """
      Controller for getting direct links
      """
      try:
        state = res[0]
        dist = res[1]
        aconst = res[2]
        pconst = res[3]
        getTamilNaduDetails("https://www.elections.tn.gov.in/SSR2022_MR_05012022/",state,dist,aconst,pconst)
        return "OK"
      except GenericError as exception:
        logger.error(f"failed due to {exception}")