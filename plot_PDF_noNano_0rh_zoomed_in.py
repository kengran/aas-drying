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
import noNano_rh0 as targetFile

#change font properties of the plots
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

''' indicate the range of data plotted'''
data_files_1=targetFile.Readfile()[1][0::10]
name_of_the_plot=['%s h'%(array(targetFile.Data()[0][0::10][i])) for i in range (shape(data_files_1)[0])]

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

nameOfthePeak = ['Si-O','Al/Mg-O','Ca-O','O-O','Si-T','Ca-Si','Ca-Ca','Si-O','Ca-O']
''

# do normalization
normalization_factor = [interm2_syn[0][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]


plt.close("all")
f, ax = plt.subplots(figsize = (2.5,3))

[ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*normalization_factor[i], alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]



#add vertical lines at the local max
lengthOftheLine = [0.92,0.8,0.85,0.8,0.9 ,0.9 ,0.8,0.8,0.9]
[ax.axvline(peakPosition[i],ymin=0,ymax=lengthOftheLine[i],color='k') for i in range (np.shape(peakPosition)[0])]

#add names of the peaks
position_y = [3.5 ,1, 1.7 ,2.5, 1.2 , 2.3 , 0.5 ,2.7, 0.66]
[plt.text(peakPosition[i],position_y[i], nameOfthePeak[i],horizontalalignment='center',fontsize=14) for i in range  (np.shape(peakPosition)[0])]

#increase the freq of the ticks
plt.locator_params(axis='x',tight=True,nbins=10)
plt.grid(axis='x')
#ax.axhline(y=0, color='k')
#plt.legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)

   
#==============================================================================
# plt.xlim (3.5, 3.8)
# ylim(1,2.5)
# plt.xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1]+0.1 , 0.2))
# plt.yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+0.1 , 0.4))
# plt.subplots_adjust(left=0.25, bottom=0.1, right=0.9, top=0.9)
#  #   f.savefig('/Users/hty/desktop/%s.eps'%('pdf noNano 0rh ca-si'))
#==============================================================================

#==============================================================================
# 
# plt.xlim (4.4,4.6)
# ylim(0.2,0.7)
# plt.xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1]+0.1 , 0.1))
# plt.yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+0.1 , 0.2))
# plt.subplots_adjust(left=0.17, bottom=0.1, right=0.9, top=0.9)
# #   f.savefig('/Users/hty/desktop/%s.eps'%('pdf noNano 0rh ca-o-2'))
#==============================================================================

#==============================================================================
# 
# plt.xlim (2.2,2.5)
# ylim(0.8, 1.8)
# plt.xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1]+0.1 , 0.1))
# plt.yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+0.1 , 0.2))
# plt.subplots_adjust(left=0.17, bottom=0.1, right=0.9, top=0.9)
# #   f.savefig('/Users/hty/desktop/%s.eps'%('pdf noNano 0rh ca-o-1'))
#==============================================================================

#==============================================================================
# 
# plt.xlim (3.7,4.1)
# ylim(0, 0.6)
# plt.xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1]+0.1 , 0.1))
# plt.yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+0.1 , 0.2))
# plt.subplots_adjust(left=0.17, bottom=0.1, right=0.9, top=0.9)
# #   f.savefig('/Users/hty/desktop/%s.eps'%('pdf noNano 0rh ca-ca'))
#==============================================================================


plt.xlim (2.9,3.2)
ylim(0,1.4)
plt.xticks(np.arange(ax.get_xlim()[0], ax.get_xlim()[1]+0.1 , 0.2))
plt.yticks(np.arange(ax.get_ylim()[0], ax.get_ylim()[1]+0.1 , 0.4))
plt.subplots_adjust(left=0.25, bottom=0.1, right=0.9, top=0.9)
#   f.savefig('/Users/hty/desktop/%s.eps'%('pdf noNano 0rh si-t'))


