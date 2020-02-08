from numpy import *

def find_local_max(interm2_syn):
    #find local max to denote the peak position
    local_max = (diff(sign(diff(interm2_syn[1]))) < 0).nonzero()[0] + 1

    peakPosition=[
        # 0.8060531,
        interm2_syn[0][local_max[1]],
        1.17, 1.619368611,
        interm2_syn[0][local_max[3]],
        2.252014246,
        interm2_syn[0][local_max[4]],

        interm2_syn[0][local_max[5]],
        interm2_syn[0][local_max[6]],
        interm2_syn[0][local_max[7]],
        interm2_syn[0][local_max[8]],
       ]

    return local_max, peakPosition

def name_of_the_peak():
    nameOfthePeak = ['H','C', 'H','C','C','H','C','C/H','C/H','C','Ca-O', 'x', 'x']

    # [nameOfthePeak.append(str(interm2_syn[0][find_local_max(interm2_syn)[0][0][i]])) for i in peak_loc]

    return nameOfthePeak

def peak_pos_0rh(interm2_syn, sample, plot_type):
    # index = find_local_max(interm2_syn)[0]
    index = (diff(sign(diff(interm2_syn[1]))) < 0).nonzero()[0] + 1
    if plot_type == '.sq':

        if sample == 'noNano_rh0' or sample == 'nano_rh0':
            # peakPosition = find_local_max(interm2_syn)[1]
            peakPosition=[
                interm2_syn[0][index[1]],
                1.17, 1.619368611,
                interm2_syn[0][index[2]],2.252014246,
                interm2_syn[0][index[3]],
                interm2_syn[0][index[4]],
                interm2_syn[0][index[5]],
                interm2_syn[0][index[6]],
                interm2_syn[0][index[7]]
                ]
        elif sample == 'noNano_rh43':
            peakPosition=[
               interm2_syn[0][index[3]],
               1.17, 1.619368611,
               interm2_syn[0][index[4]],2.252014246,
               interm2_syn[0][index[5]],
               interm2_syn[0][index[6]],
               interm2_syn[0][index[7]],
               interm2_syn[0][index[8]],
               interm2_syn[0][index[9]]
               ]
        elif sample =='nano_rh43':
            peakPosition=[
                interm2_syn[0][index[1]],
                1.17, 1.619368611,
                interm2_syn[0][index[2]],2.252014246,
                interm2_syn[0][index[3]],
                interm2_syn[0][index[6]],
                interm2_syn[0][index[7]],
                interm2_syn[0][index[8]],
                interm2_syn[0][index[9]]
                ]
        else:
            print 'testing'
            peakPosition = find_local_max(interm2_syn)[1]
        #    peakPosition=[interm2_syn[0][index[1]],1.619368611,
        #        interm2_syn[0][index[2]],2.252014246,
        #        interm2_syn[0][index[3]],
        #        interm2_syn[0][index[4]],interm2_syn[0][index[5]],
        #        interm2_syn[0][index[6]]
        #       ]
    elif plot_type == '.iq':
        if sample == 'noNano_rh0':
            peakPosition=[interm2_syn[0][index[1]],1.619368611,
                interm2_syn[0][index[2]],2.252014246,
                interm2_syn[0][index[3]],
                interm2_syn[0][index[7]],interm2_syn[0][index[8]],
                interm2_syn[0][index[9]]
               ]
        else:
           peakPosition=[interm2_syn[0][index[1]],1.619368611,
               interm2_syn[0][index[2]],2.252014246,
               interm2_syn[0][index[3]],
               interm2_syn[0][index[8]],interm2_syn[0][index[9]],
               interm2_syn[0][index[10]]
              ]
    return peakPosition

def vline_and_label_pos (sample, plot_type):
    if plot_type == '.sq':
        if sample == 'noNano_rh0':
            min_of_the_line = [
                0.1, 0.1, 0.18, 0.75, 0.6,
                0.35, 0.55, 0.5, 0.55, 0.5,
                0.8, 0.8, 0.8]
            position_y = [
                0.2, 0.2, 0.4, 2.47 , 1.9,
                1, 1.8, 1.6, 1.8, 1.6,
                2, 2, 2]
        else:
            min_of_the_line = [
                0.1, 0.1, 0.18, 0.75, 0.6,
                0.35, 0.55, 0.5, 0.55, 0.5,
                0.8, 0.8, 0.8]
            position_y = [
                0.2, 0.2, 0.4, 2.47 , 1.9,
                1, 1.8, 1.6, 1.8, 1.6,
                2, 2, 2]
    else:
        if sample == 'noNano_rh0':
            min_of_the_line = [0, 0.1, 0.73, 0.53, 0.22, 0.3, 0.2, 0.2, 0.8,0.8, 0.8, 0.8]
            position_y = [900000, 1200000, 3300000 , 2700000, 1500000, 1800000, 1500000, 1500000,1.5, 2, 2, 2]
        else:
            min_of_the_line = [0, 0.1, 0.71, 0.53, 0.22, 0.3, 0.2, 0.2, 0.8,0.8, 0.8, 0.8]
            position_y = [900000, 1200000, 3300000 , 2700000, 1500000, 1800000, 1500000, 1500000,1.5, 2, 2, 2]
    return min_of_the_line, position_y
