# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:29:46 2023

@author: sriva
"""

import shapely 

import shapely
from shapely import *
from shapely.geometry import Polygon
import numpy as np

path1 = r"C:\Users\sriva\OneDrive\Desktop\PSG COLLEGE\PLACEMENTS\KLA SDE\Milestone_Input\Milestone_Input\Milestone 3\Source.txt"
path2 = r"C:\Users\sriva\OneDrive\Desktop\PSG COLLEGE\PLACEMENTS\KLA SDE\Milestone_Input\Milestone_Input\Milestone 3\POI.txt"

#import difflib
 
coordinates = []
 
with open(path2,'r') as file2:
    data = file2.readlines()
    for line in data:
        if 'xy' in line:
            print(data)
            word = line.split()
            coordinates = word.copy()
            

coordinates.remove("xy")
coordinates.remove(coordinates[0])
print(coordinates)

count = 0

'''with open(path1,'r') as file1:
    data = file1.readlines()
    for line in data:
        count += 1
        if str(coordinates) in line[2:]:
            print(line[2:])'''
            
x_coord = []
y_coord = []

for i in range(0,len(coordinates),2):
    x_coord.append(int(coordinates[i]))
    y_coord.append(int(coordinates[i+1]))
    
print(x_coord)
    

polygon_coordinates = list(zip(x_coord,y_coord))


print(polygon_coordinates)

#p1 = polygon_coordinates.copy()

f1 = open('Milestone3_output.txt','w')
poly = Polygon(polygon_coordinates)
poly_area = poly.area

with open(path1,'r') as file1:
    data = file1.readlines()
    for line in data:
        if 'xy' in line:
            x = []
            y = []
            word = line.split()
            coordinates = word.copy()
            coordinates.remove('xy')
            coordinates.remove(coordinates[0])
            for i in range(0,len(coordinates),2):
                x.append(int(coordinates[i]))
                y.append(int(coordinates[i+1]))
            polygon_coordinates = list(zip(x,y))
            p1 = Polygon(polygon_coordinates)
            if poly_area==p1.area:
                f1.write('boundary\n')
                f1.write('layer 1\n')
                f1.write('datatype 0\n')
                f1.write(line)
                f1.write('endel\n')
            polygon_coordinates.clear()
                
f1.close()