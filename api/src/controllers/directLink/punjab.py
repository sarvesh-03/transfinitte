"""
Punjab controller
"""

from src.controllers.downloadPDF import download_pdf
from src.controllers.pdfExtractNagaland import getDataFromPdf
def addZeroes(num):
    numLen=len(num)
    if numLen==1:
        return "00"+num
    elif numLen==2:
        return "0"+num
    else: 
        return num
def getPunjabDetails(urlFormat,state,dist,acid,psid):
  acNo="A"+addZeroes(acid)
  pcNo = "P"+addZeroes(psid)
  laststring = f"{acNo}{pcNo}"
  p=f"{acNo}/{laststring}.pdf"
  url=urlFormat+p
  download_pdf(url,state,dist,acid,psid)
