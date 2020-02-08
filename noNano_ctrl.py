# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 09:37:36 2016

@author: hty
"""

from numpy import *
# import sys
# sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd
import matplotlib.pyplot as plt

def read_file_with_low_angle_info():
    directory = '/Users/hty/Google Drive/research/aas drying/APS_Feb/chi_files/noNano ctrl/contain low angle info/'

    file_name = [directory + 'AAS_7perc_noNP_ctrl_Feb29_0020-00000.gr']
    x_val = [0]

    file_name.append(directory + 'AAS_7perc_ctrl_32h_Fri8pm-00000.gr')
    x_val.append(9)

    file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb27_1715-00000.gr')
    x_val.append(30)

    file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb28_2347-00000.gr')
    x_val.append(60)

    file_name.append(
        '/Users/hty/Google Drive/research/aas drying/APS_Jul/chi_files/contain low angle info/'
        +'AAS_noNP_ctrl_Jul_mod.gr')
    x_val.append(3600)

    data_files_1 = [file(file_name[i]) for i in range (len(file_name))]

    good_data_number = range(len(file_name))
    return data_files_1, file_name, good_data_number, x_val


def Readfile():
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/noNano ctrl/'
    file_name = [directory + 'AAS_7perc_noNP_ctrl_Feb29_0020-00000.gr']
    x_val = [0]

    file_name.append(directory + 'AAS_7perc_ctrl_32h_Fri8pm-00000.gr')
    x_val.append(9)

    # file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb27_1005-00000.gr')
    # x_val.append(23)

    file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb27_1715-00000.gr')
    x_val.append(30)

    # file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb28_0731-00000.gr')
    # x_val.append(44)
    #
    # file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb28_1231-00000.gr')
    # x_val.append(49)

    file_name.append(directory + 'AAS_7perc_noNP_ctrl_Feb28_2347-00000.gr')
    x_val.append(60)

    file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Jul/chi_files/xmin_7/mod/AAS_noNP_ctrl_Jul_mod.gr')
    x_val.append(3600)

    # from december
    # file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Dec/Blake_Samples/mod/SC_7_scan_19-00000_scaled_wrt_kapton.gr')

    data_files_1=[file(file_name[i]) for i in range (0,shape(file_name)[0])]

<<<<<<< HEAD
    good_data_number = range(len(file_name))
    # good_data_number = [0,1,3,6,7]
    return data_files_1, file_name, good_data_number, x_val

def norm_peak(which_peak, which_read_file_fn):
    return gd.norm_peak(which_peak, which_read_file_fn()[0],141)

def x_value(which_read_file_fn):
    x_val = which_read_file_fn()[3]
    return array(x_val)+24
=======
    good_data_number = [0,1,3,6, 7]
    return data_files_1, file_name, good_data_number

def peak_sisi():
    sisi_sio = gd.sisi_sio(Readfile()[0],141)
    return sisi_sio

def peak_casi():
    casi_sio = gd.casi_sio(Readfile()[0],141)
    return casi_sio

def x_value():
    x_val = [
    0,
    9,#8.5,
    23,#22.58,
    30,#29.75,
    44,#44.01,
    49,#49.01,
    60,#60.28,
    3600,#3582,
    #6707.98
    ]
    return x_val
>>>>>>> 4fd4d8775961b746663b468da51d99862c5c9d2e

def curve():
    xy = gd.curve(Readfile()[0], 141)
    return xy

def CaSi():
    return gd.CaSi(Readfile()[0], 141)

def pLot():
    plt.close("all")
    f, ax = plt.subplots()

    ax.plot(curve()[0],curve()[1],'o-',label='Si-T')
    ax.plot(curve()[0],curve()[2],'o-',label='casi')

    plt.legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    plt.xlabel('time, hour')
    plt.ylabel('Si-Si/Si-O')
    f.show()
    return

if __name__ == '__main__':
    for i in read_file_with_low_angle_info()[0]:
        print i
