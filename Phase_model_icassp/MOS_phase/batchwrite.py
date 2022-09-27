import os
import random
fp=open('batch.csv','w')
mylink=[]

mylink1='https://YangAi520.github.io/Phase_model_icassp/MOS_phase/A/'
mylink2='https://YangAi520.github.io/Phase_model_icassp/MOS_phase/B/'
mylink3='https://YangAi520.github.io/Phase_model_icassp/MOS_phase/C/'
mylink4='https://YangAi520.github.io/Phase_model_icassp/MOS_phase/D/'
mylink5='https://YangAi520.github.io/Phase_model_icassp/MOS_phase/E/'

mylink.append(mylink1)
mylink.append(mylink2)
mylink.append(mylink3)
mylink.append(mylink4)
mylink.append(mylink5)

for i in range(20):
	for j in range(5):
		fp.write('link'+str(i*10+j+1)+',')
fp.write('\n')

link_number_list=[0,1,2,3,4]

for i in xrange(20):
	if i<9:
		name='0'+str(i+1)+'.wav'
	else:
		name=str(i+1)+'.wav'

	random.shuffle(link_number_list)
	for j in xrange(5):
		fp.write(mylink[link_number_list[j]]+mylink[link_number_list[j]].split('/')[-2]+'_'+name+',')

fp.write('\n')
fp.close()