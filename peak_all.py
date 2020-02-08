# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:31:46 2016

@author: hty
"""

# from matplotlib.pyplot import *
import sys
sys.path.append('/Users/hty/Google Drive/research/APS exp/chi_files')

Flag = 'nano'
if Flag == 'nonano':
    import noNano_rh0 as n0
    import noNano_50rh as n50
    import noNano_ctrl as ctrl
    xmax = 10
else:
    import nano_rh0 as n0
    import nano_rh43 as n50
    import nano_ctrl as ctrl
    xmax = 17
from matplotlib.pyplot import *
from numpy import *

reload(n0)
reload(n50)
reload(ctrl)

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

#close("all")
f, ax = subplots(2, sharex=True,figsize=(8,8))

'''Si-T'''
line1, = ax[0].plot(
    array(n0.Readfile()[0])*2.5/60,
    n0.peaks(n0.Readfile)[1],
    'o-',label='0% RH')

ax[0].set_ylabel("Si-T/T-O")

line2, = ax[0].plot(
    array(n50.Readfile()[0])*2.5/60,
    n50.peaks(n50.Readfile)[1],
    '^-',label='43% RH')

ax[0].scatter(
    ctrl.x_value(ctrl.Readfile)[0:2] - 24,
    ctrl.norm_peak('Si-T', ctrl.Readfile)[0:2],
    c='r',marker='s', label='Control', s = 40)

ax[0].legend(loc=5, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1, scatterpoints=1)

'''Ca-T'''
line4, = ax[1].plot(
        array(n0.Readfile()[0])*2.5/60,
        array(n0.peaks(n0.Readfile)[2]),
        'o-',label='0% RH'
        )
line5, = ax[1].plot(
        array(n50.Readfile()[0])*2.5/60,
        n50.peaks(n50.Readfile)[2],
        '^-',label='43% RH')

ax[1].scatter(
    ctrl.x_value(ctrl.Readfile)[0:2] - 24,
    ctrl.norm_peak('Ca-T', ctrl.Readfile)[0:2],
    c='r',marker='s', label='Control' , s = 40)

ax[1].legend( loc=4, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1,scatterpoints=1)

ax[1].set_ylabel('Ca-T/T-O')
ax[1].set_xlabel('Time (hours)')
# ax[1].set_ylim(0.71,0.85)

if Flag == 'nonano':
    yticks( arange(0.64,0.78,0.04))
else:
    yticks( arange(0.7,0.86,0.04))

# xlim(0,10)
ax[1].set_xlim(0, xmax)
f.show()

#   f.savefig('/Users/hty/desktop/peaks %s.pdf'%(Flag))
