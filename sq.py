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

# import target file
import noNano_rh0 as target

# input_name = target.read_reciprocal_space_files('.sq')[2]
# new_name = [input_name[i][:-3]+'.sq' for i in range (shape (input_name)[0])]
# data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]

data_files_1 = target.read_reciprocal_space_files('.sq')[0]

''' indicate the range of data plotted'''
data_interval = 4
xy = gd.curve(data_files_1,141) [0::data_interval]


close("all")
f = figure()
# remember to update the range of the label****
[plot(xy[i][0],xy[i][1],label='%s h'%(target.read_reciprocal_space_files('.sq')[1][0::data_interval] [i])) for i in range (shape(xy)[0])]
legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
xlabel(r'Q ($\AA^{-1}$)')
ylabel('S(Q)')

#==============================================================================
# text(5,0,'new chi files')
#==============================================================================
xlim(0,6)
ylim(-1,2.5)
f.show()

#   f.savefig('/Users/hty/desktop/sq %s.pdf'%(target.__name__))
