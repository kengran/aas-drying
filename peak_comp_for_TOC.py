# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:31:46 2016

@author: hty
"""

from matplotlib.pyplot import *
from numpy import *
import sys
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')

import nano_rh0 as n0
import noNano_rh0 as nn0
reload(n0)
reload(nn0)

sys.path.append('/Users/hty/Google Drive/python_modules')
import plot_spec as ps

style.use('classic')

#change font properties of the plots
font = {'family' : 'Helvetica',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

close("all")
f, ax = subplots(figsize=(1.6*3.3,1.2*3.3))

# f.text(0.1,0.95,'with nano')

line1, = ax.plot(
    array(nn0.peaks(nn0.Readfile)[0]),
    nn0.peak_Ca_T(nn0.Readfile),
    'o-',
    c=ps.Spec.line_color[3],
    label='No nano')

line2, = ax.plot(
    array(n0.peaks(n0.Readfile)[0]),
    n0.peak_Ca_T(n0.Readfile),
    '^-',
    c=ps.Spec.line_color[-1],
    label=r'Nano-ZrO$_2$')

ax.legend(
    loc=0,
    fontsize =17,
    ncol=1
    # ,columnspacing=1
    # ,labelspacing=0.1
    )

ax.set_ylabel('PDF peak Ca-T/T-O')
ax.set_xlabel('Drying time, hour')

subplots_adjust(left=0.17, bottom=0.15)

f.show()

#   f.savefig('/Users/hty/desktop/%s.pdf'%('peaks comp'))
