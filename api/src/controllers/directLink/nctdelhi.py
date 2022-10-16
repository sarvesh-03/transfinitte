"""
NCT OF Delhi controller
"""

from src.controllers.downloadPDF import download_pdf
def getMDelhiDetails(urlFormat,state,dist,acid,psid):
  acNo=acid
  pcNo = psid
  laststring = f"U05A{acNo}P{pcNo}"
  p=f"AC{acNo}/{laststring}.pdf"
  url=urlFormat+p
  download_pdf(url,state,dist,acid,psid)