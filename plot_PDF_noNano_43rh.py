# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 11:58:40 2016

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys

#import the target file
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')
import noNano_50rh as targetFile

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

''' indicate the range of data plotted'''
data_files_1=targetFile.Readfile()[1]

interm_syn = [np.array(data_files_1[i].readlines()) for i in range (np.shape(data_files_1)[0])]

''' remember to set start line number here '''
interm1_syn =[ [str.split(interm_syn[j][i]) for i in range(141,np.shape(interm_syn[j])[0])] for j in range (np.shape(data_files_1)[0])]

interm2_syn= [[[float(interm1_syn[k][j][i]) for j in range (0,np.shape(interm1_syn[k])[0])]for i in range (2) ] for k in range (np.shape(data_files_1)[0])]

name_of_the_plot=['%s h'%(array(targetFile.Data()[0][i])) for i in range (shape(data_files_1)[0])]

#find local max to denote the peak position
local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(data_files_1)[0])]

peakPosition=[interm2_syn[0][0][local_max[0][4]],interm2_syn[0][0][local_max[0][5]], interm2_syn[0][0][local_max[0][6]], 2.8 ,interm2_syn[0][0][local_max[0][7]], interm2_syn[0][0][local_max[0][8]],3.9,interm2_syn[0][0][local_max[0][9]],interm2_syn[0][0][local_max[0][10]]]

nameOfthePeak = ['Si-O','Mg-O','Ca-O', 'O-O' ,'Si-T','Ca-Si','Ca-Ca','Si-O','Ca-O']
''

# do normalization
normalization_factor = [interm2_syn[0][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]


close("all")
f, ax = subplots()

plot_range = arange(0, len(name_of_the_plot), 5)
[ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*normalization_factor[i],
    alpha=1,label='%s'%(name_of_the_plot[i])) for i in plot_range]

#add vertical lines at the local max
lengthOftheLine = [0.92,0.8,0.85,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
[ax.axvline(peakPosition[i],ymin=0,ymax=lengthOftheLine[i],color='k') for i in range (np.shape(peakPosition)[0])]

#add names of the peaks
position_y = [3,1,2.5, 2 , 2.7,2.7,2,2.7,3]
[text(peakPosition[i],position_y[i], nameOfthePeak[i],horizontalalignment='center',fontsize=14) for i in range  (np.shape(peakPosition)[0])]

#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=10)
grid(axis='x')

xlim (0,6)
ylim(-3,4)
#ax.axhline(y=0, color='k')
xlabel(r'r ($\AA$)')
ylabel('G(r)')
legend(loc=0, fontsize =14,ncol=1,columnspacing=0, labelspacing=0.1)
subplots_adjust(left=0.1, bottom=0.11, right=0.9, top=0.9)
f.show()

#   f.savefig('/Users/hty/desktop/%s.eps'%('pdf noNano 50rh'))
