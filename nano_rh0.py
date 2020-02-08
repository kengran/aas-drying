# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:03:45 2016

@author: hty
"""


from numpy import *
from matplotlib.pyplot import *
'''
import sys
sys.path.append('/Users/hty/Google Drive/python_modules')
import sub_subplot as ssp
'''

#change font properties of the plots
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)
''
def Readfile():
    #   read in files

    file_name = ['/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/AAS_np_7p_0rh_Feb26_2223-00000.gr']
    data_files_1=[file(file_name[0])]
    x_value = [0]

    inc0=10
    while inc0<100:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/AAS_np_7p_0rh_Feb26_2223-000%s.gr'%(inc0))
        x_value.append(inc0)
        inc0=inc0+10

    inc2=100
    while inc2<150:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/AAS_np_7p_0rh_Feb26_2223-00%s.gr'%(inc2))
        x_value.append(inc2)
        inc2=inc2+10

    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/AAS_np_7p_0rh_Feb27_0530-00000.gr')
    second_start_x = x_value[-1]+13/2.5
    x_value.append(second_start_x)
    inc3=10
    while inc3<100:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/AAS_np_7p_0rh_Feb27_0530-000%s.gr'%(inc3))
        x_value.append(x_value[-1]+10)
        inc3=inc3+10

    [data_files_1.append(file(file_name[i])) for i in range (1,shape(file_name)[0])]

    return x_value,data_files_1,file_name


def read_file_with_low_angle_info():
    '''read in files that contains low angle info'''
    file_name = ['/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/contain low angle info/AAS_np_7p_0rh_Feb26_2223-00000.gr']
    data_files_1=[file(file_name[0])]
    x_value = [0]

    inc0=10
    while inc0<100:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/contain low angle info/AAS_np_7p_0rh_Feb26_2223-000%s.gr'%(inc0))
        x_value.append(inc0)
        inc0=inc0+10

    inc2=100
    while inc2<150:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/contain low angle info/AAS_np_7p_0rh_Feb26_2223-00%s.gr'%(inc2))
        x_value.append(inc2)
        inc2=inc2+10

    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/contain low angle info/AAS_np_7p_0rh_Feb27_0530-00000.gr')
    second_start_x = x_value[-1]+13/2.5
    x_value.append(second_start_x)
    inc3=10
    while inc3<100:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_7perc_0rh/contain low angle info/AAS_np_7p_0rh_Feb27_0530-000%s.gr'%(inc3))
        x_value.append(x_value[-1]+10)
        inc3=inc3+10

    [data_files_1.append(file(file_name[i])) for i in range (1,shape(file_name)[0])]

    return x_value,data_files_1,file_name


def read_reciprocal_space_files(suffix):
    input_name = read_file_with_low_angle_info()[2]
    new_name = [input_name[i][:-3]+suffix for i in range (shape (input_name)[0])]
    data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]

    name_float = array(read_file_with_low_angle_info()[0])*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return  data_files_1, name_str

def peaks(which_read_file_fn):
    interm_syn = [np.array(which_read_file_fn()[1][i].readlines()) for i in range (np.shape(which_read_file_fn()[1])[0])]

def read_reciprocal_space_files(suffix):
    input_name = Readfile()[2]
    new_name = [input_name[i][:-3]+suffix for i in range (shape (input_name)[0])]
    data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]

    name_float = array(Readfile()[0])*2.5/60
    name_str=["{0:.2f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return  data_files_1, name_str

def peaks():
    interm_syn = [np.array(Readfile()[1][i].readlines()) for i in range (np.shape(Readfile()[1])[0])]


    ''' remember to set start line number here '''
    interm1_syn =[ [str.split(interm_syn[j][i]) for i in range(141,np.shape(interm_syn[j])[0])] for j in range (np.shape(interm_syn)[0])]

    interm2_syn= [[[float(interm1_syn[k][j][i]) for j in range (0,np.shape(interm1_syn[k])[0])]for i in range (2) ] for k in range (np.shape(interm_syn)[0])]

    # check if there are non-numbers
    '''
    upper_limit=np.empty(np.shape(interm1)[0],dtype=int)
    for i in range (np.shape(interm1)[0]):
        for j in range (0,np.shape(interm1[i])[0]):
            try:
                float(interm1[i][j][0])
            except ValueError:
                print j
                upper_limit[i] = j
                break
    '''

    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    value_of_sisi=[interm2_syn[i][1][local_max[i][7]] for i in range (shape(interm2_syn)[0])]
    value_of_SiO=[interm2_syn[i][1][local_max[i][4]] for i in range (shape(interm2_syn)[0])]
    value_of_CaSi=[interm2_syn[i][1][local_max[i][8]] for i in range (shape(interm2_syn)[0])]

    sisi_SiO = array(value_of_sisi)/array(value_of_SiO)
    CaSi_SiO=array(value_of_CaSi)/array(value_of_SiO)


    name_float = array(which_read_file_fn()[0])*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    name_float = array(Readfile()[0])*2.5/60
    name_str=["{0:.2f}".format(name_float[i]) for i in range (shape(name_float)[0])]


    return name_str,sisi_SiO, CaSi_SiO



def peak_Si_T(which_read_file_fn):
    return peaks(which_read_file_fn)[1]

def peak_Ca_T(which_read_file_fn):
    return peaks(which_read_file_fn)[2]


def pLot(sAve):
    close("all")
    f, ax = subplots()

    ax.plot(array(Data()[0]),Data()[1],'o-',label='with nano; 0rh')
    #ax.plot(x_value_w_f,sisi_SiO_w_f,'o-',label='wrong frac')
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')
    show()

    if sAve ==1:
        f.savefig('/Users/hty/desktop/%s.jpg'%('pdf 7perc Nano 0rh'),dpi=300)
    return
