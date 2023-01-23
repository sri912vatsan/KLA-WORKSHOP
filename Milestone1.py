# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 08:52:20 2023

@author: sriva
"""


path = r"C:\Users\sriva\OneDrive\Desktop\PSG COLLEGE\PLACEMENTS\KLA SDE\Milestone_Input\Milestone_Input\Milestone1\Format_Source.txt"

count = 0

file1 = open("Milestone1_output.txt","w")

with open(path,'r') as file:
    data = file.readlines()
    for line in data:
        if count==4:
            break
        if 'boundary' in line:
            count += 1
        if count>0:
            file1.write(line)
        if 'endel' in line:
            count += 1
       
        
file1.close()
            
        
        
        
        