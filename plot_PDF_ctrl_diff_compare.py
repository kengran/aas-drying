
from matplotlib.pyplot import *
from numpy import *

'''import files'''
import noNano_ctrl as nc
import nano_ctrl as nnc

import peak_assign as pn

close("all")
f, ax = subplots(figsize=(20,6))
name_of_the_plot_nc=['%s h'%(array(nc.Data()[0][i])) for i in range (shape(nc.Data()[0])[0])]
name_of_the_plot_nnc=['%s h'%(array(nnc.Data()[0][i])) for i in range (shape(nnc.Data()[0])[0])]

[ax.plot(nc.curve()[i][0],(np.array(nc.curve()[i][1])-array(nc.curve()[0][1]))*10 , '-',alpha=1,label='no nano, %s - 0 h'%(name_of_the_plot_nc[i])) for i in nc.Readfile()[2]]

[ax.plot(nnc.curve()[i][0],(np.array(nnc.curve()[i][1])-array(nnc.curve()[0][1]))*10 + 5, '--',linewidth=1.5,alpha=1,label='nano, %s - 4.35 h'%(name_of_the_plot_nnc[i])) for i in nnc.Readfile()[2]]

legend(loc=0, fontsize ='small',ncol=2,columnspacing=0.5, labelspacing=0)

#add vertical lines at the local max
i_range = [0, 2, 5, 8]
lengthOftheLine = [0.92,0.9,0.9,0.9,0.9,0.9,0.8,0.8,0.9,0.9]
[ax.axvline(pn.find_local_max(nc.curve())[1][i],ymin=0,ymax=lengthOftheLine[i],color='k') for i in i_range]

#add names of the peaks
position_y = [3.5,1,2.5 ,2.5, 3, 3,2,2.7,3.5]
[text(pn.find_local_max(nc.curve())[1][i],position_y[i], pn.name_of_the_peak()[i],horizontalalignment='center',fontsize=14) for i in i_range]

show()

#   f.savefig('/Users/hty/desktop/diff pdf compare %s.pdf'%('full range'))
