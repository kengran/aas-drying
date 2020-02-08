# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:00:08 2015

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys

#import the target file
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')
import noNano_50rh as targetFile

#change font properties of the plots
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

''' indicate the range of data plotted'''
i_range = [0,1,5,-1]
data_files_1=[targetFile.Readfile()[1][i] for i in i_range]

name_of_the_plot=['%s h'%(array(targetFile.Data()[0][i])) for i in i_range]

interm_syn = [np.array(data_files_1[i].readlines()) for i in range (np.shape(data_files_1)[0])]

''' remember to set start line number here '''
interm1_syn =[ [str.split(interm_syn[j][i]) for i in range(141,np.shape(interm_syn[j])[0])] for j in range (np.shape(data_files_1)[0])]

interm2_syn= [[[float(interm1_syn[k][j][i]) for j in range (0,np.shape(interm1_syn[k])[0])]for i in range (2) ] for k in range (np.shape(data_files_1)[0])]

# check if there are non-numbers
'''
upper_limit=np.empty(np.shape(interm1)[0],dtype=int)
for i in range (np.shape(interm1)[0]):
    for j in range (0,np.shape(interm1[i])[0]):
        try:
            float(interm1[i][j][0])
        except ValueError:
            print j
            upper_limit[i] = j
            break
'''



#find local max to denote the peak position
local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(data_files_1)[0])]

peakPosition=[interm2_syn[0][0][local_max[0][4]],interm2_syn[0][0][local_max[0][5]], interm2_syn[0][0][local_max[0][6]],2.8,interm2_syn[0][0][local_max[0][7]], interm2_syn[0][0][local_max[0][8]],3.9,interm2_syn[0][0][local_max[0][9]],interm2_syn[0][0][local_max[0][10]]]

nameOfthePeak = ['Si-O','Al/Mg-O','Ca-O','O-O','Si-Si','Ca-Si','Ca-Ca','Si-O','Ca-O']
''

# do normalization
normalization_factor = [interm2_syn[-1][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]

normalization_factor_2 = [interm2_syn[0][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]


close("all")
f, ax = subplots(figsize=(8,8))

[ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*normalization_factor[i], alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]


#difference plots
[ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])*normalization_factor_2[i]-array(interm2_syn[0][1]))*5 + 5, alpha=1,label='%s - 0h'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]

[ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])-array(interm2_syn[0][1]))*5 + 10, '--', linewidth=1.5,alpha=1,label='%s - 0h no norm.'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]


#add vertical lines at the local max
lengthOftheLine = [0.92,0.8,0.85,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
[ax.axvline(peakPosition[i],ymin=0,ymax=lengthOftheLine[i],color='k') for i in range (np.shape(peakPosition)[0])]

#add names of the peaks
position_y = [4,1,2.5 ,2.5, 3, 3,2,2.7,3.5]
[text(peakPosition[i],position_y[i], nameOfthePeak[i],horizontalalignment='center',fontsize=14) for i in range  (np.shape(peakPosition)[0])]

#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=10)
grid(axis='x')
xlim (0.8,6)
ylim (-4,16)
#ax.axhline(y=0, color='k')
xlabel(r'r ($\AA$)')
ylabel('G(r)')
legend(loc=2, fontsize ='small',ncol=3,columnspacing=0.5, labelspacing=0)

text(5,7,'x 5')
show()

#   f.savefig('/Users/hty/desktop/%s.eps'%('diff pdf noNano 43rh x5'))
