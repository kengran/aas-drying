# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 11:12:36 2016

@author: hty
"""
import matplotlib
matplotlib.use('Qt5Agg')
import sys
sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd
from numpy import *
from matplotlib.pyplot import *
sys.path.append('/Users/hty/Google Drive/research/APS exp/py_files')
import peak_assign_recip as pa
import sub_subplot as ssp

# import target file
import noNano_rh0 as target

import plot_spec as S

reload(pa)
reload(target)

dtype = '.sq'

''' indicate the range of data plotted'''
if target.__name__ == 'noNano_rh0':
    data_interval = 2
    data_files_1 = target.read_reciprocal_space_files_d95(dtype)[0][0::data_interval]
    data_label = target.read_reciprocal_space_files_d95(dtype)[1][0::data_interval]
elif target.__name__ == 'noNano_rh43':
    data_interval = 1
    which_files = target.read_file_with_low_angle_info
    data_files_1 = target.read_reciprocal_space_files(dtype, which_files)[0][0::data_interval]
    data_label = target.read_reciprocal_space_files(dtype, which_files)[1][0::data_interval]
elif target.__name__ == 'nano_rh43':
    data_interval = 3
    which_files = target.read_file_with_low_angle_info
    data_files_1 = target.read_reciprocal_space_files(dtype, which_files)[0][0::data_interval]
    data_label = target.read_reciprocal_space_files(dtype, which_files)[1][0::data_interval]
else:
    data_interval = 7
    data_files_1 = target.read_reciprocal_space_files(dtype)[0][0::data_interval]
    data_label = target.read_reciprocal_space_files(dtype)[1][0::data_interval]

# automatically select the plotting config by input
if target.__name__ == 'noNano_rh43':
    inset_x_min = 0.2
    inset_y_max = 0.7
else:
    inset_x_min = 0.3
    inset_y_max = 0.6



xy = gd.curve(data_files_1,141)


# set style of the plot
style.use('classic')

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)


# close("all")
f, ax = subplots(figsize=(6,4.5))
subplots_adjust(left=0.19, bottom=0.17)

# remember to update the range of the label****
[ax.plot(
    xy[i][0],xy[i][1],
    c = S.Spec.line_color[i+S.Spec.interval-4],
    linestyle=S.Spec.line_type[i%3],
    linewidth=S.Spec.line_width[i],
    label='%s h'%(data_label[i])) for i in range (shape(xy)[0])]
legend(loc=4, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
xlabel(r'Q ($\AA^{-1}$)')

if dtype == '.sq':
    ylabel('S(Q)')
else:
    ylabel('I(Q)')

#==============================================================================
# text(5,0,'new chi files')
#==============================================================================
xlim(0,6)
ylim(-1,2.6)

#add vertical lines at the local max
# num_of_peak_showed = arange(9)

num_of_peak_showed = arange(shape(pa.peak_pos_0rh(xy, target.__name__, dtype))[0])

max_of_the_line = array(pa.vline_and_label_pos(target.__name__, dtype)[0])+0.2

[axvline(
    pa.peak_pos_0rh(xy[0], target.__name__, dtype)[i],
    ymin=pa.vline_and_label_pos(target.__name__, dtype)[0][i],
    ymax=max_of_the_line[i],color='k',ls=':') for i in num_of_peak_showed]

#add names of the peaks
[text(
    pa.peak_pos_0rh(xy[0], target.__name__, dtype)[i],
    pa.vline_and_label_pos(target.__name__, dtype)[1][i],
    pa.name_of_the_peak()[i],
    horizontalalignment='center',fontsize=14)
    for i in num_of_peak_showed]

#creating a sub-subplot
rect = [0.12,0.55,0.18,0.4]
ax_sub = ssp.add_subplot_axes(ax,rect)
[plot(
    xy[i][0],xy[i][1],
    c = S.Spec.line_color[i+S.Spec.interval-4],
    linestyle=S.Spec.line_type[i%3],
    linewidth=S.Spec.line_width[i],
    label='%s h'%(data_label[i])
    )
    for i in range (shape(xy)[0])]

xlim(inset_x_min, 0.6)
if dtype == '.iq':
    ylim(0, 2500000)
else:
    ylim(-0.4, inset_y_max)
xticks(arange(0.3,0.61,0.1))
# yticks(arange(0.0,2.01,1.0))
yFormatter = FormatStrFormatter('%.1f')
ax_sub.yaxis.set_major_formatter(yFormatter)
# ax_sub.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))


f.show()

print '\n   ploting:', target.__name__

#   f.savefig('/Users/hty/desktop/%s %s.pdf'%(dtype[1:], target.__name__))
