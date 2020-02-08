# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:00:08 2015

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys
from matplotlib import gridspec

#import the target file
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')

import peak_assign as pn
reload(pn)

import getData as gd

'''change target here'''
import nano_rh0 as target
reload(target)

''' indicate the range of data plotted'''
if target.__name__ == 'nano_rh0':
    data_interval = 8
    data_files_1=target.Readfile()[1][0::data_interval]
    name_of_the_plot=['%s h'%(array(target.peaks(target.Readfile)[0][0::data_interval][i])) for i in range (shape(data_files_1)[0])]
elif target.__name__ == 'nano_rh43':
    data_interval = 3
    data_files_1=target.read_file_with_low_angle_info()[1][0::data_interval]
    name_of_the_plot=[
        '%s h'%(array(target.peaks(
        target.read_file_with_low_angle_info)[0][0::data_interval][i]))
        for i in range (shape(data_files_1)[0])]
elif target.__name__ == 'noNano_rh43':
    data_interval = 6
    data_files_1=target.Readfile()[1][0::data_interval]
    name_of_the_plot=['%s h'%(array(target.peaks(target.Readfile)[0][0::data_interval][i])) for i in range (shape(data_files_1)[0])]
else:
    data_interval = 9
    data_files_1=target.Readfile()[1][0::data_interval]
    name_of_the_plot=['%s h'%(array(target.peaks(target.Readfile)[0][0::data_interval][i])) for i in range (shape(data_files_1)[0])]

interm2_syn = gd.curve(data_files_1,141)

# do normalization
norm_factor_wrt_last_curve = [interm2_syn[-1][1][pn.find_local_max(interm2_syn)[0][0][4]]/interm2_syn[i][1][pn.find_local_max(interm2_syn)[0][i][4]] for i in range (shape(data_files_1)[0])]

norm_factor_wrt_first_curve = [interm2_syn[0][1][pn.find_local_max(interm2_syn)[0][0][4]]/interm2_syn[i][1][pn.find_local_max(interm2_syn)[0][i][4]] for i in range (shape(data_files_1)[0])]


# set style of the plot
# style.use('classic')

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

interval = 8
line_color=cm.YlGnBu(np.linspace(0, 1, interval))


def plot():
    # start plotting
    close('all')
    f, ax0 = subplots(figsize=(6,4.5))

    subplots_adjust(
            left = 0.15,
            bottom = 0.16
            )

#    text(0.05, 0.9, target.__name__, transform=ax0.transAxes)

    # no normalization
    # [ax0.plot(interm2_syn[i][0],np.array(interm2_syn[i][1]), alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]


    # with normalization
    [ax0.plot(
        interm2_syn[i][0],np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i],
        alpha=1,label='%s'%(name_of_the_plot[i]),
        color=line_color[i+interval-5]
        )
        for i in range (np.shape(data_files_1)[0])]

    #add vertical lines at the local max

    # num_of_peak_showed = [0,2,5]
    num_of_peak_showed = arange(9)
    num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

    lengthOftheLine = [0.85, 0.3, 0.66, 0.4, 0.61, 0.8, 0.6, 0.55, 0.6, 0.8, 0.8, 0.8]
    [ax0.axvline(
        pn.find_local_max(interm2_syn)[1][i],
        ymin=0,
        ymax=lengthOftheLine[i],
        color='k',
        ls=':') for i in num_of_peak_showed]

    #add names of the peaks
    position_y = [3.2, -0.8, 1.8 , 0, 1.5, 2.7, 1.5, 1, 1.5]
    [text(
        pn.find_local_max(interm2_syn)[1][i],position_y[i],
        pn.name_of_the_peak(interm2_syn)[i],
        horizontalalignment='center',
        verticalalignment='bottom',
        fontsize=14,
        rotation=80) for i in num_of_peak_showed]


    #increase the freq of the ticks
    locator_params(axis='x',tight=True,nbins=10)

    xlim (0.8,6)
    # ylim (-0.4,0.4)
    #ax.axhline(y=0, color='k')

    ylabel('G(r) ($\AA^{-2}$)')
    xlabel(r'r ($\AA$)')
    legend(loc=4, fontsize ='small',ncol=1,columnspacing=0.5, labelspacing=0, frameon = True)

    f.show()

    # f.savefig('/Users/hty/desktop/pdf %s.pdf'%(target.__name__))


def difference_plot(gs0, gs1, title_text = ''):
    # f, ax = subplots(nrows=2, ncols=1, sharex=True, figsize=(7,7))

    ax0 = subplot(gs0)
    text(0.1, 4.5, title_text)
    [ax0.plot(
        interm2_syn[i][0],
        np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i],
        alpha=1,
        label='%s'%(name_of_the_plot[i]),
        color=line_color[i+interval-4]
        ) for i in range (np.shape(data_files_1)[0])]

    # [ax.plot(interm2_syn[i][0],np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i], alpha=1,label='%s'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]

    #add vertical lines at the local max

    # num_of_peak_showed = [0,2,5]
    num_of_peak_showed = arange(9)
    # num_of_peak_showed = append(num_of_peak_showed, [-3, -2, -1])

    lengthOftheLine = [0.85, 0.3, 0.66, 0.55, 0.61, 0.8, 0.6, 0.55, 0.6, 0.8, 0.8, 0.8]
    [ax0.axvline(
        pn.find_local_max(interm2_syn)[1][i],
        ymin=0,
        ymax=lengthOftheLine[i],
        color='k',
        ls=':') for i in num_of_peak_showed]

    #add names of the peaks
    position_y = [3.2, -0.8, 1.8 , 1, 1.5, 2.7, 1.5, 1, 1.5]
    [text(
        pn.find_local_max(interm2_syn)[1][i],position_y[i],
        pn.name_of_the_peak(interm2_syn)[i],
        horizontalalignment='center',
        verticalalignment='bottom',
        fontsize=14,
        rotation=80) for i in num_of_peak_showed]


    #increase the freq of the ticks
    locator_params(axis='x',tight=True,nbins=10)

    xlim (0.8,6)
    ylim (-3,4)
    #ax.axhline(y=0, color='k')

    ylabel('G(r) ($\AA^{-2}$)')
    Legend=ax0.legend(
        loc=4, fontsize ='small',
        ncol=2,columnspacing=0.5,
        labelspacing=0, frameon = True, title='Drying time')
    setp(Legend.get_title(),fontsize='small')

    '''difference plots'''
    ax1 = subplot(gs1)
    mag_factor = 1
    # text(0.1, 0.5, '(b)')

    line_type = ['-','-','--','-']
    marker_type = ['','','','']
    line_width = [1,1,1.5,2]

    [ax1.plot(
        interm2_syn[i][0],
        (np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i]-array(interm2_syn[0][1])),
        linestyle=line_type[i], linewidth=line_width[i],
        alpha=1,
        label='%s - %s'%(name_of_the_plot[i], name_of_the_plot[0]),
        color=line_color[i+interval-5]
        ) for i in range (np.shape(data_files_1)[0])[1:]]

    #difference plots
    # [ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])*norm_factor_wrt_first_curve[i]-array(interm2_syn[0][1]))*5 + 6, '--', alpha=1,label='%s - %s'%(name_of_the_plot[i], name_of_the_plot[0])) for i in range (np.shape(data_files_1)[0])]

    # [ax.plot(interm2_syn[i][0],(np.array(interm2_syn[i][1])-array(interm2_syn[0][1]))*5 + 10, '--', linewidth=1.5,alpha=1,label='%s - 0h no norm.'%(name_of_the_plot[i])) for i in range (np.shape(data_files_1)[0])]
    locator_params(axis='x',tight=True,nbins=10)

    xlabel(r'r ($\AA$)')
    xlim (0.8,6)
    ylim(-0.6, 0.5)
    # text(5,7.5,'x 5')
    legend(loc=4, fontsize ='small',ncol=2,columnspacing=0.5, labelspacing=0, frameon = True)
    title('Difference', fontsize='small')
    return target.__name__

if __name__ == '__main__':

    # close("all")
#    f = figure(figsize=(8,8))
#    gs = gridspec.GridSpec(2, 1,
#                           height_ratios=[2,1]
#                           )
#    difference_plot(gs[0],gs[1])
#    f.show()
        
    plot()


    #   f.savefig('/Users/hty/desktop/diff pdf %s.pdf'%(target.__name__))
