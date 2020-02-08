# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:23:04 2016

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')

#==============================================================================
# import noNano_rh0_prescan as nn100
# import noNano_rh0 as nn0
#==============================================================================
import noNano_ctrl as ctrl





close('all')
f, ax = subplots()
ax.plot(ctrl.x_value(),ctrl.peak_sisi(),'o-', label='Control')
ax.plot(ctrl.x_value(),ctrl.peak_casi(),'o-', label='Control')

legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)

xlabel('Time, hour')
ylabel('Si-T/Si-O')
#xlim(-1,10)
f.show()



#   savefig('/Users/hty/desktop/%s.eps'%('sisi-sio 0rh noNano dry&ctrl'))
