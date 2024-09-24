import pyogrio
import fiona
import geopandas as gpd
from shapely import LineString,hausdorff_distance,distance

class find_dist:
  def __init__(self,ref,r_layer):# ex. ref : "8gonev30_GNSS01.gpkg" r_layer : "linev30_GNSS01"
    self.ref = ref
    self.r_layer = r_layer
  def makedist(self,cp,c_layer):
      #lat lon
      ref_trj = gpd.read_file(self.ref, layer = self.r_layer) 
      compare_trj = gpd.read_file(cp, layer = c_layer)
      
      #to EN
      ref_trj = ref_trj.to_crs(32647)
      compare_trj = compare_trj.to_crs(32647)
      
      dist = distance(ref_trj.geometry.iloc[0], compare_trj.geometry.iloc[0])
      h_dist = hausdorff_distance(ref_trj.geometry.iloc[0], compare_trj.geometry.iloc[0])
      print("=======================")
      print(f"reference line = {self.ref}")
      print(f"compare line = {cp}")
      print(f"euclidean_distance = {dist} m")
      print(f"hausdorff_distance = {h_dist} m")
      print("=======================")
      #import pdb;pdb.set_trace()
        
AU20 = find_dist("8goneAU20_v30_GNSS01.gpkg","linev30_GNSS01")
AU20.makedist("8goneAU20_v30_SBKK.gpkg","lineAU20_v30_SBKK")
AU20.makedist("8goneAU20_v30_PKKT.gpkg","lineAU20_v30_PKKT")
AU20.makedist("8goneAU20_v30_BPLE.gpkg","lineAU20_v30_BPLE")
AU20.makedist("8goneAU20_v30_OKRK.gpkg","lineAU20_v30_OKRK")

MX9 = find_dist("8goneMX9_v30_GNSS02.gpkg","lineMX9_v30_GNSS02")
MX9.makedist("8goneMX9_v30_SBKK.gpkg","lineMX9_v30_SBKK")
MX9.makedist("8goneMX9_v30_PKKT.gpkg","lineMX9_v30_PKKT")
MX9.makedist("8goneMX9_v30_BPLE.gpkg","lineMX9_v30_BPLE")
MX9.makedist("8goneMX9_v30_OKRK.gpkg","lineMX9_v30_OKRK")

import pdb; pdb.set_trace() 

#hard code
#latlon
#ref_trj = gpd.read_file("8gonev30_GNSS01.gpkg",        layer = "linev30_GNSS01")
#compare_trj = gpd.read_file("8goneAU20_v30_SBKK.gpkg", layer = "lineAU20_v30_SBKK")
#compare_trj = gpd.read_file("8goneAU20_v30_PKKT.gpkg", layer = "lineAU20_v30_PKKT")
#compare_trj = gpd.read_file("8goneAU20_v30_BPLE.gpkg", layer = "lineAU20_v30_BPLE")
#compare_trj = gpd.read_file("8goneAU20_v30_OKRK.gpkg", layer = "lineAU20_v30_OKRK")


# #EN
# ref_trj = ref_trj.to_crs(32647)
# compare_trj = compare_trj.to_crs(32647)


# dist = distance(ref_trj.geometry.iloc[0], compare_trj.geometry.iloc[0])
# h_dist = hausdorff_distance(ref_trj.geometry.iloc[0], compare_trj.geometry.iloc[0])  
# print(f"euclidean_distance = {dist} m")
# print(f"hausdorff_distance = {h_dist} m")

#test dist and h_dist
# L1 = LineString([(0, 1), (1, 1)])
# #L2 = LineString([(0, 0), (1, 0)])
# L2 = LineString([(1, 1), (0, 0)])
# dist = distance(L1, L2)
# h_dist = hausdorff_distance(L1, L2)
# import pdb; pdb.set_trace()