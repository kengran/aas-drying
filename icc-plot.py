import pandas as pd
import matplotlib.pyplot as plt
from numpy import *
import plot_spec as S

df = pd.read_excel('../nishant zr data/icc AAS & ZrO2.xlsx', index_col=None, na_values=['NA'])

x = df['Time from mixing (h)']
y = df['AAS']

x_0_1 = df[u'Time from mixing (h).1']
y_0_1 = df[u'AAS w/ 0.1% ZrO2']

x_1 = df[u'Time from mixing (h).2']
y_1 = df['AAS w/ 1.0% ZrO2']

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
plt.matplotlib.rc('font', **font)

plt.close('all')
f,ax = plt.subplots()

ax.plot(x[1:], y[1:]*1000,
    c = S.Spec.line_color[0+S.Spec.interval-4],
    linestyle=S.Spec.line_type[0],
    linewidth=S.Spec.line_width[0],
    label = 'AAS')
ax.plot(x_0_1[1:], y_0_1[1:]*1000,
    c = S.Spec.line_color[2+S.Spec.interval-4],
    linestyle=S.Spec.line_type[1],
    linewidth=S.Spec.line_width[1],
    label = 'AAS with 0.1% ZrO$_2$')
ax.plot(x_1[1:], y_1[1:]*1000,
    c = S.Spec.line_color[3+S.Spec.interval-4],
    linestyle=S.Spec.line_type[0],
    linewidth=S.Spec.line_width[3],
    label = 'AAS with 1.0% ZrO$_2$')

# plt.subplots_adjust(left = 0.17)

ax.legend(fontsize = 14, labelspacing = 0.1)

plt.ylim(-0, 3)
plt.xlabel(r'Time (hours)')
plt.ylabel(r'Heat flow (mW/g)')
plt.xticks(arange(1, 111, 10))
plt.xlim(1,101)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
axins = inset_axes(ax,
                   width="40%",  # width = 30% of parent_bbox
                   height="40%",  # height : 1 inch
                   loc=7,
                   borderpad = 2)

axins.plot(x[500:1500], y[500:1500]*1000,
    c = S.Spec.line_color[0+S.Spec.interval-4],
    linestyle=S.Spec.line_type[0],
    linewidth=S.Spec.line_width[0],
    label = 'AAS')
axins.plot(x_0_1[500:1500], y_0_1[500:1500]*1000,
    c = S.Spec.line_color[2+S.Spec.interval-4],
    linestyle=S.Spec.line_type[1],
    linewidth=S.Spec.line_width[1],
    label = 'AAS with 0.1% ZrO$_2$',ls='--')
axins.plot(x_1[500:1500], y_1[500:1500]*1000,
    c = S.Spec.line_color[3+S.Spec.interval-4],
    linestyle=S.Spec.line_type[0],
    linewidth=S.Spec.line_width[3],
    label = 'AAS with 1.0% ZrO$_2$',ls='-.')

axins.set_xticks(arange(5,31,3))
axins.set_yticks(arange(0,3.1,1))
axins.set_xlim(8,17)

f.show()

# f.savefig('/Users/hty/desktop/icc %s.pdf'%('aas'))
