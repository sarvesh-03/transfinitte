"""
Nagaland controller
"""

from src.controllers.downloadPDF import download_pdf
from src.controllers.pdfExtractNagaland import getDataFromPdf
def getNagalandDetails(urlFormat,state,dist,acid,psid):
  acNo=acid
  pcNo = psid
  laststring = f"S17A{acNo}P{pcNo}"
  p=f"{acNo}/{laststring}.pdf"
  url=urlFormat+p
  path = download_pdf(url,state,dist,acid,psid)
  return getDataFromPdf(path)