# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:29:30 2016

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *
import sys
sys.path.append('/Users/hty/Google Drive/python_modules')

import getData as gd

def read_file_with_low_angle_info():
    directory = '/Users/hty/Google Drive/research/aas drying/APS_Feb/chi_files/noNano_50rh/contain low angle info/'
    file_name = [directory + 'AAS_noNP_7p_50rh_Feb28_1451-00000.gr']
    data_files_1=[file(file_name[0])]
    x_value = [0]

    file_name.append(directory + 'AAS_noNP_7p_50rh_Feb28_1451-00060.gr')
    x_value.append(60)

    file_name.append(directory + 'AAS_noNP_7p_50rh_Feb28_1451-00120.gr')
    x_value.append(120)

    file_name.append(directory + 'AAS_noNP_7p_50rh_Feb28_1451-00180.gr')
    x_value.append(180)

    data_files_1 = [file(file_name[i]) for i in range (len(file_name))]
    return x_value,data_files_1,file_name


def Readfile():
    #   read in files
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/noNano_50rh/'
    file_name = [directory + 'AAS_noNP_7p_50rh_Feb28_1451-00000.gr']
    data_files_1=[file(file_name[0])]
    x_value = [0]

    inc=10
    while inc<100:
        file_name.append(directory + 'AAS_noNP_7p_50rh_Feb28_1451-000%s.gr'%(inc))
        x_value.append(inc)
        inc=inc+10

    inc1=100
    while inc1<200:
        file_name.append(directory + 'AAS_noNP_7p_50rh_Feb28_1451-00%s.gr'%(inc1))
        x_value.append(inc1)
        inc1=inc1+10

    [data_files_1.append(file(file_name[i])) for i in range (1,shape(file_name)[0])]

    return x_value,data_files_1, file_name

def peaks(which_read_file_fn):
    sisi_sio = gd.sisi_sio(which_read_file_fn()[1],141)
    casi_sio = gd.casi_sio(which_read_file_fn()[1],141)

    #Time = array(which_read_file_fn()[0])*2.5/60
    name_float = array(which_read_file_fn()[0])*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return name_str,sisi_sio,casi_sio

def read_reciprocal_space_files(suffix, which_read_file_fn):
    input_name = which_read_file_fn()[2]
    new_name = [input_name[i][:-3]+suffix for i in range (shape (input_name)[0])]
    data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]

    name_float = array(which_read_file_fn()[0])*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return  data_files_1, name_str

def pLot(sAve):
    close("all")
    f, ax = subplots()

    ax.plot(array(peaks(Readfile)[0]),peaks(Readfile)[1],'o-',label='noNano 50rh')
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')

    f.show()

    if sAve ==1:
        f.savefig('/Users/hty/desktop/%s.jpg'%('pdf noNano 50rh'),dpi=300)
    return

if __name__ == "__main__":
    print read_reciprocal_space_files('.sq', read_file_with_low_angle_info)[1]
