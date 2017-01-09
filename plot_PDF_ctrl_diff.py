# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:01:43 2016

@author: hty
"""


from numpy import *
from matplotlib.pyplot import *
from matplotlib import gridspec
import sys
# sys.path.append('/Users/hty/Google Drive/research/aas drying/APS_Feb/chi_files')
# sys.path.append('/Users/hty/Google Drive/research/aas drying/white aas kinetics data')

'''import the target file'''
import noNano_ctrl as targetFile

import peak_assign as pn

# set style of the plot
style.use('seaborn-white')

#change font properties of the plots
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

interm2_syn = targetFile.curve()

'''design the name of each plot'''
name_of_the_plot=['%s h'%(array(targetFile.x_value()[i])) for i in range (shape(interm2_syn)[0])]
''

# do normalization
normalization_factor = [interm2_syn[0][1][pn.find_local_max(interm2_syn)[0][0][4]]/interm2_syn[i][1][pn.find_local_max(interm2_syn)[0][i][4]] for i in range (shape(interm2_syn)[0])]


close("all")
gs = gridspec.GridSpec(2, 1,
                       height_ratios=[2,1]
                       )

# f, ax = subplots(nrows=2, ncols=1, sharex=True, figsize=(7,7))
f = figure(figsize=(8,8))
ax0 = subplot(gs[0])

[ax0.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*1, alpha=1,label='%s'%(name_of_the_plot[i])) for i in targetFile.Readfile()[2]]

#add vertical lines at the local max

# num_of_peak_showed = [0,2,5]
num_of_peak_showed = arange(9)
num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

lengthOftheLine = [0.91, 0.3, 0.73, 0.4, 0.6, 0.8, 0.6, 0.55, 0.6, 0.8, 0.8, 0.8]
[ax0.axvline(pn.find_local_max(interm2_syn)[1][i],ymin=0,ymax=lengthOftheLine[i],color='k',linewidth=0.8) for i in num_of_peak_showed]

#add names of the peaks
position_y = [3.5, -0.5, 2.5 , 0, 1.5, 2.7, 1.8, 1, 1.5]
[ax0.text(pn.find_local_max(interm2_syn)[1][i],position_y[i], pn.name_of_the_peak(interm2_syn)[i],horizontalalignment='center',fontsize=14) for i in num_of_peak_showed]

#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=20)
grid(axis='x')

xlim (0.8,6)

ylim (-3,4)
#ax.axhline(y=0, color='k')

ax0.set_ylabel('G(r)')
legend(loc=0, fontsize ='small',ncol=1,columnspacing=0.5, labelspacing=0, frameon = True)

'''difference plots'''
ax1 = subplot(gs[1])
mag_factor = 1

[ax1.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])*1-array(interm2_syn[0][1]))*mag_factor, '--',linewidth=1.5,alpha=1,label='%s - %s'%(name_of_the_plot[i], name_of_the_plot[0])) for i in targetFile.Readfile()[2]]

# ax1.text(5,2,'x %s'%(mag_factor))
ax1.grid(axis='x')
xlim (0.8,6)
ylim(-0.9, 0.6)
locator_params(axis='x',tight=True,nbins=20)
xlabel(r'r ($\AA$)')
legend(loc=0, fontsize ='small',ncol=3,columnspacing=0.5, labelspacing=0, frameon = True)

f.show()


#   f.savefig('/Users/hty/desktop/diff pdf %s.pdf'%(targetFile.__name__))
