import read_file_mid_range as rf
from numpy import *
from matplotlib.pyplot import *
import sys
sys.path.append('/Users/hty/Google Drive/code/aas-drying')
import getData as gd

######### specify sample to plot #####
sample = 'nano'
RH = 0

reload(rf)
loaded_file = rf.Readfile(sample, RH)[0]
xy = gd.curve(loaded_file, 141)
print '\n   loaded_file:\n', loaded_file[0]

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
matplotlib.rc('font', **font)

close("all")

scale_factor = 0.7
f, ax = subplots(figsize=(12*scale_factor,7*scale_factor))

if not RH == 43:
    if sample == 'no nano':
        label = ['0.0', '0.4', '2.3', '4.6']
        sample_name = 'Without nano-ZrO$_2$ 0% RH'
    else:
        label = ['0.0', '3.3', '6.5', '9.8']
        sample_name = 'With nano-ZrO$_2$ 0% RH'
else:
    if sample == 'no nano':
        label = ['0.0', '2.1', '4.2', '6.3']
        sample_name = 'Without nano-ZrO$_2$ 43% RH'
    else:
        label = ['0.0', '4.0', '7.7', '11.9']
        sample_name = 'With nano-ZrO$_2$ 43% RH'

ax.arrow(10.9, -0.03, 0.3, 0, head_width=0.01, head_length=0.1,
    fc='k', ec='k')
ax.arrow(13.3, 0.14, -0.3, 0, head_width=0.01, head_length=0.1,
    fc='k', ec='k')
ax.arrow(15.5, 0.06, -0.3, 0, head_width=0.01, head_length=0.1,
    fc='k', ec='k')
ax.arrow(16.6, 0.08, 0.3, 0, head_width=0.01, head_length=0.1,
    fc='k', ec='k')
ax.arrow(20.6, 0, -0.3, 0, head_width=0.01, head_length=0.1,
    fc='k', ec='k')

interval = 8
line_color=cm.YlGnBu(np.linspace(0, 1, interval))
line_type = ['-','--',':','-']
marker_type = ['','','','']
line_width = [1,1.5,1.5,2]

[ax.plot(
    xy[i][0],(array(xy[i][1])),
    c=line_color[i+interval-4],
    alpha=1,
    linestyle=line_type[i], linewidth=line_width[i],
    label='%s h'%(label[i])) for i in rf.Readfile(sample, RH)[2] ]

legend(loc=4, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1, frameon=True)

xlabel(r'r ($\AA$)')
ylabel('G(r) ($\AA^{-2}$)')
xlim (10,22)
ylim (-0.39, 0.4)
#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=10)
grid(axis='x')
text(15.5, 0.43, sample_name)

subplots_adjust(bottom = 0.15, left = 0.15)

f.show()

# f.savefig('/Users/hty/desktop/pdf mid range %s RH%s.pdf'%(sample, RH))
