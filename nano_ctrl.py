# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:45:32 2016

@author: hty
"""

from numpy import *
import sys
sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd

def Readfile():
    file_name = ['/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/AAS_7perc_nano_ctrl_Feb26_2151-00000.gr']
    data_files_1=[file(file_name[0])]

    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/AAS_7perc_nano_ctrl_Feb27_0953-00000.gr')
    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/AAS_7perc_NP_ctrl_Feb27_1727-00000.gr')

    ''' this one is weird'''
    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/AAS_7perc_NP_ctrl_Feb28_0741-00000.gr')

    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/AAS_7perc_NP_ctrl_Feb28_1239-00000.gr')
    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/AAS_7perc_NP_ctrl_Feb28_2358-00000.gr')

    # from july
    file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Jul/chi_files/xmin_7/mod/AAS_NP_ctrl_Jul_mod.gr')

    # from december
    # file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Dec/Blake_Samples/mod/SC_7_scan_20-00000_scaled_wrt_kapton.gr')

    [data_files_1.append(file(file_name[i])) for i in range (1,shape(file_name)[0])]
    good_data_number = [0,1,4,5, 6,7]
    return data_files_1, file_name, good_data_number


def curve():
    xy = gd.curve(Readfile()[0], 141)
    return xy

def peak_sisi():
    """normalized """
    sisi_sio = gd.sisi_sio(Readfile()[0],141)
    return sisi_sio

def peak_casi():
    """normalized """
    casi_sio = gd.casi_sio(Readfile()[0],141)
    return casi_sio

def CaSi():
    """ no norm """
    return gd.CaSi(Readfile()[0], 141)

def x_value():
    x_val = [
    4.35,
    16.38,
    23.95,
    38.18,
    43.15,
    54.47,
    3576,
    6701.98
    ]
    return x_val

def pLot():
    close("all")
    f, ax = plt.subplots()

    ax.plot(Data()[0],Data()[1],'o-',label='Nano ctrl')
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')
    return
