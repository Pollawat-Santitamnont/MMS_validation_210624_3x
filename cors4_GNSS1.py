import toml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pyproj
from pyproj import CRS,Proj

def plot():
    #plot 1
    fig, ax = plt.subplots()
    ax.scatter(df3.dE, df3.dN)
    #centerlize graph
    xabs_max = abs(max(ax.get_xlim(), key=abs))
    yabs_max = abs(max(ax.get_ylim(), key=abs))
    ax.set_xlim(xmin=-xabs_max, xmax=xabs_max)
    ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)
    #name
    for i, txt in enumerate(df3.name):
        ax.annotate(txt, (df3.dE.iloc[i], df3.dN.iloc[i]))
        
    plt.title("EN PLANE")
    plt.xlabel("E(m)")
    plt.ylabel("N(m)")
    plt.grid()
    plt.show()



    #plot 2
    fig, ax = plt.subplots()
    ax.scatter(df3.dE, df3.dU)
    #centerlize graph
    xabs_max = abs(max(ax.get_xlim(), key=abs))
    yabs_max = abs(max(ax.get_ylim(), key=abs))
    ax.set_xlim(xmin=-xabs_max, xmax=xabs_max)
    ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)
    #name
    for i, txt in enumerate(df3.name):
        ax.annotate(txt, (df3.dE.iloc[i], df3.dU.iloc[i]))
    plt.title("EU PLANE")
    plt.xlabel("E(m)")
    plt.ylabel("U(m)")

    plt.grid()
    plt.show()

    #plot 3
    fig, ax = plt.subplots()
    ax.scatter(df3.dN, df3.dU)
    #centerlize graph
    xabs_max = abs(max(ax.get_xlim(), key=abs))
    yabs_max = abs(max(ax.get_ylim(), key=abs))
    ax.set_xlim(xmin=-xabs_max, xmax=xabs_max)
    ax.set_ylim(ymin=-yabs_max, ymax=yabs_max)
    #name
    for i, txt in enumerate(df3.name):
        ax.annotate(txt, (df3.dN.iloc[i], df3.dU.iloc[i]))
    plt.title("NU PLANE")
    plt.xlabel("N(m)")
    plt.ylabel("U(m)")

    plt.grid()
    plt.show()

pyproj.datadir.set_data_dir(r'C:\Anaconda3\Lib\site-packages\pyproj')
def xyz2utm(x,y,z,zone):
    ecef = {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'} # Cartisian
    utm = "EPSG:326"+zone # 47 or 47 WGS84 UTM Zone 47N
    transproj = pyproj.Transformer.from_crs(ecef,utm)
    E,N,h = transproj.transform(x,y,z)
    return E,N,h
 
# Load a TOML file
with open('cors4_GNSS1.toml', 'r') as f:
    config = toml.load(f)

# make in

#reference
ref = "SBKKGNSS01_precise"
dfr = pd.DataFrame(config[ref])
ENUr= xyz2utm(dfr.x.dd,dfr.y.dd,dfr.z.dd,"47")

#compare with
Name = []
dE = []
dN = []
dU = []
#for i in ["BPLE_GNSS1","PKKT_GNSS1"]: #debug
for i in config.keys():
    if i == ref: 
        continue
    else:
        df = pd.DataFrame(config[i])
        ENU = xyz2utm(df.x.dd,df.y.dd,df.z.dd,"47")
        Name.append(i)
        dE.append(ENU[0] - ENUr[0])
        dN.append(ENU[1] - ENUr[1])
        dU.append(ENU[2] - ENUr[2])

thisdict = {"Name":Name,"dE":dE,"dN":dN,"dU":dU}
#import pdb; pdb.set_trace()

#add this for plot only
thisdict2 = {
"Name" : [ref],
"dE"   : [0],
"dN"   : [0],
"dU"   : [0]}
#make out
df1 = pd.DataFrame(thisdict)
df2 = pd.DataFrame(thisdict2)
#import pdb; pdb.set_trace()
df3 = pd.concat([df2, df1], axis = 0)
#import pdb; pdb.set_trace()
print(df3.to_markdown(floatfmt=(".3f"),showindex=False))
#import pdb; pdb.set_trace()

#plot()


import pdb; pdb.set_trace()
