# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:14:28 2016

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')

import noNano_rh0_prescan as nn100
import noNano_rh0 as nn0
import noNano_ctrl as ctrl

sys.path.append('/Users/hty/Google Drive/python_modules')
import sub_subplot as ssp



close('all')
ax = subplot()
l1, = ax.plot((array(nn100.Data()[0])-nn100.Data()[0][-1]-19/2.5)*2.5/60,nn100.Data()[1],'o-',label='96% RH')
l2, = ax.plot(array(nn0.Data()[1]),nn0.Data()[2],'o-',label='0% RH')

xlabel('Time, hour')
ylabel('Si-T/Si-O')
#xlim(-1,10)

#create two x axes
ax2 = ax.twiny()
l3, = ax2.plot(ctrl.Data()[0],ctrl.Data()[1],'ro-', label='Control')

legend((l1,l2,l3),('96% RH','0% RH','Control'),loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)


#==============================================================================
# #creating an inset
# rect = [0.3,0.6,0.4,0.2]
# ax_sub = ssp.add_subplot_axes(ax,rect)
# plot(ctrl.Data()[0],ctrl.Data()[1],'ro-', label='Control')
# legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
# ylim(0.31,0.41)
#==============================================================================

#   savefig('/Users/hty/desktop/%s.eps'%('sisi-sio 0rh noNano dry&ctrl'))
