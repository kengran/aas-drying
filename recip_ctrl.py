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
import peak_assign_recip as pa

import nano_ctrl as n43

import plot_spec as S

reload(S)
reload(pa)
reload(n43)

input_name = n43.read_file_with_low_angle_info()[1]
new_name = [input_name[i][:-3]+'.sq' for i in range (shape (input_name)[0])]
data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]


''' indicate the range of data plotted'''
y_val = gd.curve(data_files_1,141)

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

# close("all")
f, ax = subplots()

if n43.__name__ == 'noNano_ctrl':
    plot_range = range(len(y_val))
else:
    # plot_range = [0, 1, 3, 4,5]
    plot_range = range(len(y_val))

color_spec = S.Spec()
[ax.plot(
    y_val[i][0],y_val[i][1],
    c = color_spec.line_color[i + color_spec.interval-5],
    linestyle=S.Spec.line_type[i],
    linewidth=S.Spec.line_width[i],
    label='%s h'%(n43.x_value(n43.Readfile) [i])) for i in plot_range]

legend(loc=4, ncol=1, fontsize='small', columnspacing=1, labelspacing=0.1)
xlabel(r'Q ($\AA^{-1}$)')
ylabel('S(Q)')

xlim(0,6)
ylim(-1, 2.8)


# num_of_peak_showed = arange(9)
num_of_peak_showed = arange(len(pa.find_local_max(y_val[-1])[1]))

min_of_the_line = array([0, 0, 0.08, 0.62, 0.45,
    0.25, 0.4, 0.4, 0.45, 0.35,
    0.8, 0.8, 0.8])+0.1

max_of_the_line = array(min_of_the_line)+0.2
nameOfthePeak = ['H','C', 'H','C','C','H','C','C/H','C/H','C','Ca-O', 'x', 'x']
position_y = array([
    0.2, 0.2, 0.5, 2.6 , 2,
    1.2, 1.8, 1.8, 2,1.6,
    2, 2, 2])

#add vertical lines at the local max
[ax.axvline(
    pa.find_local_max(y_val[-1])[1][i],
    ymin=min_of_the_line[i],ymax=max_of_the_line[i],
    color='k',ls=':')
    for i in num_of_peak_showed]

#add names of the peaks
[text(
    pa.find_local_max(y_val[-1])[1][i],position_y[i],
    pa.name_of_the_peak()[i], fontsize = 'small',
    horizontalalignment='center') for i in num_of_peak_showed]


f.show()

#   f.savefig('/Users/hty/desktop/sq low angle %s.pdf'%(n43.__name__))
