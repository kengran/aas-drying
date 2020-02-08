
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 13:45:32 2016

@author: hty
"""

from numpy import *
# import sys
# sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd

def read_file_with_low_angle_info():
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/contain low angle info/'

    file_name = [directory + '/AAS_7perc_nano_ctrl_Feb26_2151-00000.gr']
    x_val = [4]

    file_name.append(directory + '/AAS_7perc_nano_ctrl_Feb27_0953-00000.gr')
    x_val.append(16)

    # file_name.append(directory + '/AAS_7perc_NP_ctrl_Feb27_1727-00000.gr')
    # x_val.append(24)

    ''' this one is weird'''
    # file_name.append(directory + '/AAS_7perc_NP_ctrl_Feb28_0741-00000.gr')
    # x_val.append(38)

    file_name.append(directory + '/AAS_7perc_NP_ctrl_Feb28_1239-00000.gr')
    x_val.append(43)

    file_name.append(directory + '/AAS_7perc_NP_ctrl_Feb28_2358-00000.gr')
    x_val.append(54)

    # from july
    file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Jul/chi_files/contain low angle info/AAS_NP_ctrl_Jul_mod.gr')
    x_val.append(3600)

    data_files_1 = [file(file_name[i]) for i in range (len(file_name))]

    good_data_number = range(len(file_name))
    return data_files_1, file_name, good_data_number, x_val

def Readfile():
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/Nano ctrl/'

    file_name = [directory + 'AAS_7perc_nano_ctrl_Feb26_2151-00000.gr']
    x_val = [4]

    file_name.append(directory + 'AAS_7perc_nano_ctrl_Feb27_0953-00000.gr')
    x_val.append(16)

    # file_name.append(directory + 'AAS_7perc_NP_ctrl_Feb27_1727-00000.gr')
    # x_val.append(24)

    ''' this one is weird'''
    # file_name.append(directory + 'AAS_7perc_NP_ctrl_Feb28_0741-00000.gr')
    # x_val.append(38)

    file_name.append(directory + 'AAS_7perc_NP_ctrl_Feb28_1239-00000.gr')
    x_val.append(43)

    file_name.append(directory + 'AAS_7perc_NP_ctrl_Feb28_2358-00000.gr')
    x_val.append(54)

    # from july
    file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Jul/chi_files/xmin_7/mod/AAS_NP_ctrl_Jul_mod.gr')
    x_val.append(3600)

    # from december
    # file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Dec/Blake_Samples/mod/SC_7_scan_20-00000_scaled_wrt_kapton.gr')

    data_files_1=[file(file_name[0])]
    [data_files_1.append(file(file_name[i])) for i in range (1,shape(file_name)[0])]
    good_data_number = range(len(file_name))
    return data_files_1, file_name, good_data_number, x_val


def curve():
    xy = gd.curve(Readfile()[0], 141)
    return xy

def norm_peak(which_peak, which_read_file_fn):
    """normalized """
    # using read file function containing low angle info:
    return gd.norm_peak(which_peak, which_read_file_fn()[0],141)

def CaSi():
    """ no norm """
    return gd.CaSi(read_file_with_low_angle_info()[0], 141)

def x_value(which_read_file_fn):
    x_val = which_read_file_fn()[3]
    return array(x_val)+24

def pLot():
    close("all")
    f, ax = plt.subplots()

    ax.plot(Data()[0],Data()[1],'o-',label='Nano ctrl')
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')
    return
