## idea ##
#delete the eigth-figure calibration imu
##########
import pyogrio
import fiona
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString

name = "MX9_v30_OKRK.csv"
df = pd.read_csv(name)
#Open QGIS and choose fid
#จำนวนบรรทัดเท่ากันในไฟล์ csv น่าจะ sample เท่ากัน
#gnss01 SBKK start 4514 end 9241
#PKKT  start 4507  end 9237 #CORS ที่เหลือน่าจใช้เหมือนกัน
####AU_20####
#บรรทัดล่างนี้ไว้ใช้สำหรับ GNSS01 SBKK 
#rslt_df = df[(df["fid"] >= 4514) & (df["fid"] <= 9241)]
#บรรทัดล่างนี้ไว้ใช้สำหรับ CORS ที่เหลือ
#rslt_df = df[(df["fid"] >= 4507) & (df["fid"] <= 9237)]
####AU_20####

####MX9####
#บรรทัดล่างนี้ไว้ใช้สำหรับ ทุก base เนื่องจาก sample คล้ายกัน
rslt_df = df[(df["fid"] >= 350) & (df["fid"] <= 8659)]

####MX9####
gdf_p = gpd.GeoDataFrame(rslt_df,geometry = gpd.points_from_xy(rslt_df.Longitude,rslt_df.Latitude),crs = "EPSG:4326")
geometry = [Point(xy) for xy in zip(rslt_df.Longitude,rslt_df.Latitude)] 
geometry.append(geometry[0]) # ให้เส้นวนกลับมาทีเดิม
#import pdb; pdb.set_trace()
Line = LineString(geometry)
gdf_L = gpd.GeoDataFrame(geometry = [Line],crs = "EPSG:4326")
gdf_p.to_file("8gone"+name[:-4]+".gpkg", layer= "pnt" + name[:-4], driver = "GPKG")
gdf_L.to_file("8gone"+name[:-4]+".gpkg", layer= "line"+ name[:-4], driver = "GPKG")
import pdb; pdb.set_trace()