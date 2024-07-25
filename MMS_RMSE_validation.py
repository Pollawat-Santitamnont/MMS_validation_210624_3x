import pandas as pd
import math

def sepMMS(row,name):  
    return row[name][1:-2].split(";")
def diff(row):
    dE =  float(row.E_MMS) - float(row.E_RTK)
    dN =  float(row.N_MMS) - float(row.N_RTK)
    dh =  float(row.h_MMS) - float(row.h_RTK)
    return dE,dN,dh
def double(row):
    dE2 = row.dE ** 2
    dN2 = row.dN ** 2
    dh2 = row.dh ** 2
    return dE2,dN2,dh2


#df1 = pd.read_csv("GCP_Measure.csv")
df1 = pd.read_csv("GCP_Measure_edit5_speed_30_60.csv")
# Select only Speed if dont , hashtag it #
df1 = df1[df1['Speed'] == 30]
#df1 = df1[df1['Speed'] == 60] 
#import pdb; pdb.set_trace()
df1[["E_MMS","N_MMS","h_MMS"]] = df1.apply(lambda row: sepMMS(row,"MMS_measure"),axis = 1,result_type='expand')
df1[["E_RTK","N_RTK","h_RTK"]] = df1.apply(lambda row: sepMMS(row,"RTK_measure"),axis = 1,result_type='expand')
df2 = df1.drop(df1.columns.difference(["NO","Strip","Speed","E_MMS","N_MMS","h_MMS","E_RTK","N_RTK","h_RTK"]), axis = 1)
df2[["dE","dN","dh"]] = df2.apply(diff,axis = 1,result_type = 'expand')
df2[["dE2","dN2","dh2"]] = df2.apply(double,axis = 1,result_type = 'expand')
#import pdb; pdb.set_trace()
# drop outliner if dont , hashtag it #

# drop when all
#df2 = df2.drop([14,29],axis = 0)

# drop when speed 30
#df2 = df2.drop([14],axis = 0)

# drop when speed 60
#df2 = df2.drop([29],axis = 0)

#import pdb; pdb.set_trace()
sum_dE2 = df2.dE2.sum()
sum_dN2 = df2.dN2.sum() 
sum_dh2 = df2.dh2.sum()
mean_2d = (sum_dE2 + sum_dN2) /len(df2)
mean_3d = (sum_dE2 + sum_dN2 + sum_dh2) /len(df2)
mean_v = sum_dh2/len(df2)
RMSE_H = math.sqrt(mean_2d)
RMSE_V = math.sqrt(mean_v)
RMSE_3d = math.sqrt(mean_3d)
df2 = df2.drop(["dE2","dN2","dh2"],axis = 1)
print(df2.to_markdown(floatfmt = (".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".6f",".6f",".6f")))
print(f"RMSE_H  = {RMSE_H:.3f}")
print(f"RMSE_V  = {RMSE_V:.3f}")
print(f"RMSE_3d = {RMSE_3d:.3f}")
import pdb; pdb.set_trace()