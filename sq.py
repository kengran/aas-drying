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
sys.path.append('/Users/hty/Google Drive/research/APS exp/py_files')
import peak_assign_sq as pa
import sub_subplot as ssp

# import target file
import noNano_rh0 as target

# input_name = target.read_reciprocal_space_files('.sq')[2]
# new_name = [input_name[i][:-3]+'.sq' for i in range (shape (input_name)[0])]
# data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]
''' indicate the range of data plotted'''
data_interval = 2

data_files_1 = target.read_reciprocal_space_files_d95('.sq')[0]
data_label = target.read_reciprocal_space_files_d95('.sq')[1][0::data_interval]

xy = gd.curve(data_files_1,141) [0::data_interval]


close("all")
f, ax = subplots()
# remember to update the range of the label****
[ax.plot(xy[i][0],xy[i][1],label='%s h'%(data_label[i])) for i in range (shape(xy)[0])]
legend(loc=4, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
xlabel(r'Q ($\AA^{-1}$)')
ylabel('S(Q)')

#==============================================================================
# text(5,0,'new chi files')
#==============================================================================
xlim(0,6)
ylim(-1,2.6)

#add vertical lines at the local max
# num_of_peak_showed = arange(9)
num_of_peak_showed = arange(shape(pa.peak_pos_0rh(xy, target.__name__))[0])

max_of_the_line = array(pa.vline_pos(target.__name__))+0.2

[axvline(pa.peak_pos_0rh(xy, target.__name__)[i],ymin=pa.vline_pos(target.__name__)[i],ymax=max_of_the_line[i],color='k') for i in num_of_peak_showed]

#add names of the peaks
[text(pa.peak_pos_0rh(xy, target.__name__)[i],pa.label_pos(target.__name__)[i], pa.name_of_the_peak(xy)[i],horizontalalignment='center',fontsize=14) for i in num_of_peak_showed]

#creating a sub-subplot
rect = [0.08,0.55,0.2,0.4]
ax_sub = ssp.add_subplot_axes(ax,rect)
[plot(xy[i][0],xy[i][1],label='%s h'%(data_label[i])) for i in range (shape(xy)[0])]
xlim(0.3, 0.6)
ylim(-0.4, 0.6)
xticks(arange(0.3,0.61,0.1))
# yticks(arange(0.0,2.01,1.0))
yFormatter = FormatStrFormatter('%.1f')
ax_sub.yaxis.set_major_formatter(yFormatter)
# ax_sub.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

f.show()

#   f.savefig('/Users/hty/desktop/sq %s.pdf'%(target.__name__))
