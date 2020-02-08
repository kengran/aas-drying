
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
import nano_ctrl as target_ctrl
reload(target_ctrl)

import peak_assign as pn
reload(pn)

# set style of the plot
rcParams.update(rcParamsDefault)
style.use('classic')

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

interm2_syn = target_ctrl.curve()

'''design the name of each plot'''
name_of_the_plot=['%s h'%(array(target_ctrl.x_value(target_ctrl.Readfile)[i])) for i in range (shape(interm2_syn)[0])]
''

# do normalization
normalization_factor = [interm2_syn[0][1][pn.find_local_max(interm2_syn)[0][0][4]]/interm2_syn[i][1][pn.find_local_max(interm2_syn)[0][i][4]] for i in range (shape(interm2_syn)[0])]


def difference_plot(gs0, gs1, title_text = ''):
    ax0 = subplot(gs0)

    # line_color = ['b','gold','r','c','m']
    interval = 8
    line_color=cm.YlGnBu(np.linspace(0, 1, interval))

    [ax0.plot(
        interm2_syn[i][0],np.array(interm2_syn[i][1])*1,
        alpha=1,label='%s'%(name_of_the_plot[i])
        ,color=line_color[i+interval-5]
        )
        for i in range(len(interm2_syn))]
# target_ctrl.Readfile()[2]

    #add vertical lines at the local max

    # num_of_peak_showed = [0,2,5]
    num_of_peak_showed = arange(9)
    num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

    lengthOftheLine = [0.91, 0.3, 0.73, 0.55, 0.6, 0.8, 0.6, 0.55, 0.6, 0.8, 0.8, 0.8]
    [ax0.axvline(
        pn.find_local_max(interm2_syn)[1][i],
        ymin=0,ymax=lengthOftheLine[i],
        color='k',linewidth=0.8, ls=':') for i in num_of_peak_showed]

    #add names of the peaks
    position_y = [3.3, -0.5, 2.3 , 1, 1.4, 2.7, 1.5, 1, 1.5]
    [ax0.text(
        pn.find_local_max(interm2_syn)[1][i],
        position_y[i],
        pn.name_of_the_peak(interm2_syn)[i],
        horizontalalignment='center', verticalalignment='bottom',
        fontsize=14, rotation=80) for i in num_of_peak_showed]

    text(0.1, 4.5, title_text)

    #increase the freq of the ticks
    locator_params(axis='x',tight=True,nbins=10)
    # grid(axis='x')

    xlim (0.8,6)
    ylim (-3,4)
    #ax.axhline(y=0, color='k')

    ax0.set_ylabel('G(r) ($\AA^{-2}$)')
    Legend=ax0.legend(
        loc=4, fontsize ='small',
        ncol=2,columnspacing=0.5,
        labelspacing=0, frameon = True,
        title='Alkali-activation time')
    setp(Legend.get_title(),fontsize='small')

    '''difference plots'''
    ax1 = subplot(gs1)
    mag_factor = 1

    line_type = ['-','--',':','-']
    marker_type = ['','','','']
    line_width = [1,1.5,1.5,2]
    [ax1.plot(
        interm2_syn[i][0][0::2],
        (np.array(interm2_syn[i][1][0::2])*1-array(interm2_syn[0][1][0::2]))*mag_factor,
        linestyle=line_type[i-1], linewidth=line_width[i-1],
        alpha=1,marker=marker_type[i-1],
        markersize=2,label='%s - %s'%(name_of_the_plot[i],
        name_of_the_plot[0])
        ,color=line_color[i+interval-6]
        )
        for i in target_ctrl.Readfile()[2][1:]]

    # ax1.text(5,2,'x %s'%(mag_factor))
    # ax1.grid(axis='x')
    xlim (0.8,6)
    ylim(-1, 0.6)
    locator_params(axis='x',tight=True,nbins=10)
    locator_params(axis='y',tight=True,nbins=5)
    xlabel(r'r ($\AA$)')
    legend(
        loc=0, fontsize ='small',
        ncol=2,columnspacing=0.5, labelspacing=0, frameon = True)

    # text(0.1, 0.6, '(b)')
    title('Difference', fontsize='small')

if __name__ == '__main__':
    close("all")
    # f, ax = subplots(nrows=2, ncols=1, sharex=True, figsize=(7,7))
    f = figure(figsize=(8,8))
    gs = gridspec.GridSpec(2, 1,
                           height_ratios=[2,1]
                           )
    difference_plot(gs[0],gs[1])
    f.show()

#   f.savefig('/Users/hty/desktop/diff pdf %s.pdf'%(target_ctrl.__name__))
