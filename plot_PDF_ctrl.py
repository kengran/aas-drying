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

import noNano_ctrl as targetFile
import peak_assign as pn

reload(targetFile)

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

interm2_syn = targetFile.curve()

'''design the name of each plot'''
name_of_the_plot=['%s h'%(array(targetFile.x_value(targetFile.Readfile)[i])) for i in range (shape(interm2_syn)[0])]

close("all")
f, ax0 = subplots(figsize=(6,4))

line_color = ['b','gold','r','c','m']
[ax0.plot(
    interm2_syn[i][0],np.array(interm2_syn[i][1])*1,
    alpha=1,label='%s'%(name_of_the_plot[i]),
    color=line_color[i])
    for i in targetFile.Readfile()[2]]


#add vertical lines at the local max

# num_of_peak_showed = [0,2,5]
num_of_peak_showed = arange(9)
num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

lengthOftheLine = [0.91, 0.3, 0.73, 0.4, 0.6, 0.8, 0.6, 0.55, 0.6, 0.8, 0.8, 0.8]
[ax0.axvline(pn.find_local_max(interm2_syn)[1][i],ymin=0,ymax=lengthOftheLine[i],color='k',linewidth=0.8, ls=':') for i in num_of_peak_showed]

#add names of the peaks
position_y = [3.3, -0.5, 2.3 , 0, 1.4, 2.7, 1.5, 1, 1.5]
[ax0.text(
    pn.find_local_max(interm2_syn)[1][i],
    position_y[i],
    pn.name_of_the_peak(interm2_syn)[i],
    horizontalalignment='center', verticalalignment='bottom',
    fontsize=14, rotation=80) for i in num_of_peak_showed]

# text(0.1, 4, '(a)')

#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=10)
# grid(axis='x')

xlim (0.8,6)
ylim (-3,4)
#ax.axhline(y=0, color='k')

ax0.set_ylabel('G(r) ($\AA^{-2}$)')
Legend=ax0.legend(
    loc=4, fontsize ='small',
    ncol=2,columnspacing=0.5,
    labelspacing=0, frameon = True,
    title='Alkali-activation time')
setp(Legend.get_title(),fontsize='small')

f.show()

#   f.savefig('/Users/hty/desktop/pdf %s.pdf'%(targetFile.__name__))
