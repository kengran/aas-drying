# import read_file_quick_check as rf
from numpy import *
from matplotlib.pyplot import *
import sys
sys.path.append('/Users/hty/Google Drive/python_modules')
import getData as gd
import plot_spec as S

def Readfile():
    directory = '/Users/hty/Google Drive/research/aas drying/APS_Dec/zro2/'

    file_name = [directory+'SC_6_scan_22-00000.gr']
    file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Feb/chi_files/no_nano_7perc_0rh/AAS_no_nano_7perc_0rh_Feb26_1310-00000.gr')
    file_name.append('/Users/hty/Google Drive/research/aas drying/APS_Feb/chi_files/nano_7perc_0rh/AAS_np_7p_0rh_Feb26_2223-00000.gr')
    # file_name.append(directory+'AAS_no_nano_7perc_0rh_5h.gr')
    # file_name.append('/Users/hty/Google Drive/research/aas drying/APS exp/chi_files/no_nano_7perc_0rh/doodle_place/AAS_no_nano_7perc_0rh_Feb26_1310-00100.iq')

    data_files_1 = [file(file_name[i]) for i in range (0,shape(file_name)[0])]
    # good_data_number = [0,1]
    good_data_number = arange(shape(file_name)[0])
    return data_files_1, file_name, good_data_number

xy = gd.curve(Readfile()[0], 141)

#change font properties of the plots
font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 17}
matplotlib.rc('font', **font)

# labels = ['xmin=2','xmin=7']
# '%s'%(rf.Readfile()[1][i][-25:])

close("all")
f, ax = subplots(figsize=(10,6))

ax.plot(xy[2][0],(array(xy[2][1]) - array(xy[1][1]))*10,
    c = S.Spec.line_color[3],
    label='Difference curve')
ax.plot(xy[0][0],(array(xy[0][1])),
    c = S.Spec.line_color[-1],
    linewidth=1.5,
    label=r'ZrO$_2$', ls='--')

legend(loc=0, fontsize =14,ncol=1,columnspacing=1, labelspacing=0.1)

xlabel(r'r ($\AA$)')
ylabel('G(r) ($\AA^{-2}$)')
xlim (0,10)
ylim (-10, 25)
#increase the freq of the ticks
locator_params(axis='x',tight=True,nbins=10)
grid(axis='x')
text(1.2, 3, r'$\times$10', fontsize=14)

#add vertical lines at the local max
i_range = [0, 1]
# i_range = range (np.shape(pn.find_local_max(interm2_syn)[1])[0])
argmax_search_start_pt = [200, 300]
location = [argmax(xy[0][1][argmax_search_start_pt[0]:250]),argmax(xy[0][1][argmax_search_start_pt[1]:400]) ]

lengthOftheLine = [0.5, 0.8,0.85,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
[ax.axvline(xy[0][0][argmax_search_start_pt[i]+location[i]],ymin=0,ymax=lengthOftheLine[i],color='k') for i in i_range]

#add names of the peaks
position_y = [8, 19 ,2.5 ,2.5, 3, 3,2,2.7,3.5]
peak_names = ['Zr-O', 'Zr-Zr']
[text(
    xy[0][0][argmax_search_start_pt[i]+location[i]],
    position_y[i], peak_names[i],
    horizontalalignment='center',
    fontsize=14, rotation=80, verticalalignment='bottom')
    for i in i_range]

f.show()

# f.savefig('/Users/hty/desktop/pdf compare %s.pdf'%('aas diff and zro2'))
