import os
import numpy as np
import shutil

file_list=['p232_011.wav', 'p232_021.wav', 'p232_045.wav', 'p232_049.wav', 'p232_050.wav', 'p232_071.wav', 'p232_092.wav', 'p232_094.wav', 'p232_096.wav', 'p232_110.wav','p257_003.wav', 'p257_008.wav', 'p257_011.wav', 'p257_013.wav', 'p257_015.wav', 'p257_023.wav', 'p257_026.wav', 'p257_042.wav', 'p257_050.wav', 'p257_055.wav']

A_source_dir='./Natural/'
B_source_dir='./Phase_model/'
C_source_dir='./RAAR100/'
D_source_dir='./GL100/'
E_source_dir='./NN+GL100/'
F_source_dir='./RAAR13/'
G_source_dir='./GL22/'

A_target_dir='./A/'
B_target_dir='./B/'
C_target_dir='./C/'
D_target_dir='./D/'
E_target_dir='./E/'
F_target_dir='./F/'
G_target_dir='./G/'

for i in xrange(len(file_list)):
	if i<9:
		name='0'+str(i+1)
	else:
		name=str(i+1)

	shutil.copyfile(A_source_dir+file_list[i],A_target_dir+'A_'+name+'.wav')
	shutil.copyfile(B_source_dir+file_list[i],B_target_dir+'B_'+name+'.wav')
	shutil.copyfile(C_source_dir+file_list[i],C_target_dir+'C_'+name+'.wav')
	shutil.copyfile(D_source_dir+file_list[i],D_target_dir+'D_'+name+'.wav')
	shutil.copyfile(E_source_dir+file_list[i],E_target_dir+'E_'+name+'.wav')
	shutil.copyfile(F_source_dir+file_list[i],F_target_dir+'F_'+name+'.wav')
	shutil.copyfile(G_source_dir+file_list[i],G_target_dir+'G_'+name+'.wav')
