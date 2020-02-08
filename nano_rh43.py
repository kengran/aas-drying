# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:03:45 2016

@author: hty
"""


from numpy import *
from matplotlib.pyplot import *
import getData as gd

def read_file_with_low_angle_info():
    file_name = ['/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_1818-00000.gr']
    x_value = [0]

    inc0=10
    while inc0<31:
        file_name.append(
            '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_1818-000%s.gr'%(inc0))
        x_value.append(inc0)
        inc0=inc0+10

    file_name.append(
        '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_1948-00000.gr')
    #   !!calculate the gap between each exp remember to change everytime
    second_start_x = x_value[-1] + 15/2.5
    x_value.append(second_start_x)

    inc1=30
    while inc1<91:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_1948-000%s.gr'%(inc1))
        x_value.append(x_value[-1]+30)
        inc1=inc1+30

    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_2355-00000.gr')
    x_value.append(x_value[-1]+22/2.5)

    file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_2355-00050.gr')
    x_value.append(x_value[-1]+50)

    inc2=100
    while inc2<155:
        file_name.append('/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/contain low angle info/AAS_np_7p_50rh_Feb27_2355-00%s.gr'%(inc2))
        x_value.append(x_value[-1]+50)
        inc2=inc2+50

    data_files_1 = [file(file_name[i]) for i in range (len(file_name))]
    return x_value,data_files_1,file_name



def Readfile():
    #   read in old files
    directory = '/Users/hty/Google Drive/research/aas drying/aps_feb/chi_files/nano_43rh/'

    file_name = [directory+'AAS_np_7p_50rh_Feb27_1818-00000.gr']
    data_files_1=[file(file_name[0])]
    x_value = [0]

    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-0000%s.gr'%(5))
    data_files_1.append(file(file_name[-1]))
    x_value.append(5)

#==============================================================================
#     file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-0000%s.gr'%(7))
#     data_files_1.append(file(file_name[-1]))
#     x_value.append(7)
#==============================================================================

    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-0000%s.gr'%(8))
    data_files_1.append(file(file_name[-1]))
    x_value.append(8)


    inc0=10
    while inc0<11:
        file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-000%s.gr'%(inc0))
        data_files_1.append(file(file_name[-1]))
        x_value.append(inc0)
        inc0=inc0+10

    num = 13
    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-000%s.gr'%(num))
    data_files_1.append(file(file_name[-1]))
    x_value.append(num)

    incc = 15
    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-000%s.gr'%(incc))
    data_files_1.append(file(file_name[-1]))
    x_value.append(incc)

    incc = 20
    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-000%s.gr'%(incc))
    data_files_1.append(file(file_name[-1]))
    x_value.append(incc)

    incc = 30
    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1818-000%s.gr'%(incc))
    data_files_1.append(file(file_name[-1]))
    x_value.append(incc)

    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1948-00000.gr')
    data_files_1.append(file(file_name[-1]))
    #   !!calculate the gap between each exp remember to change everytime
    second_start_x = x_value[-1] + 15/2.5
    x_value.append(second_start_x)

    inc1=10
    while inc1<44:
        file_name.append(directory+'AAS_np_7p_50rh_Feb27_1948-000%s.gr'%(inc1))
        data_files_1.append(file(file_name[-1]))
        x_value.append(x_value[-1]+10)
        inc1=inc1+10


    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1948-00080.gr')
    data_files_1.append(file(file_name[-1]))
    x_value.append(x_value[-1]+40)


    file_name.append(directory+'AAS_np_7p_50rh_Feb27_1948-00090.gr')
    data_files_1.append(file(file_name[-1]))
    x_value.append(x_value[-1]+10)

    file_name.append(directory+'AAS_np_7p_50rh_Feb27_2355-00000.gr')
    data_files_1.append(file(file_name[-1]))
    x_value.append(x_value[-1]+22/2.5)

    file_name.append(directory+'AAS_np_7p_50rh_Feb27_2355-00050.gr')
    data_files_1.append(file(file_name[-1]))
    x_value.append(x_value[-1]+50)

    inc2=100
    while inc2<155:
        file_name.append(directory+'AAS_np_7p_50rh_Feb27_2355-00%s.gr'%(inc2))
        data_files_1.append(file(file_name[-1]))
        x_value.append(x_value[-1]+50)
        inc2=inc2+50

    return x_value,data_files_1,file_name


def curve():
    xy = gd.curve(Readfile()[1], 141)
    return xy


def read_reciprocal_space_files(suffix, which_read_file_fn):
    input_name = which_read_file_fn()[2]
    new_name = [input_name[i][:-3]+suffix for i in range (shape (input_name)[0])]
    data_files_1 = [file(new_name[i]) for i in range (shape (input_name)[0])]

    name_float = array(which_read_file_fn()[0])*2.5/60
    name_str=["{0:.1f}".format(name_float[i]) for i in range (shape(name_float)[0])]

    return  data_files_1, name_str


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

    return name_str,sisi_SiO, CaSi_SiO


def pLot(sAve):
    plt.close("all")
    f, ax = plt.subplots()

    ax.plot(array(Data()[0][0:9]),Data()[2][0:9],'o-',label='with nano; 43rh')
    #ax.plot(x_value_w_f,sisi_SiO_w_f,'o-',label='wrong frac')
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')


    if sAve ==1:
        f.savefig('/Users/hty/desktop/%s.eps'%('pdf 7perc Nano 0rh'))
    return

if __name__ == "__main__":
    for item in Readfile()[2]:
        print item
