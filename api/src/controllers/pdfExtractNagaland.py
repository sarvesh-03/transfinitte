from tokenize import String
from src.models.familytree import UserRelation
from src.models.relation import Relation
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
from src.controllers import electoral_bot

asw=pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

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
    text_extracted = pytesseract.image_to_string(Image.open(imageORfile),config='psm '+str(psm),lang='eng')
  else:
    text_extracted = pytesseract.image_to_string(imageORfile,config='psm '+str(psm), lang='eng') 
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
    try:
        row = text_rows

        if (len(row))>0:
            for row_iter in range(len(row)):
                if row[row_iter].startswith(('Age')):
                    gender = row[row_iter].replace('is','').replace('Photo','').split(':')[-1]
                    age = row[row_iter].replace('is','').replace('Photo','').split(('Gender'))[0].strip('Age:')       
        return age, gender
    except UnboundLocalError:
        pass
#### Father/Husband Name ####

def get_f_h_name(text_rows):
    try:
        row = text_rows
        if (len(row))>0:    
            for row_iter in range(len(row)):
                if row[row_iter].startswith("Father"):
                    f_h_name=row[row_iter].strip("Father's Name:")
                    f_h_name = re.sub(r'[^a-zA-Z0-9]', '', f_h_name)
                    f_or_h = 'father'
               
                elif row[row_iter].startswith("Husband"):
                        f_h_name=row[row_iter].strip("Husband's Name:")
                        f_h_name = re.sub(r'[^a-zA-Z0-9]', '', f_h_name)
                        f_or_h = 'husband'
                      
                elif row[row_iter].startswith("Mother"):
                        f_or_h = "NaN"
                        f_h_name = "NaN"
                        
        return f_or_h,f_h_name
    except UnboundLocalError:
        pass

#### Name ####
def get_name(text_rows):
  try:
    row = text_rows
    print(text_rows)
    if (len(row))>0:
        for row_iter in range(len(row)):
            if row[row_iter].startswith('Name'):
                name=row[row_iter].strip('Name').replace(":","").strip()
                return name
  except UnboundLocalError:
    pass


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
    try:
        v_id=get_voterid(row)
        v_name=get_name(row)
        f_or_h,f_h_name=get_f_h_name(row)
        age, gender = get_gender_age(row)
        house_no = get_house_no(row)
        slno=True
        return v_id,v_name,f_or_h,f_h_name,age,gender,house_no,slno
    except TypeError:
        pass

def get_house_no(text_rows):
    house_no=0
    row = text_rows
    if(len(row)) > 0:
        for row_iter in range(len(row)):
            if row[row_iter].startswith('House'):
                house_no = row[row_iter].strip('House Number:')
                house_no = re.sub(r'[^0-9]', "", house_no)
    return house_no

def findf_or_h(v_id):
    try:
        f_or_h = asw.loc[asw["v_id"] == v_id]["f_or_h"].values[0]
        return f_or_h
    except:
        pass

def findf_or_h_name(v_id):
    try:
        f_or_h_name = asw.loc[asw["v_id"] == v_id]["f_h_name"].values[0]
        return f_or_h_name
    except:
        pass

def findf_or_h_id(v_id):
    try:
        f_or_h_name = findf_or_h_name(v_id)
        House_no = getHouseNoFromDF(v_id)
        f_or_h_id_values = asw.loc[(asw["v_name"] == f_or_h_name) & (asw["house_no"] == House_no)]["v_id"].values
        if len(f_or_h_id_values) > 0:
            f_or_h_id = f_or_h_id_values[0]
            return f_or_h_id
    except:
        pass

def getGenderFromDF(v_id):
    try:
        print(v_id)
        gender = asw.loc[asw["v_id"] == v_id]["gender"].values[0].strip()
        return gender
    except:
        pass    

def getNameFromDF(v_id):
    try:
        name = asw.loc[asw["v_id"] == v_id]["v_name"].values[0]
        return name
    except:
        pass

def getHouseNoFromDF(v_id):
    try:
        House_no = asw.loc[asw["v_id"] == v_id]["house_no"].values[0]
        return House_no
    except:
        pass

def findSpouseId(v_id):
    try:
        v_name = getNameFromDF(v_id)
        h_no = getHouseNoFromDF(v_id)
        spouse_id = asw.loc[(asw["f_h_name"] == v_name) &  (asw["f_or_h"] == "husband") & (asw["house_no"] == h_no)]["v_id"].values[0]
                                                                          
        return spouse_id
    except:
        pass

def getParents(v_id):
    f_or_h = findf_or_h(v_id)
    if f_or_h == "father":
        father_id = findf_or_h_id(v_id)
        print(father_id)
        mother_id = findSpouseId(father_id)
        return father_id, mother_id
    else:
        pass
    

def getSpouseParents(v_id):
    f_or_h = findf_or_h(v_id)
    if f_or_h == "husband":
        husband_id = findf_or_h_id(v_id)
        SpouseFatherId, SpouseMotherId = getParents(husband_id)
        return SpouseFatherId, SpouseMotherId

def getSibilings(v_id):
    try:
        f_or_h = findf_or_h(v_id)
        if f_or_h == "father":
            father_name = findf_or_h_name(v_id)
            h_no = getHouseNoFromDF(v_id)
            IDs = asw.loc[(asw["f_h_name"].str.contains(father_name[:-2])) & (asw["f_or_h"] == "father") & (asw["house_no"] == h_no)]["v_id"].values
            sibilingsIDs = np.delete(IDs, np.where(IDs == v_id))
            return sibilingsIDs
    except:
        pass
def getChildren(v_id):
    try:
        v_gender = getGenderFromDF(v_id)
        if v_gender == "MALE":
            v_name = getNameFromDF(v_id).strip()
            h_no = getHouseNoFromDF(v_id)
            childrenIDs = asw.loc[(asw["f_h_name"] == v_name) & (asw["f_or_h"] == 'father') & (asw["house_no"] == h_no)]["v_id"].values
            return childrenIDs
    except:
        pass

def getRelatives(v_id,vis_set,response):

  if v_id not in vis_set:
    vis_set.add(v_id)
    children=getChildren(v_id)
    print(children)
    child_relation=[]
    if children is not None:
        for id in children:
            child_relation.append(Relation(id=id,type='blood'))
            getRelatives(id,vis_set,response)
    siblings=getSibilings(v_id)
    siblings_relation=[]
    print(siblings)
    if siblings is not None:
        for id in siblings:
            siblings_relation.append(Relation(id=id,type='blood'))
            getRelatives(id,vis_set,response)
    parents=getParents(v_id)
    parents_relation=[]
    print(parents)
    if parents is not None:
        for id in parents:
            parents_relation.append(Relation(id=id,type='blood'))
            getRelatives(id,vis_set,response)
    spouse_relation=[]
    sp_id=findSpouseId(v_id)
    if sp_id is not None:
        spouse_relation.append(Relation(id=sp_id,type='married'))
    gen=getGenderFromDF(v_id)
    if gen is not None:    
        res=UserRelation(id=v_id,gender=gen,parents=parents_relation,spouses=spouse_relation,children=child_relation,siblings=siblings_relation)
        response.append(res)
    

    
      
lista=[]
def getDataFromPdf(path):
    print(electoral_bot.voter_id)
    sl_no=1
    
    response = []
    vis_set=set(String)
    image_list = []
    image_pdf(path,'./imagesNagaland', image_list)
    image_list = image_list[:23]
    for page_iter in tqdm(range(len(image_list))):
    
        if page_iter==2:
            block_images=voter_block_crop(image_list[page_iter],True)
        elif page_iter>2:
            block_images=voter_block_crop(image_list[page_iter],False)
        else:
            continue
        for block_iter in range(len(block_images)):
            rows_text=get_voter_block_textrows(block_images[block_iter])
            try:
            
                if len(rows_text)>2:
                    v_id,v_name,f_or_h,f_h_name,age,gender,slno,house_no=get_voter_block_details(rows_text)
            #print(v_id)
            # print( house_no)
                lista.append([v_id,v_name,f_or_h,f_h_name,age,gender,house_no,sl_no])
                sl_no+=1
            except TypeError:
                print(rows_text)
    
    global asw
    print(len(lista))
    asw=pd.DataFrame(lista,columns=['v_id','v_name','f_or_h','f_h_name','age','gender','house_no','sl_no'])
    print(asw)
    getRelatives(electoral_bot.voter_id,vis_set,response)
    return response
