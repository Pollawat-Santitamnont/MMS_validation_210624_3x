import laspy
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import shapely.geometry as geom
from matplotlib import cm
from skspatial.objects import Point,Points
import math

def sepMMS(row,name):  
    return row[name][1:-1].split(";")
def pntden(folder,row):
    CEN = row.E_MMS,row.N_MMS,row.h_MMS
    las = laspy.read( folder + "/" + row.Strip)
    df = pd.DataFrame ({'X':las.xyz[:,0], 'Y':las.xyz[:,1], 'Z':las.xyz[:,2]})
    xmin,ymin,xmax,ymax = geom.Point(CEN[0], CEN[1]).buffer(0.6).bounds #setตามความยาวแนวทแยงของGCP ให้เกินหน่อยเพราะจะได้เก็บ GCP ได้ครบ
    df = df[ (df.X>xmin)   & (df.X<xmax)   &  (df.Y>ymin)  & (df.Y<ymax)]
    AREA = (df.X.max() - df.X.min())*(df.Y.max()-df.Y.min())
    Point_density = int(len(df)/AREA)
    return Point_density
    
if 1: ### auto get point density ###
    dfGCP = pd.read_csv("./GCP_Measure_edit5_speed_30_60.csv")
    #speed which you used
    Speed = 30
    dfGCP = dfGCP[dfGCP['Speed'] == Speed]
    #folder where you placed .las file
    folder = "./Speed_30"
    dfGCP[["E_MMS","N_MMS","h_MMS"]] = dfGCP.apply(lambda row: sepMMS(row,"MMS_measure"),axis = 1,result_type='expand')
    dfGCP[["E_RTK","N_RTK","h_RTK"]] = dfGCP.apply(lambda row: sepMMS(row,"RTK_measure"),axis = 1,result_type='expand')
    #import pdb; pdb.set_trace()
    dfGCP["Point_density_pnt_per_sqm"] = dfGCP.apply(lambda row: pntden(folder,row),axis = 1)
    pnt_mean = math.floor(dfGCP["Point_density_pnt_per_sqm"].mean())
    dfGCP = dfGCP.drop(["MMS_measure","RTK_measure"],axis = 1)
    print(dfGCP.to_markdown(floatfmt = (".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".3f",".6f",".6f",".6f")))
    print(f"point_density = {pnt_mean} pnt/sqm.")
    #output to keep
    dfGCP.to_pickle(f"./dfGCP_speed{Speed}.pkl") 
    import pdb; pdb.set_trace()

if 0: ### get old pickle and plot
    dfGCP = pd.read_pickle("./dfGCP_speed30.pkl")  
    # using a function df.plot.bar() 
    dfGCP.plot.bar(x = 'NO', y = 'Point_density_pnt_per_sqm',rot = 0)
    plt.show()

    



if 0: ### source ###
    dfGCP = pd.read_csv("GCP_Measure_edit5_speed_30.csv")
    dfGCP[["E_MMS","N_MMS","h_MMS"]] = dfGCP.apply(lambda row: sepMMS(row,"MMS_measure"),axis = 1,result_type='expand')
    dfGCP[["E_RTK","N_RTK","h_RTK"]] = dfGCP.apply(lambda row: sepMMS(row,"RTK_measure"),axis = 1,result_type='expand')
    ## sample ##
    #CEN = 678411.533,1527288.589,-29.356 # GCP:14 Flight-line :  009+300_010+000_FWD.las Speed : 30 km/hr
    #CEN = 678679.559,1527097.680,-28.810 # GCP:15 Flight-line :  009+300_010+000_FWD.las Speed : 30 km/hr
    #las = laspy.read(r'009+300_010+000_FWD.las') 
    #CEN = 678666.340,1527065.860,-28.870 # GCP:13 Flight-line :  009+300_010+000_REV.las, Speed : 30 km/hr
    pntden = []
    for i in range(len(dfGCP)):
        if i == 4: # be float nan so cant find density
            continue
        else:
            CEN = dfGCP["E_MMS"].iloc[i],dfGCP["N_MMS"].iloc[i],dfGCP["h_MMS"].iloc[i]
            las = laspy.read(dfGCP["Strip"].iloc[i]) 
    
            #las = laspy.read(r'20220819124907000.las')
            
    
            #import pdb ; pdb.set_trace()
    
            ##############################
            df = pd.DataFrame ({'X':las.xyz[:,0], 'Y':las.xyz[:,1], 'Z':las.xyz[:,2],
                                'return_number':las.return_number.array,
                                'classification':las.classification.array,
                                'intensity':las.intensity})
            #import pdb; pdb.set_trace()
            xmin,ymin,xmax,ymax = geom.Point(CEN[0], CEN[1]).buffer(0.6).bounds #setตามความยาวแนวทแยงของGCP ให้เกินหน่อยเพราะจะได้เก็บ GCP ได้ครบ
            # set 0.6 จะได้ 1.2*1.2 m ถ้า set 2 จะได้ 4*4 m
            df = df[ (df.X>xmin)   & (df.X<xmax)   &  (df.Y>ymin)  & (df.Y<ymax)]
            AREA = (df.X.max() - df.X.min())*(df.Y.max()-df.Y.min())
            print("index = ",i)
            print("Strip",dfGCP["Strip"].iloc[i])
            print("NO",dfGCP["NO"].iloc[i])
            print(f'Point density ={int(len(df)/AREA)} pnt/sqm.')
            pntden.append(int(len(df)/AREA))
            ########################33
            #import pdb ; pdb.set_trace()
            PC=Points( df.to_numpy())
            #####################plot only one graph##################################
            if 0:
                CM = cm.get_cmap('Greys')
                fig = plt.figure()
                #ax = fig.add_subplot(111, projection='3d')
                ax = fig.add_subplot(111)
                ax.set_aspect('auto')
                #cb = PC.plot_3d( ax , s=1, alpha=0.5, c=df.intensity, cmap=CM)
                cb = PC.plot_2d( ax , s=1, alpha=0.5, c=df.intensity, cmap=CM)
                #cb = PC.plot_3d( ax , s=1, alpha=0.5)
                #ax.set_zlim(df.Z.mean()-0.5,df.Z.mean()+0.5)
    
                fig.colorbar(cb, cax = cb, ax = ax)
                plt.show()
            
            #print("xmax-xmin",xmax-xmin)
            #print("ymax-ymin",ymax-ymin)
    print(f"average_point_density = {math.floor(sum(pntden)/len(pntden))} pnt/sqm.")
    import pdb; pdb.set_trace()