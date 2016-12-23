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

import noNano_ctrl as n43

input_name = n43.Readfile()[1]
new_name = [input_name[i][:-3]+'.sq' for i in range (shape (input_name)[0])]
data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]


''' indicate the range of data plotted'''
y_val = gd.curve(data_files_1,141)


close("all")
f = figure()
#==============================================================================
# names=['%s'%(i) for i in range (shape(data_files_1)[0])]
#==============================================================================
[plot(y_val[i][0],y_val[i][1],label='%s h'%(n43.x_value() [i])) for i in range (shape(y_val)[0])]
legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
xlabel(r'r ($\AA^{-1}$)')
ylabel('S(Q)')
xlim(0.5,6)

f.show()

#==============================================================================
# text(5,0,'new chi files')
#==============================================================================

#   f.savefig('/Users/hty/desktop/sq %s.pdf'%(n43.__name__))
