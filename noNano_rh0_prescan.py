# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:00:08 2015

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
    data_files_1=[file('/Users/hty/Google Drive/research/APS exp/chi_files/no_nano_7perc_0rh/no_nano_7p_0rh_prescan/AAS_no_nano_7perc_100rh_Feb26-00000.gr')]
    x_value = [0]
    inc=1
    while inc<4:
        data_files_1.append(file('/Users/hty/Google Drive/research/APS exp/chi_files/no_nano_7perc_0rh/no_nano_7p_0rh_prescan/AAS_no_nano_7perc_100rh_Feb26-0000%s.gr'%(inc)))
        x_value.append(inc)
        inc=inc+1
        
    ''
    inc2=0
    while inc2<4:
        data_files_1.append(file('/Users/hty/Google Drive/research/APS exp/chi_files/no_nano_7perc_0rh/no_nano_7p_0rh_prescan/AAS_no_nano_7perc_100rh_Feb26_1246-0000%s.gr'%(inc2)))
        x_value.append(inc2+3+14/2.5)
        inc2=inc2+1
    return x_value,data_files_1
    ''
    ''

def Data():
    interm_syn = [np.array(Readfile()[1][i].readlines()) for i in range (np.shape(Readfile()[1])[0])]
    
    ''' remember to set start line number here '''
    interm1_syn =[ [str.split(interm_syn[j][i]) for i in range(141,np.shape(interm_syn[j])[0])] for j in range (np.shape(Readfile()[1])[0])]
    
    interm2_syn= [[[float(interm1_syn[k][j][i]) for j in range (0,np.shape(interm1_syn[k])[0])]for i in range (2) ] for k in range (np.shape(Readfile()[1])[0])]
    
    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]
    
    value_of_sisi=[interm2_syn[i][1][local_max[i][7]] for i in range (shape(interm2_syn)[0])]
    value_of_SiO=[interm2_syn[i][1][local_max[i][4]] for i in range (shape(interm2_syn)[0])]
    
    sisi_SiO = array(value_of_sisi)/array(value_of_SiO)
    return Readfile()[0],sisi_SiO


'''
#   read in files with wrong mole fraction
data_files_wrong_frac=[file('/Users/hty/Google Drive/research/APS exp/data/0rh_noNano_wrong_mole_fraction/AAS_no_nano_7perc_0rh_Feb26_1310-00000.gr')]
x_value_w_f = [0]
for i in range (9):
    inc=10+10*i
    data_files_wrong_frac.append(file('/Users/hty/Google Drive/research/APS exp/data/0rh_noNano_wrong_mole_fraction/AAS_no_nano_7perc_0rh_Feb26_1310-000%s.gr'%(inc)))
    x_value_w_f.append(inc)
for j in range (6):
    inc2=100+10*j
    data_files_wrong_frac.append(file('/Users/hty/Google Drive/research/APS exp/data/0rh_noNano_wrong_mole_fraction/AAS_no_nano_7perc_0rh_Feb26_1310-00%s.gr'%(inc2)))
    x_value_w_f.append(inc2)

readl = [np.array(data_files_wrong_frac[i].readlines()) for i in range (np.shape(data_files_wrong_frac)[0])]

""" remember to set start line number here """
splitLine =[ [str.split(readl[j][i]) for i in range(140,np.shape(readl[j])[0])] for j in range (np.shape(data_files_wrong_frac)[0])]

strToFloat= [[[float(splitLine[k][j][i]) for j in range (0,np.shape(splitLine[k])[0])]for i in range (2) ] for k in range (np.shape(data_files_wrong_frac)[0])]

#find local max to denote the peak position
local_max_wrong_frac = [(diff(sign(diff(strToFloat[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(strToFloat)[0])]

value_of_sisi_w_f=[strToFloat[i][1][local_max_wrong_frac[i][7]] for i in range (shape(strToFloat)[0])]
value_of_SiO_w_f=[strToFloat[i][1][local_max_wrong_frac[i][4]] for i in range (shape(strToFloat)[0])]

sisi_SiO_w_f = array(value_of_sisi_w_f)/array(value_of_SiO_w_f)
'''

name_of_the_plot=['0','0.42','1.96','3.33']
def pLot(sAve):
    close("all")
    f, ax = subplots()
    
    ax.plot(array(Data()[0])*2.5/60,Data()[1],'o-',label='correct fraction')  
    #ax.plot(x_value_w_f,sisi_SiO_w_f,'o-',label='wrong frac')  
    legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)
    xlabel('time, hour')
    ylabel('Si-Si/Si-O')
    '''
    #increase the freq of the ticks
    locator_params(axis='x',tight=True,nbins=10)
    grid(axis='x')
    #xlim (1,6)
    ax.axhline(y=0, color='k')
    xlabel(r'r ($\AA$)')
    ylabel('G(r)')
    '''
    
    if sAve ==1:
        f.savefig('/Users/hty/desktop/%s.jpg'%('pdf 7perc noNano 0rh'),dpi=300)
    return

