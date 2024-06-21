# การคำนวณเพื่อตรวจสอบค่าพิกัดของ GNSS ที่ไปรังวัดในสนามในงานแผนงาน การวัดสอบเทียบ MMS ระหว่าง Trimble MX-9,
#CHCNAV AU20 และ  Phoenix MX-2

############################
# พลวัต สันติธรรมนนท์ 
# นักศึกษาปริญญาโท ภาควิชาวิศวกรรมสำรวจ
# คณะวิศวกรรมศาสตร์  จุฬาลงกรณ์มหาวิทยาลัย 
############################
from tabulate import tabulate
import pandas as pd
import numpy as np

#นำข้อมูลเข้า
df = pd.read_csv("GCPs.csv",skiprows=1)

#ส่วนการคำนวณ
#คิดทางราบ
dE = pd.DataFrame(df["Easting.1"] - df["Easting.2"],columns = ['dE'])
dN = pd.DataFrame(df["Northing.1"] - df["Northing.2"],columns = ['dN'])

#คิดทางดิ่ง สามารถคิด h หรือ H ก็ได้
dH = pd.DataFrame(df["Orthometric Height.1"] - df["Orthometric Height.2"],columns = ['dH'])

#คำนวน RMSE
df2 = pd.concat([dE,dN,dH],axis = 1)
df2["dE2"] = df2["dE"] ** 2
df2["dN2"] = df2["dN"] ** 2
df2["dH2"] = df2["dH"] ** 2
sum_E2 = df2["dE2"].sum()
sum_N2 = df2["dN2"].sum()
mean_H = sum_E2+sum_N2/len(df2)
RMSE_H = np.sqrt(mean_H)
sum_H2 = df2["dH2"].sum()
mean_V = sum_H2/len(df2)
RMSE_V = np.sqrt(mean_V)

#แสดงผลข้อมูล
print(df2.to_markdown(floatfmt = [".3f",".3f",".3f",".6f",".6f",".6f"]))

#ค่าพิกัด RMSE ทั้งทางราบและดิ่ง
print("RMSE_H = {0:.3f}" .format(RMSE_H))
print("RMSE_V = {0:.3f}" .format(RMSE_V))