"""
WestBengal controller
"""
from src.controllers.downloadPDF import download_pdf
from src.controllers.pdfExtractNagaland import getDataFromPdf
westBengalDistricts =['COOCHBEHAR', 'JALPAIGURI', 'DARJEELING', 'UTTAR DINAJPUR', 'DAKHSIN DINAJPUR', 'MALDA', 'MURSHIDABAD', 'NADIA', 'NORTH 24 PARGANAS', 'SOUTH 24  PARGANAS', 'KOLKATA SOUTH', 'KOLKATA NORTH', 'HOWRAH', 'HOOGHLY', 'PURBO MEDINIPUR', 'PASCHIM MEDINIPUR', 'PURULIA', 'BANKURA', 'PURBA BARDHAMAN', 'BIRBHUM', 'ALIPURDUAR', 'KALIMPONG', 'JHARGRAM', 'PASCHIM BARDHAMAN']
def getWestBengalDetails(urlFormat,state,dist,acid,psid):
  dcid = westBengalDistricts.index(dist)+1
  params=f"?DCID={dcid}%20&ACID={acid}&PSID={psid}#toolbar=0&navpanes=0"
  url=urlFormat+params
  path=download_pdf(url,state,dist,acid,psid)
  return getDataFromPdf(path)