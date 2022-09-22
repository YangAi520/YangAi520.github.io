import os
import random
fp=open('batch.csv','w')
mylink=[]

mylink1='https://YangAi520.github.io/Phase_model/MOS/A/'
mylink2='https://YangAi520.github.io/Phase_model/MOS/B/'
mylink3='https://YangAi520.github.io/Phase_model/MOS/C/'
mylink4='https://YangAi520.github.io/Phase_model/MOS/D/'
mylink5='https://YangAi520.github.io/Phase_model/MOS/E/'
mylink6='https://YangAi520.github.io/Phase_model/MOS/F/'
mylink7='https://YangAi520.github.io/Phase_model/MOS/G/'

mylink.append(mylink1)
mylink.append(mylink2)
mylink.append(mylink3)
mylink.append(mylink4)
mylink.append(mylink5)
mylink.append(mylink6)
mylink.append(mylink7)

for i in range(20):
	for j in range(7):
		fp.write('link'+str(i*10+j+1)+',')
fp.write('\n')

link_number_list=[0,1,2,3,4,5,6]

for i in xrange(20):
	if i<9:
		name='0'+str(i+1)+'.wav'
	else:
		name=str(i+1)+'.wav'

	random.shuffle(link_number_list)
	for j in xrange(7):
		fp.write(mylink[link_number_list[j]]+mylink[link_number_list[j]].split('/')[-2]+'_'+name+',')

fp.write('\n')
fp.close()