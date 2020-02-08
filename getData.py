# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 11:31:12 2016

@author: hty
"""

from numpy import *

def curve(Readfiles,starting_line):
    interm_syn = [array(Readfiles[i].readlines()) for i in range (shape(Readfiles)[0])]

    ''' remember to set start line number here '''
    interm1_syn =[ [str.split(interm_syn[j][i])
        for i in range(starting_line,shape(interm_syn[j])[0])]
        for j in range (shape(interm_syn)[0])]

    interm2_syn= [[[float(interm1_syn[k][j][i])
        for j in range (0,shape(interm1_syn[k])[0])]
        for i in range (shape(interm1_syn[k][0])[0]) ]
        for k in range (shape(interm_syn)[0])]

    # check if there are non-numbers
    '''
    upper_limit=empty(shape(interm1)[0],dtype=int)
    for i in range (shape(interm1)[0]):
        for j in range (0,shape(interm1[i])[0]):
            try:
                float(interm1[i][j][0])
            except ValueError:
                print j
                upper_limit[i] = j
                break
    '''

    return interm2_syn

def norm_peak(which_peak, Readfiles, starting_line):
    interm2_syn=curve(Readfiles,starting_line)

    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    value_of_SiO=[interm2_syn[i][1][local_max[i][4]] for i in range (shape(interm2_syn)[0])]

    if which_peak == 'si-t' or which_peak == 'Si-T':
        value_of_peak=[interm2_syn[i][1][local_max[i][7]] for i in range (shape(interm2_syn)[0])]
        norm_int = array(value_of_peak)/array(value_of_SiO)
    elif which_peak == 'ca-t' or which_peak == 'Ca-T':
        value_of_casi=[interm2_syn[i][1][local_max[i][8]] for i in range (shape(interm2_syn)[0])]
        norm_int = array(value_of_casi)/array(value_of_SiO)
    elif which_peak == 'ca-o' or which_peak == 'Ca-O':
        value_of_peak=[interm2_syn[i][1][local_max[i][6]] for i in range (shape(interm2_syn)[0])]
        norm_int = array(value_of_peak)/array(value_of_SiO)
    else:
        print ("Wrong input!")

    return norm_int

def peak(which_peak, Readfiles, starting_line):
    interm2_syn=curve(Readfiles,starting_line)

    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    if which_peak == 'si-t' or which_peak == 'Si-T':
        value_of_peak=array([interm2_syn[i][1][local_max[i][7]] for i in range (shape(interm2_syn)[0])])
    elif which_peak == 'ca-t' or which_peak == 'Ca-T':
        value_of_peak=array([interm2_syn[i][1][local_max[i][8]] for i in range (shape(interm2_syn)[0])])
    elif which_peak == 'ca-o' or which_peak == 'Ca-O':
        value_of_peak= array([interm2_syn[i][1][local_max[i][6]] for i in range (shape(interm2_syn)[0])])
    elif which_peak == 'T-O':
        value_of_peak= array([interm2_syn[i][1][local_max[i][4]] for i in range (shape(interm2_syn)[0])])

    else:
        print ("Wrong input!")

    return value_of_peak

def sisi_sio(Readfiles,starting_line):
    interm2_syn=curve(Readfiles,starting_line)

    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    value_of_sisi=[interm2_syn[i][1][local_max[i][7]] for i in range (shape(interm2_syn)[0])]
    value_of_SiO=[interm2_syn[i][1][local_max[i][4]] for i in range (shape(interm2_syn)[0])]

    sisi_SiO = array(value_of_sisi)/array(value_of_SiO)
    return sisi_SiO


def casi_sio(Readfiles,starting_line):
    interm2_syn=curve(Readfiles,starting_line)

    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    value_of_casi=[interm2_syn[i][1][local_max[i][8]] for i in range (shape(interm2_syn)[0])]
    value_of_SiO=[interm2_syn[i][1][local_max[i][4]] for i in range (shape(interm2_syn)[0])]

    casi_SiO = array(value_of_casi)/array(value_of_SiO)
    return casi_SiO

def CaSi(Readfiles,starting_line):
    interm2_syn=curve(Readfiles,starting_line)

    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    value_of_casi=[interm2_syn[i][1][local_max[i][8]] for i in range (shape(interm2_syn)[0])]
    return value_of_casi
