# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 14:28:18 2023

@author: sriva
"""

import shapely
from shapely import *
from shapely.geometry import Polygon
import numpy as np

path1 = r"C:\Users\sriva\OneDrive\Desktop\PSG COLLEGE\PLACEMENTS\KLA SDE\Milestone_Input\Milestone_Input\Milestone 7\Source.txt"
path2 = r"C:\Users\sriva\OneDrive\Desktop\PSG COLLEGE\PLACEMENTS\KLA SDE\Milestone_Input\Milestone_Input\Milestone 7\POI.txt"

#import difflib
 
coordinates = []
layer = []
 
with open(path2,'r') as file2:
    data = file2.readlines()
    for line in data:
        if 'layer' in line:
            word = line.split()
            layer.append(word[1])
        if 'xy' in line:
            print(data)
            word = line.split()
            coordinates.append(word.copy())
            
number_of_points = 0
print(layer)


for coord in coordinates:
    coord.remove("xy")
    number_of_points = int(coord[0])
    coord.remove(coord[0])

print(coordinates)

#count = 0

'''with open(path1,'r') as file1:
    data = file1.readlines()
    for line in data:
        count += 1
        if str(coordinates) in line[2:]:
            print(line[2:])'''
          
x_coord = []
y_coord = []

for coord in coordinates:
    for i in range(0,len(coord),2):
        x_coord.append(int(coord[i]))
        y_coord.append(int(coord[i+1]))
    
print(x_coord)
    

polygon_coordinates = list(zip(x_coord,y_coord))
print('Polygon coordinates:',polygon_coordinates)

new_poly_coordinates = list()

#temp = list()
for i in range(0,len(polygon_coordinates),number_of_points):
    new_poly_coordinates.append(polygon_coordinates[i:i+number_of_points])
    
print(new_poly_coordinates)

#p1 = polygon_coordinates.copy()

f1 = open('Milestone7_output.txt','w')

poly_area = []

for points in new_poly_coordinates:
    poly = Polygon(points)
    poly_area.append(poly.area)

print(poly_area)

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
            if p1.area in poly_area:
                f1.write('boundary\n')
                f1.write('layer 1\n')
                f1.write('datatype 0\n')
                f1.write(line)
                f1.write('endel\n')
            polygon_coordinates.clear()
                
f1.close()
