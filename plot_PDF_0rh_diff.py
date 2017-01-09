# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:00:08 2015

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys

#import the target file
import noNano_rh0 as target
import peak_assign as pn


''' indicate the range of data plotted'''
data_interval = 9
data_files_1=target.Readfile()[1][0::data_interval]
name_of_the_plot=['%s h'%(array(target.peaks()[0][0::data_interval][i])) for i in range (shape(data_files_1)[0])]

interm_syn = [np.array(data_files_1[i].readlines()) for i in range (np.shape(data_files_1)[0])]

''' remember to set start line number here '''
interm1_syn =[ [str.split(interm_syn[j][i]) for i in range(141,np.shape(interm_syn[j])[0])] for j in range (np.shape(data_files_1)[0])]

interm2_syn= [[[float(interm1_syn[k][j][i]) for j in range (0,np.shape(interm1_syn[k])[0])]for i in range (2) ] for k in range (np.shape(data_files_1)[0])]

#find local max to denote the peak position
local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(data_files_1)[0])]

local_min = [(diff(sign(diff((np.array(interm2_syn[i][1])-array(interm2_syn[0][1]))))) > 0).nonzero()[0] + 1 for i in range (shape(data_files_1)[0]-1)]

# mininums
peakPosition_min=[interm2_syn[0][0][local_min[1][7]]]

peakPosition=[interm2_syn[0][0][local_max[0][4]],interm2_syn[0][0][local_max[0][5]], interm2_syn[0][0][local_max[0][6]], 2.8 ,interm2_syn[0][0][local_max[0][7]], interm2_syn[0][0][local_max[0][8]],3.9,interm2_syn[0][0][local_max[0][9]],interm2_syn[0][0][local_max[0][10]]]

nameOfthePeak = ['Si-O','Al/Mg-O','Ca-O','O-O','Si-Si','Ca-Si','Ca-Ca','Si-O','Ca-O']
''

# do normalization
norm_factor_wrt_last_curve = [interm2_syn[-1][1][pn.find_local_max(interm2_syn)[0][0][4]]/interm2_syn[i][1][pn.find_local_max(interm2_syn)[0][i][4]] for i in range (shape(data_files_1)[0])]

norm_factor_wrt_first_curve = [interm2_syn[0][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]


# set style of the plot
style.use('classic')

#change font properties of the plots
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

# start plotting
close("all")
f, ax = subplots(figsize=(9,7))

[ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i], alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]

#difference plots
[ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i]-array(interm2_syn[0][1]))*5 + 6, '--', alpha=1,label='%s - %s'%(name_of_the_plot[i], name_of_the_plot[0])) for i in range (np.shape(data_files_1)[0])]

# [ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])-array(interm2_syn[0][1]))*5 + 10, '--', linewidth=1.5,alpha=1,label='%s - 0h no norm.'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]


#add vertical lines at the local max

# num_of_peak_showed = [0,2,5]
num_of_peak_showed = arange(9)
num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

lengthOftheLine = [0.92,0.8,0.85,0.8,0.8,0.8,0.8,0.8,0.8,0.8, 0.8, 0.8]
[ax.axvline(pn.find_local_max(interm2_syn)[1][i],ymin=0,ymax=lengthOftheLine[i],color='k') for i in num_of_peak_showed]

#add names of the peaks
position_y = [3.5, 1, 2.5 , 2.5, 3, 3.5, 2,2.7,3.5, 3, 3, 3]
[text(pn.find_local_max(interm2_syn)[1][i],position_y[i], pn.name_of_the_peak(interm2_syn)[i],horizontalalignment='center',fontsize=14) for i in num_of_peak_showed]


#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=20)
grid(axis='x')

xlim (0.8,6)
ylim (-4,9)
#ax.axhline(y=0, color='k')
xlabel(r'r ($\AA$)')
ylabel('G(r)')
legend(loc=0, fontsize ='small',ncol=2,columnspacing=0.5, labelspacing=0, frameon = True)

text(5,7.5,'x 5')
draw()
f.show()


#   f.savefig('/Users/hty/desktop/diff pdf %s.pdf'%(target.__name__))
