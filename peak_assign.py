from numpy import *

#peaks afer 15A for noNano_ctrl case
# peak_loc = [31,32,35]

#peaks afer 15A for nano_ctrl case
peak_loc = [35,38,42]

def find_local_max(interm2_syn):
    #find local max to denote the peak position
    local_max = [(diff(sign(diff(interm2_syn[i][1]))) < 0).nonzero()[0] + 1 for i in range (shape(interm2_syn)[0])]

    peakPosition=[interm2_syn[0][0][local_max[0][4]],interm2_syn[0][0][local_max[0][5]],
        interm2_syn[0][0][local_max[0][6]],2.6,
        interm2_syn[0][0][local_max[0][7]],interm2_syn[0][0][local_max[0][8]],
        3.9,interm2_syn[0][0][local_max[0][9]],
        interm2_syn[0][0][local_max[0][10]],

        # peak position after 15A
        interm2_syn[0][0][local_max[0][peak_loc[0]]], interm2_syn[0][0][local_max[0][peak_loc[1]]]
        , interm2_syn[0][0][local_max[0][peak_loc[2]]]
       ]

    return local_max, peakPosition

def name_of_the_peak(interm2_syn):
    nameOfthePeak = ['T-O','Al/Mg-O','Ca-O','O-O','Si-T','Ca-T','Ca-Ca','T-O','Ca-O']

    [nameOfthePeak.append(str(interm2_syn[0][0][find_local_max(interm2_syn)[0][0][i]])) for i in peak_loc]

    return nameOfthePeak
