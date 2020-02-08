# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:00:08 2015

@author: hty
"""

from numpy import *
from matplotlib.pyplot import *

def Readfile():
    '''read in files that contain low angle info'''
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/no_nano_7perc_0rh/'
    file_name = [directory + 'AAS_no_nano_7perc_0rh_Feb26_1310-00000.gr']
    data_files_1=[file(file_name[0])]
    x_value = [0]

    inc0=1
    while inc0<10:
        file_name.append(directory + 'AAS_no_nano_7perc_0rh_Feb26_1310-0000%s.gr'%(inc0))
        x_value.append(inc0)
        inc0=inc0+1

    inc=10
    while inc<50:
        file_name.append(directory + 'AAS_no_nano_7perc_0rh_Feb26_1310-000%s.gr'%(inc))
        x_value.append(inc)
        inc=inc+5

    inc=55
    while inc<100:
        file_name.append(directory + 'AAS_no_nano_7perc_0rh_Feb26_1310-000%s.gr'%(inc))
        x_value.append(inc)
        inc=inc+5

    inc2=110
    while inc2<151:
        file_name.append(directory + 'AAS_no_nano_7perc_0rh_Feb26_1310-00%s.gr'%(inc2))
        x_value.append(inc2)
        inc2=inc2+10

    [data_files_1.append(file(file_name[i])) for i in range (1,shape(file_name)[0])]

    return x_value,data_files_1, file_name

def read_reciprocal_space_files(suffix):
    input_name = Readfile()[2]
    new_name = [input_name[i][:-3]+suffix for i in range (shape (input_name)[0])]
    data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]

    name_float = array(Readfile()[0])*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return  data_files_1, name_str

def read_reciprocal_space_files_d95(suffix):
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/no_nano_7perc_0rh/'

    file_name = [directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-00000']
    x_value = [0]

    inc0=10
    while inc0<30:
        file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-000%s'%(inc0))
        x_value.append(inc0)
        inc0=inc0+10

    # inc0 = 22
    # file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-000%s'%(inc0))
    # x_value.append(inc0)

    # inc0 = 23
    # file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-000%s'%(inc0))
    # x_value.append(inc0)

    # inc0 = 24
    # file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-000%s'%(inc0))
    # x_value.append(inc0)

    # inc0 = 26
    # file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-000%s'%(inc0))
    # x_value.append(inc0)

    inc0=30
    while inc0<60:
        file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-000%s'%(inc0))
        x_value.append(inc0)
        inc0=inc0+20

    inc2=100
    while inc2<160:
        file_name.append(directory + 'xmin_2_for_rec_space/AAS_no_nano_7perc_0rh_Feb26_1310-00%s'%(inc2))
        x_value.append(inc2)
        inc2=inc2+50

    new_name = [file_name[i]+ suffix for i in range (shape (file_name)[0])]
    data_files_1 = [file(new_name[i]) for i in range (shape (file_name)[0])]

    name_float = array(x_value)*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return data_files_1, name_str

def peaks(which_read_file_fn):
    interm_syn = [np.array(which_read_file_fn()[1][i].readlines()) for i in range (np.shape(which_read_file_fn()[1])[0])]

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


    return name_str, sisi_SiO,CaSi_SiO

def peak_Si_T(which_read_file_fn):
    return peaks(which_read_file_fn)[1]

def peak_Ca_T(which_read_file_fn):
    return peaks(which_read_file_fn)[2]


# name_of_the_plot=['0','0.42','1.96','3.33']

def pLot(sAve):
    close("all")

    f, ax = subplots(1, sharex=True, figsize = (10,10))
    ax.plot(array(Readfile()[0])*2.5/60,Data()[1],'o-',label='SiSi/SiO')
    ax.plot(array(Readfile()[0])*2.5/60,array(Data()[2]),'o-',label='CaSi/SiO')
    ax.legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)

    show()

    if sAve ==1:
        f.savefig('/Users/hty/desktop/%s.jpg'%('pdf 7perc noNano 0rh'),dpi=300)

#if __name__ == '__main__':