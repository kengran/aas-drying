from numpy import *
from matplotlib.pyplot import *

'''import the target file'''
import nano_ctrl as target_ctrl
import nano_rh0 as target
import peak_assign as pn

import plot_spec as S

close("all")

f, ax = subplots(figsize=(10,6))

# control
xy_ctrl = target_ctrl.curve()

'''design the name of each plot'''
name_of_the_plot_ctrl=['%s h'%(array(target_ctrl.x_value(target_ctrl.Readfile)[i])) for i in range (shape(xy_ctrl)[0])]

mag_factor = 1
plot_range = [3]
[ax.plot(
    xy_ctrl[i][0],
    (np.array(xy_ctrl[i][1])*1-array(xy_ctrl[0][1]))*mag_factor,
    '-',linewidth=1.5,
    alpha=1,
    c = S.Spec.line_color[3],
    label='Control with nano-ZrO$_2$ (%s - %s)'%(name_of_the_plot_ctrl[i], name_of_the_plot_ctrl[0])) for i in plot_range]


# dry with nano

''' indicate the range of data plotted'''
data_interval = 16
data_files_1=target.Readfile()[1][0::data_interval]
name_of_the_plot=[
    '%s h'%(array(target.peaks(target.Readfile)[0][0::data_interval][i]))
    for i in range (shape(data_files_1)[0])]

interm_syn = [np.array(data_files_1[i].readlines()) for i in range (np.shape(data_files_1)[0])]

''' remember to set start line number here '''
interm1_syn =[ [str.split(interm_syn[j][i]) for i in range(141,np.shape(interm_syn[j])[0])] for j in range (np.shape(data_files_1)[0])]

interm2_syn= [[[float(interm1_syn[k][j][i]) for j in range (0,np.shape(interm1_syn[k])[0])]for i in range (2) ] for k in range (np.shape(data_files_1)[0])]

#find local max to denote the peak position
local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(data_files_1)[0])]

norm_factor_wrt_first_curve = [interm2_syn[0][1][local_max[0][4]]/interm2_syn[i][1][local_max[i][4]] for i in range (shape(data_files_1)[0])]

[ax.plot(
    interm2_syn[i][0],
    (np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i]-array(interm2_syn[0][1])),
    '--',linewidth=1.5,alpha=1,
    c = S.Spec.line_color[-1],
    label='Drying with nano-ZrO$_2$ (%s - %s)'%(name_of_the_plot[i], name_of_the_plot[0]))
    for i in [1]]

#add vertical lines at the local max

# num_of_peak_showed = [0,2,5]
num_of_peak_showed = arange(9)
num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

lengthOftheLine = [0.6, 0.63, 0.66, 0, 0.68, 0.8, 0.75, 0.61, 0.69, 0.8, 0.8, 0.8]
[ax.axvline(
    pn.find_local_max(interm2_syn)[1][i],
    ymin=0,ymax=lengthOftheLine[i],
    color='k', ls=':') for i in num_of_peak_showed]

#add names of the peaks
position_y = [0.12, 0.15, 0.2 , 1.1, 0.2, 0.33, 0.25, 0.14, 0.22]
[text(
    pn.find_local_max(interm2_syn)[1][i],
    position_y[i],
    pn.name_of_the_peak(interm2_syn)[i],
    horizontalalignment='center',verticalalignment='bottom',
    fontsize=14, rotation=80) for i in num_of_peak_showed]


xlim (0.8,7)
ylim(-0.5,0.5)
xlabel(r'r ($\AA$)')
ylabel(r'G(r) ($\AA^{-2}$)')
legend(loc=4, fontsize ='small',ncol=1,columnspacing=0.5, labelspacing=0, frameon = True)
locator_params(axis='x',tight=True,nbins=10)
# grid(axis='x')
f.show()

#   f.savefig('/Users/hty/desktop/pdf diff comp %s %s.pdf'%(target.__name__, target_ctrl.__name__))
