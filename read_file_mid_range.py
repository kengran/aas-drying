from numpy import *
# import sys
# sys.path.append('/Users/hty/Google Drive/python_modules')
# import getData as gd

def Readfile(sample, rh):
    if rh == 0:
        if sample == 'no nano':
            directory = '/Users/hty/Google Drive/research/aas drying/data used in manuscript/nonano 0rh manuscript/x-axis-higher-res.001/'

            file_name = [directory+'AAS_no_nano_7perc_0rh_0h.gr']
            file_name.append(directory+'AAS_no_nano_7perc_0rh_0pt4h.gr')
            file_name.append(directory+'AAS_no_nano_7perc_0rh_2h.gr')
            file_name.append(directory+'AAS_no_nano_7perc_0rh_5h.gr')
        else:
            directory = '/Users/hty/Google Drive/research/aas drying/data used in manuscript/nano 0rh manuscript/x-axis-higher-res/'

            file_name = [directory+'AAS_np_7p_0rh_0h.gr']
            file_name.append(directory+'AAS_np_7p_0rh_3h.gr')
            file_name.append(directory+'AAS_np_7p_0rh_6h.gr')
            file_name.append(directory+'AAS_np_7p_0rh_10h.gr')
    elif rh == 43:
        if sample == 'no nano':
            directory = '/Users/hty/Google Drive/research/aas drying/data used in manuscript/nonano 43rh/x-axis-higher-res/'

            file_name = [directory+'AAS_noNP_7p_50rh_Feb28_1451-00000.gr']
            file_name.append(directory+'AAS_noNP_7p_50rh_Feb28_1451-00050.gr')
            file_name.append(directory+'AAS_noNP_7p_50rh_Feb28_1451-00100.gr')
            file_name.append(directory+'AAS_noNP_7p_50rh_Feb28_1451-00150.gr')
        else:
            directory = '/Users/hty/Google Drive/research/aas drying/data used in manuscript/nano 43rh/x-axis-higher-res/'

            file_name = [directory+'AAS_np_7p_50rh_Feb27_1818-00000.gr']
            file_name.append(directory+'AAS_np_7p_50rh_Feb27_1948-00060.gr')
            file_name.append(directory+'AAS_np_7p_50rh_Feb27_2355-00050.gr')
            file_name.append(directory+'AAS_np_7p_50rh_Feb27_2355-00150.gr')
    else:
        print "wrong rh value!!"

    data_files_1 = [file(file_name[i]) for i in range (0,shape(file_name)[0])]
    # good_data_number = [0,1]
    good_data_number = arange(shape(file_name)[0])
    return data_files_1, file_name, good_data_number
