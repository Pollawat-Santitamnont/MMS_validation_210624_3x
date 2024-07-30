# การคำนวณเพื่อตรวจสอบค่าพิกัดของ GNSS ที่ไปรังวัดในสนามในงานแผนงานในเวลาที่ต่างกัน การวัดสอบเทียบ MMS ระหว่าง Trimble MX-9,
#CHCNAV AU20 และ  Phoenix MX-2

############################
# พลวัต สันติธรรมนนท์ 
# นักศึกษาปริญญาโท ภาควิชาวิศวกรรมสำรวจ
# คณะวิศวกรรมศาสตร์  จุฬาลงกรณ์มหาวิทยาลัย 
############################
# update log
# v2 
#1.make_table_with_apply  2.mean is enough 3.read_csv with usecols
############################
from tabulate import tabulate
import pandas as pd
import numpy as np

def diff(row):
    dE = row["Easting.1"] - row["Easting.2"]
    dN = row["Northing.1"] - row["Northing.2"]
    dh = row["Ellipsoidal Height.1"] - row["Ellipsoidal Height.2"]
    return dE,dN,dh


#นำข้อมูลเข้า
colnames = ['Name', 'Northing.1', 'Easting.1', 'Ellipsoidal Height.1',
                    'Northing.2', 'Easting.2', 'Ellipsoidal Height.2']
df = pd.read_csv("GCPs.csv",skiprows=1,usecols = colnames)
#import pdb; pdb.set_trace()
df[["dE","dN","dh"]] = df.apply(lambda row: diff(row),axis = 1,result_type = 'expand')
meandE = df.dE.mean()
meandN = df.dN.mean()
meandh = df.dh.mean()
df2 = df.drop(df.columns.difference(['Name','dE', 'dN','dh']),axis = 1)
#import pdb; pdb.set_trace()

#แสดงผลข้อมูล
print(df2.to_markdown(floatfmt = [".3f",".3f",".3f",".3f"],showindex = False))

#ค่าพิกัด RMSE ทั้งทางราบและดิ่ง
print("mean_dE = {0:.3f} m" .format(meandE))
print("mean_dN = {0:.3f} m" .format(meandN))
print("mean_dh = {0:.3f} m" .format(meandh))

import pdb; pdb.set_trace()