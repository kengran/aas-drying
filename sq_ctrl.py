# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:12:36 2016

@author: hty
"""

import sys
sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd
from numpy import *
from matplotlib.pyplot import *
import peak_assign_sq as pa

import nano_ctrl as n43

input_name = n43.Readfile()[1]
new_name = [input_name[i][:-3]+'.sq' for i in range (shape (input_name)[0])]
data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]


''' indicate the range of data plotted'''
y_val = gd.curve(data_files_1,141)


close("all")
f, ax = subplots()
#==============================================================================
# names=['%s'%(i) for i in range (shape(data_files_1)[0])]
#==============================================================================
# plot_range = range (shape(y_val)[0])
plot_range = n43.Readfile()[2]
[ax.plot(y_val[i][0],y_val[i][1],label='%s h'%(n43.x_value() [i])) for i in plot_range]
legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
xlabel(r'Q ($\AA^{-1}$)')
ylabel('S(Q)')
xlim(0.5,6)
ylim(-0.5, 2.7)

#add vertical lines at the local max
# num_of_peak_showed = arange(9)
num_of_peak_showed = arange(shape(pa.find_local_max(y_val)[1])[0])

min_of_the_line = [0, 0.08, 0.75, 0.55, 0.3, 0.5, 0.45, 0.45, 0.8,0.8, 0.8, 0.8]
max_of_the_line = array(min_of_the_line)+0.2

[ax.axvline(pa.find_local_max(y_val)[1][i],ymin=min_of_the_line[i],ymax=max_of_the_line[i],color='k') for i in num_of_peak_showed]

#add names of the peaks
position_y = [0.2, 0.5, 2.6 , 2, 1.2, 1.8, 1.7, 1.7,1.5, 2, 2, 2]
[text(pa.find_local_max(y_val)[1][i],position_y[i], pa.name_of_the_peak(y_val)[i],horizontalalignment='center',fontsize=14) for i in num_of_peak_showed]


f.show()

#==============================================================================
# text(5,0,'new chi files')
#==============================================================================

#   f.savefig('/Users/hty/desktop/sq %s.pdf'%(n43.__name__))
