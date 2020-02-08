import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sname = 'table_no_nano'

if sname == 'table_nano':
    skipFooter = 1
elif sname == 'table_no_nano':
    skipFooter = 0

df = pd.read_excel ('../cal_peak_shift_higher_res.xlsx',
    sheetname = sname, skiprows=1,
    skip_footer=skipFooter)

plt.rcParams.update(plt.rcParamsDefault)
plt.style.use(u'seaborn-ticks')

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 20}
plt.rc('font', **font)

interval = 3
line_color=plt.cm.YlGnBu(np.linspace(0, 1, interval))

plt.close('all')

scale_factor = 0.7
fig, ax = plt.subplots(figsize=(12*scale_factor,4*scale_factor))

# ax = df.plot.bar()

bar_width = 0.35
xaxis = np.arange(6)

ax.bar(xaxis, df[0],
    bar_width,
    hatch="///"
    ,color=line_color[1]
    )
ax.bar(xaxis+bar_width, df[0.43],
    bar_width
    ,color=line_color[2]
    )

ax.set_xlabel('Peak Shoulder Location ($\AA$)')
ax.set_ylabel('Strain')
plt.xticks(rotation=0)

ax.legend(('0%', '43%'),
    title='RH', fontsize=15,
    loc=0, labelspacing=0, frameon=True)

ax.set_xticks(xaxis + bar_width/2)
ax.set_xticklabels((r'11.1', r'13.3$^a$', '15.6$^b$', '16.9', '20.3$^c$',r'$\frac{a+b+c}{3}$'))

plt.axhline(0, color='k')

plt.subplots_adjust(
        bottom=0.35,
        left= 0.16, 
        top=0.95
    )

ax.spines["top"].set_visible(False)
# ax.spines["bottom"].set_visible(False)
# ax.spines["left"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show(block=False)

 # plt.savefig('/Users/hty/desktop/strain bar chart %s.pdf'%(sname))
