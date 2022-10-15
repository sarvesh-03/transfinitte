"""
TamilNadu controller
"""

from src.controllers.downloadPDF import download_pdf
tamilnaduDistricts = ["Thiruvallur","Chennai","Kancheepuram","Vellore","Krishnagiri","Dharmapuri","Tiruvannamalai","Viluppuram","Salem","Namakkal","Erode","Nilgiris","Coimbatore","Dindigul","Karur","Tiruchirappalli","Perambalur","Cuddalore","Nagapattinam","Tiruvarur","Thanjavur","Pudukottai","Sivaganga","Madurai","Theni","Virudhunagar","Ramanathapuram","Thoothukudi","Tirunelveli","Kanniyakumari","Ariyalur","Tirupur","Kallakurichi","Tenkasi","Chengalpattu","Tirupattur","Ranippet","Mayiladuthurai"]
def addZeroes(num):
    numLen=len(num)
    if numLen==1:
        return "00"+num
    elif numLen==2:
        return "0"+num
    else: 
        return num
def getTamilNaduDetails(urlFormat,state,dist,acid,psid):
  distNo = tamilnaduDistricts.index(dist)+1
  acNo="ac"+addZeroes(acid)
  pcNo = addZeroes(psid)
  laststring = f"{acNo}{pcNo}"
  p=f"dt{distNo}/{acNo}/{laststring}.pdf"
  url=urlFormat+p
  download_pdf(url,state,dist,acid,psid)
