"""
Goa controller
"""

from src.controllers.downloadPDF import download_pdf
def addZeroes(num):
    numLen=len(num)
    if numLen==1:
        return "00"+num
    elif numLen==2:
        return "0"+num
    else: 
        return num
def getGoaDetails(urlFormat,state,dist,acid,psid):
  acNo="A"+acid
  pcNo = "P"+psid
  laststring = f"S05{acNo}{pcNo}"
  p=f"{acid}/{laststring}.pdf"
  url=urlFormat+p
  print("Url"+ url)
  download_pdf(url,state,dist,acid,psid)
