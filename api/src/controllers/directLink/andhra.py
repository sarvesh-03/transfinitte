"""
Andhra controller
"""

andhraDistricts=["Srikakulam","Vizianagaram","Visakhapatnam","East Godavari","West Godavari","Krishna","Guntur","Prakasam","Nellore","Kadapa","Kurnool","Anantapur","Chittoor"]

# https://ceoaperolls.ap.gov.in/AP_Eroll_2022/Popuppage?partNumber=1&roll=EnglishMotherRoll&districtName=DIST_03&acname=23&acnameeng=A23&acno=23&acnameurdu=023

def addZeroes(num):
  if num >=1 & num <=9:
    return "0"+str(num)
  return str(num)
def addZeores2(n):
  num= str(n)
  numLen=len(num)
  if numLen==1:
        return "00"+num
  elif numLen==2:
        return "0"+num
  else: 
        return num
def getAndhraDetails(urlFormat,state,dist,acid,psid):
  dcid = andhraDistricts.index(dist)+1
  params=f"?partNumber={psid}&roll=EnglishMotherRoll&districtName=DIST_{addZeroes(dcid)}&acname={acid}&acnameeng=A{acid}&acno={acid}&acnameurdu={addZeores2(acid)}"
  url=urlFormat+params
  print(url)
  return url
