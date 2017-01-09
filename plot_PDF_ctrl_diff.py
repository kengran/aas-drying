# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:01:43 2016

@author: hty
"""


from numpy import *
from matplotlib.pyplot import *
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
f, ax = subplots(figsize=(10,7))

[ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*normalization_factor[i], alpha=1,label='%s'%(name_of_the_plot[i])) for i in targetFile.Readfile()[2]]

'''difference plots'''
mag_factor = 5

[ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])*normalization_factor[i]-array(interm2_syn[0][1]))*mag_factor + 7, '--',linewidth=1.5,alpha=1,label='%s - %s no norm.'%(name_of_the_plot[i], name_of_the_plot[0])) for i in targetFile.Readfile()[2]]

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

ylim (-5,12)
#ax.axhline(y=0, color='k')
xlabel(r'r ($\AA$)')
ylabel('G(r)')
legend(loc=4, fontsize ='small',ncol=2,columnspacing=0.5, labelspacing=0, frameon = True)

text(5,9,'x %s'%(mag_factor))
f.show()


#   f.savefig('/Users/hty/desktop/diff pdf %s full range.pdf'%(targetFile.__name__))
