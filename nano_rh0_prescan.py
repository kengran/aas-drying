# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 13:42:32 2016

@author: hty
"""
from numpy import *
from matplotlib.pyplot import *

def Readfile():
    #prescan

    files_prescan=[file('/Users/hty/Google Drive/research/APS exp/chi_files/nano_7p_0rh_prescan/AAS_np_7p_100rh_Feb26_2207-00000.gr')]
    inc_ps=1
    x_val_ps=[0]
    while inc_ps<4:
        files_prescan.append(file('/Users/hty/Google Drive/research/APS exp/chi_files/nano_7p_0rh_prescan/AAS_np_7p_100rh_Feb26_2207-0000%s.gr'%(inc_ps)))
        x_val_ps.append(inc_ps)
        inc_ps=inc_ps+1
    x_val_ps=array(x_val_ps)-x_val_ps[-1]-10/2.5
    return x_val_ps,files_prescan

def Data():
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
    
    sisi_SiO = array(value_of_sisi)/array(value_of_SiO)
    return Readfile()[0],sisi_SiO


def pLot(sAve):
    plt.close("all")
    f, ax = plt.subplots()
    
    ax.plot(array(Data()[0])*2.5/60,Data()[1],'o-',label='with nano')  
    #ax.plot(x_value_w_f,sisi_SiO_w_f,'o-',label='wrong frac')  
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')
    
    
    if sAve ==1:
        f.savefig('/Users/hty/desktop/%s.jpg'%('pdf 7perc Nano 0rh'),dpi=300)
    return

