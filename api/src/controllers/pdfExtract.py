from pdf2image import convert_from_path
import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image
import pdf2image
import difflib
import re
import pandas as pd
import sys
import numpy as np
from tqdm import tqdm

from translate import Translator
translator= Translator(from_lang="tamil",to_lang="english")


###Function to convert PDFs to Images 
# Input: PDF File name with .pdf and folder relative to current directory
# Output: Saves images in the folder
def image_pdf(pdf_file, folder, image_list):
  #pdf_file='test'
  images = convert_from_path(pdf_file)
  if not os.path.exists(folder):
      os.makedirs(folder)
  for i in range(len(images)):

    images[i].save(folder+'/'+ str(i) +'.jpg', 'JPEG')
    image_list.append(Image.open(folder+'/'+ str(i) +'.jpg'))
  return image_list 

###Function to convert Images to Text 
# Input: Image File with and folder relative to current directory
# Output: Saves images in the folder

def image_text(imageORfile,psm=11,if_file=True):

  #imageORfile='test0.jpg'
  if if_file:
    text_extracted = pytesseract.image_to_string(Image.open(imageORfile),config='psm '+str(psm),lang='tam+eng')
  else:
    text_extracted = pytesseract.image_to_string(imageORfile,config='psm '+str(psm), lang='tam+eng') 
  return text_extracted 

###Function to crop images 


def image_crop(imageORfile,crop_dim_list,if_file=True):
  if if_file:
    im=Image.open(imageORfile)
  else:
    im= imageORfile
  im1 = im.crop(crop_dim_list)
  return im1 

###Function to crop a page into voter blocks

def voter_block_crop(page_image,is_page2=False):
  crop_block_list=[]
  imag=page_image
  if is_page2:
    start_height=133
  else:
    start_height=115
  width=501
  height=195
  b=start_height
  for i in np.arange(1,31,1):  
    if (i%3)==1:
      a=60
      c,d=a+width,b+height
      crop_list=[a,b,c,d]
      crop_block_list.append(image_crop(imag,crop_list,False))
    if (i%3)==2:
      a=561
      c,d=a+width,b+height
      crop_list=[a,b,c,d]
      crop_block_list.append(image_crop(imag,crop_list,False))    
    if (i%3)==0:
      a=1063
      c,d=a+width,b+height
      crop_list=[a,b,c,d]
      if i>=3:
        b+=height
      crop_block_list.append(image_crop(imag,crop_list,False))
  crop_block_image_list=crop_block_list
  
  return crop_block_image_list

#### Voter ID  ####
def get_voterid(text_rows):
  row = text_rows
  if (len(row))>0:
    voterid=row[0].strip()
  return voterid

#### Gender and Age ####

def get_gender_age(text_rows):
  global age
  global gender
  row = text_rows
  
  if (len(row))>0:
    for row_iter in range(len(row)):
      if row[row_iter].startswith(('வயது')):
        gender = row[row_iter].replace('-', '').replace('Available','').replace('is','').replace('Photo','').split(':')[-1]
        if gender.__contains__("பெண்‌"):
             gender = "female"
        elif gender.__contains__("ஆண்‌"):
            gender = "male"
        else:
            gender = "other"
        age = row[row_iter].replace('-', '').replace('Available','').replace('is','').replace('Photo','').split(('பாலினம்'))[0].strip('வயது:')       
  return age, gender

#### Father/Husband Name ####

def get_f_h_name(text_rows):
  global f_or_h
  global f_h_name
  row = text_rows
  if (len(row))>0:    
    for row_iter in range(len(row)):
      if row[row_iter].startswith(('கணவர்‌','தந்‌ைத','தந்த')):
        if row[row_iter].startswith(('தந்‌ைத','தந்த')):
          if not row[row_iter+1].startswith(('வீட்டு')):
            f_h_name=row[row_iter]+' '+row[row_iter+1].replace('-', '').replace('Available','').replace('is','').replace('Photo','').strip('தந்‌ைத பெயர்‌:')
            # f_h_name = translator.translate(f_h_name)
          else:
            f_h_name=row[row_iter].replace('-', '').replace('Available','').replace('is','').replace('Photo','').strip('தந்‌ைத பெயர்‌:')
            # f_h_name = translator.translate(f_h_name)
          f_or_h='father'
        elif row[row_iter].startswith(('கணவர்‌')):
          if not row[row_iter+1].startswith(('வீட்டு')):
            f_h_name=row[row_iter]+' '+row[row_iter+1].replace('-', '').replace('Available','').replace('is','').replace('Photo','').strip('கணவர்‌ பெயர்‌:')
            # f_h_name = translator.translate(f_h_name)
          else:
            f_h_name=row[row_iter].replace('-', '').replace('Available','').replace('is','').replace('Photo','').strip('கணவர்‌ பெயர்‌:')
            # f_h_name = translator.translate(f_h_name)


          f_or_h='husband'
        else:
          f_or_h=''
  return f_or_h,f_h_name

#### Name ####
def get_name(text_rows):
  global name  
  row = text_rows
  if (len(row))>0:
    for row_iter in range(len(row)):
      if row[row_iter].startswith('பெயர்‌:'):
        if not row[row_iter+1].startswith(('கணவர்‌','தந்‌ைத','தந்த')):
          name=row[row_iter]+' '+row[row_iter+1].replace('-', '').strip('பெயர்‌:')
          # name = translator.translate(name)
        else:
          name=row[row_iter].replace('-', '').strip('பெயர்‌:')
          # name = translator.translate(name)
  return name

#### House Number ####
def get_house_no(text_rows):
    global house_no
    house_no = -1
    row = text_rows
    if(len(row)) > 0:
        for row_iter in range(len(row)):
            if row[row_iter].startswith('வீட்டு'):
                house_no = row[row_iter].replace('-', '').replace('Available','').replace('is','').replace('Photo','').strip('வீட்டு எண்:').replace(': ',"")
                print(house_no)
                
    return house_no

#### Get Details from Voter Block #####

def get_voter_block_textrows(block_image):
  text_raw= image_text(block_image,psm=11,if_file=False)
  row=[]
  slno=False
  for j in text_raw.split('\n'):
    if j != '' and j != ' ' and j != '\x0c'and j != '  ' and j != '   'and j != '    ':
      row.append(j)
  return row

def get_voter_block_details(row):
  v_id=get_voterid(row)
  v_name=get_name(row)
  f_or_h,f_h_name=get_f_h_name(row)
  house_no = get_house_no(row)  
  age, gender = get_gender_age(row)
  slno=True
  return v_id,v_name,f_or_h,f_h_name,age,gender,slno,house_no


sl_no=1
lista=[]
image_list = []
image_pdf('ac1.pdf','./images', image_list)
print(image_list)
for page_iter in tqdm(range(len(image_list))):
    
    if page_iter==2:
       block_images=voter_block_crop(image_list[page_iter],True)
    elif page_iter>2:
       block_images=voter_block_crop(image_list[page_iter],False)
    else:
      continue
    for block_iter in range(len(block_images)):
      rows_text=get_voter_block_textrows(block_images[block_iter])
      if len(rows_text)>2:
        v_id,v_name,f_or_h,f_h_name,age,gender,slno,house_no=get_voter_block_details(rows_text)
        #print(v_id)
        # print( house_no)
        lista.append([v_id,v_name,f_or_h,f_h_name,age,gender,house_no,sl_no])
        sl_no+=1

def findf_or_h(v_id):
    f_or_h = asw.loc[asw["v_id"] == v_id]["f_or_h"].values[0]
    return f_or_h

def findf_or_h_name(v_id):
    f_or_h_name = asw.loc[asw["v_id"] == v_id]["f_h_name"].values[0]
    return f_or_h_name

def findf_or_h_id(v_id):
    f_or_h_name = findf_or_h_name(v_id)
    House_no = getHouseNoFromDF(v_id)
    f_or_h_id = asw.loc[(asw["v_name"].str.contains(f_or_h_name[:-2])) & (asw["house_no"] == House_no)]["v_id"].values[0]
    return f_or_h_id

def getGenderFromDF(v_id):
    gender = asw.loc[asw["v_id"] == v_id]["gender"].values[0]
    return gender

def getNameFromDF(v_id):
    name = asw.loc[asw["v_id"] == v_id]["v_name"].values[0]
    print(name)
    return name

def getHouseNoFromDF(v_id):
    House_no = asw.loc[asw["v_id"] == v_id]["house_no"].values[0]
    return House_no

def findSpouseId(v_id):
    v_name = getNameFromDF(v_id).replace("\u200c","").strip()
    h_no = getHouseNoFromDF(v_id)
    spouse_id = asw.loc[(asw["f_h_name"].str.contains(v_name[:-2])) &  (asw["f_or_h"] == "husband") & (asw["house_no"] == h_no)]["v_id"].values[0]
                                                                          
    return spouse_id

def getParents(v_id):
    f_or_h = findf_or_h(v_id)
    if f_or_h == "father":
        father_id = findf_or_h_id(v_id)
        print(father_id)
        mother_id = findSpouseId(father_id)
        return father_id, mother_id
    else:
        return "Not possible with given data"
    

def getSpouseParents(v_id):
    f_or_h = findf_or_h(v_id)
    if f_or_h == "husband":
        husband_id = findf_or_h_id(v_id)
        SpouseFatherId, SpouseMotherId = getParents(husband_id)
    return SpouseFatherId, SpouseMotherId

def getSibilings(v_id):
    f_or_h = findf_or_h(v_id)
    if f_or_h == "father":
        father_name = findf_or_h_name(v_id)
        h_no = getHouseNoFromDF(v_id)
        IDs = asw.loc[(asw["f_h_name"].str.contains(father_name[:-2])) & (asw["f_or_h"] == "father") & (asw["house_no"] == h_no)]["v_id"].values
        sibilingsIDs = np.delete(IDs, np.where(IDs == v_id))
        return sibilingsIDs
    
def getChildren(v_id):
    v_gender = getGenderFromDF(v_id)
    if v_gender == "male":
        v_name = getNameFromDF(v_id).replace("\u200c","").strip()
        h_no = getHouseNoFromDF(v_id)
        childrenIDs = asw.loc[(asw["f_h_name"].str.contains(v_name[:-2])) & (asw["f_or_h"] == 'father') & (asw["house_no"] == h_no)]["v_id"].values
        return childrenIDs

def getDataFromPdf(path):
    sl_no=1
    lista=[]
    image_list = []
    image_pdf(path,'./images', image_list)
    for page_iter in tqdm(range(len(image_list))):
    
        if page_iter==2:
            block_images=voter_block_crop(image_list[page_iter],True)
        elif page_iter>2:
            block_images=voter_block_crop(image_list[page_iter],False)
        else:
            continue
    for block_iter in range(len(block_images)):
      rows_text=get_voter_block_textrows(block_images[block_iter])
      if len(rows_text)>2:
        v_id,v_name,f_or_h,f_h_name,age,gender,slno,house_no=get_voter_block_details(rows_text)
        #print(v_id)
        # print( house_no)
        lista.append([v_id,v_name,f_or_h,f_h_name,age,gender,house_no,sl_no])
        sl_no+=1
    
    asw=pd.DataFrame(lista,columns=['v_id','v_name','f_or_h','f_h_name','age','gender','house_no','sl_no'])
    