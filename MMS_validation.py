import pandas as pd
from tabulate import tabulate
import math

def sepMMS(row,name):  
    return row[name][1:-2].split(";")
    
def diff(row):
    dE =  float(row.E_MMS) - float(row.E_RTK)
    dN =  float(row.N_MMS) - float(row.N_RTK)
    dh =  float(row.h_MMS) - float(row.h_RTK)
    return dE,dN,dh
    
def CalcError( df ):
    err = list()
    for ax in ['dE', 'dN', 'dh']:
        MAE = df[ax].abs().sum()/len(df)
        STD = df[ax].std()
        MSE = (df[ax]**2).sum()/len(df)
        err.append( { 'axis': ax , 'MAE':MAE,'STD':STD,'MSE':MSE} )
    dfError = pd.DataFrame( err  )
    return dfError
    
def axis_error(df,STR):
    MAE = df[STR].abs().sum()/len(df)
    STD = df[STR].std()
    MSE = (df[STR]**2).sum()/len(df)
    return [MAE,STD,MSE]

def RMSE(df):
    sum_dE2 = row2.dE2.sum()
    sum_dN2 = row2.dN2.sum() 
    sum_dh2 = row2.dh2.sum()
    mean_2d = (sum_dE2 + sum_dN2) /len(row2)
    mean_3d = (sum_dE2 + sum_dN2 + sum_dh2) /len(row2)
    mean_v = sum_dh2/len(row2)
    RMSE_H = math.sqrt(mean_2d)
    RMSE_V = math.sqrt(mean_v)
    RMSE_3d = math.sqrt(mean_3d)
    return [RMSE_H,RMSE_V,RMSE_3d]
    
def All_axis_error(df):
    error_E = axis_error(df,"dE")
    error_N = axis_error(df,"dN")
    error_h = axis_error(df,"dh")
    dfe = pd.DataFrame({"Name":["MAE","STD","MSE"]})
    dfe[["dE","dN","dh"]] = error_E,error_N,error_h
    return dfe

def double(row):
    dE2 = row.dE ** 2
    dN2 = row.dN ** 2
    dh2 = row.dh ** 2
    return dE2,dN2,dh2

df1 = pd.read_csv("GCP_Measure_edit5_speed_30_60.csv")

for spd,row in df1.groupby('Speed'):
    row[["E_MMS","N_MMS","h_MMS"]] = row.apply(lambda row: sepMMS(row,"MMS_measure"),axis = 1,result_type='expand')
    row[["E_RTK","N_RTK","h_RTK"]] = row.apply(lambda row: sepMMS(row,"RTK_measure"),axis = 1,result_type='expand')
    row2 = row.drop(row.columns.difference(["NO","Strip","Speed","E_MMS","N_MMS","h_MMS","E_RTK","N_RTK","h_RTK"]), axis = 1)
    row2[["dE","dN","dh"]] = row2.apply(diff,axis = 1,result_type = 'expand')
    row2[["dE2","dN2","dh2"]] = row2.apply(double,axis = 1,result_type = 'expand')
    RMSE_H,RMSE_V,RMSE_3d = RMSE(row2)
    row2 = row2.drop(["dE2","dN2","dh2"],axis = 1)
    dfe = All_axis_error(row2)
    print(f"=================== Speed = {spd} km/hr ===================")
    print(row2.to_markdown(floatfmt = (".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".6f",".6f",".6f")))
    print(f"RMSE_H  = {RMSE_H:.3f}")
    print(f"RMSE_V  = {RMSE_V:.3f}")
    print(f"RMSE_3d = {RMSE_3d:.3f}")
    print(tabulate(dfe, tablefmt = "pipe",floatfmt=(".3f",".3f",".3f",".3f",".0f"),showindex=False,headers="keys"))
    print(f"===========================================================")
    #import pdb; pdb.set_trace()
    
import pdb; pdb.set_trace()