# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:32:22 2015

@author: user
"""
import os
import random
fp=open('batch.csv','w')
mylink=[]
system=[]
mylink1='https://YangAi520.github.io/Phase_model/ABX_main/A/'
mylink2='https://YangAi520.github.io/Phase_model/ABX_main/B/'
mylink.append(mylink1)
mylink.append(mylink2)
system1=sorted(os.listdir('./A/'))
system2=sorted(os.listdir('./B/'))
system.append(system1)
system.append(system2)
for i in range(40):
    fp.write('link'+str(i+1)+',')
fp.write('\n')
system_list=[0,1]
for i in xrange(20):
	random.shuffle(system_list)
	for j in xrange(len(system_list)):
		if i==19 and j==len(system_list)-1:
			fp.write(mylink[system_list[j]]+system[system_list[j]][i]+'\n')
		else:
			fp.write(mylink[system_list[j]]+system[system_list[j]][i]+',')

fp.close()
