# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:00:08 2015

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys

#import the target file
sys.path.append('/Users/hty/Google Drive/research/aas drying/APS exp/chi_files')
import nano_rh0 as n0
import noNano_rh0 as nn0

#change font properties of the plots
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

''' indicate the range of data plotted'''
data_files_1=[n0.Readfile()[1][0], nn0.Readfile()[1][0]]

name_of_the_plot=['nano', 'no nano']

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

nameOfthePeak = ['T-O','Mg-O','Ca-O','O-O','Si-T','Ca-Si','Ca-Ca','T-O','Ca-O']
''

# do normalization
normalization_factor = [interm2_syn[0][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]


close("all")
f, ax = subplots()

'''with normalization'''
[ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*normalization_factor[i], alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]

'''no normalization'''
#==============================================================================
# [ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1]), alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]
#==============================================================================


#add vertical lines at the local max
lengthOftheLine = [0.83,0.55, 0.75 ,0.75,0.8,0.8,0.8,0.8,0.8,0.8]
[ax.axvline(peakPosition[i],ymin=0,ymax=lengthOftheLine[i],color='k') for i in range (np.shape(peakPosition)[0])]

#add names of the peaks
position_y = [3,1,2.5, 2.3, 2.7,2.7,2,2.7,3]
[text(peakPosition[i],position_y[i], nameOfthePeak[i],horizontalalignment='center',fontsize=14) for i in range  (np.shape(peakPosition)[0])]

#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=10)
grid(axis='x')
xlim (0,6)
ylim (-3,4)
#ax.axhline(y=0, color='k')
xlabel(r'r ($\AA$)')
ylabel('G(r)')
legend(loc=4, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1, title = '0h (start of drying)')
subplots_adjust(left=0.1, bottom=0.11, right=0.9, top=0.9)
f.show()
#   f.savefig('/Users/hty/desktop/%s.pdf'%('pdf compare 0rh at the start of drying'))
