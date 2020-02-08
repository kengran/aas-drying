import pandas as pd
from numpy import *
from matplotlib.pyplot import *

f_nano = pd.read_excel ('../weight loss aas.xlsx', sheetname = 'nano-out')
f_no_nano = pd.read_excel ('../weight loss aas.xlsx', sheetname = 'no nano-out')

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

close('all')
fig = figure()

scatter(
    f_nano['time in hours'], f_nano['nano']*100,
    label = 'Nano-ZrO$_2$')

scatter(
    f_no_nano['time in hours'], f_no_nano['no nano']*100,
    label = 'No nano', c = 'g',
    marker='^')

legend(labelspacing=0.1, fontsize='small')
xlabel('Time (hours)')
ylabel('% weight')
xlim(0,150)
ylim(84,100)

from scipy import interpolate

f = interpolate.interp1d(
    f_nano['time in hours'], f_nano['nano']*100, kind='cubic')
xnew = np.arange(0, 140, 1)
ynew = f(xnew)
plot( xnew, ynew, '-')

f1 = interpolate.interp1d(
    f_no_nano['time in hours'], f_no_nano['no nano']*100, kind='cubic')
x_nonano = np.arange(0, 115, 1)
y_nonano = f1(x_nonano)
plot( x_nonano, y_nonano, '-')

fig.show()

# fig.savefig('/Users/hty/desktop/%s.pdf'%('aas weight loss'))
